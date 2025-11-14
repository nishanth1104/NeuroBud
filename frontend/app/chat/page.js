'use client'

import { useState, useRef, useEffect } from 'react'
import axios from 'axios'
import Link from 'next/link'
import { useSession, signOut } from 'next-auth/react'
import ReactMarkdown from 'react-markdown'
import { useAdmin } from '../hooks/useAdmin'

export default function ChatPage() {
  const { data: session } = useSession()
  const { isAdmin } = useAdmin()
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [conversationId, setConversationId] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const [isOffline, setIsOffline] = useState(false)
  const [messageCount, setMessageCount] = useState(0)
  const [showBreakReminder, setShowBreakReminder] = useState(false)
  const [feedbackGiven, setFeedbackGiven] = useState({}) // Track which messages have feedback
  const [showRating, setShowRating] = useState({}) // Track which message shows rating UI
  const messagesEndRef = useRef(null)
  

  // Auto-scroll to bottom
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  // Detect online/offline status
  useEffect(() => {
    const handleOnline = () => {
      setIsOffline(false)
      setError(null)
    }
    
    const handleOffline = () => {
      setIsOffline(true)
      setError('You are offline. Messages will not be sent until you reconnect.')
    }
    
    window.addEventListener('online', handleOnline)
    window.addEventListener('offline', handleOffline)
    
    // Check initial status
    if (!navigator.onLine) {
      handleOffline()
    }
    
    return () => {
      window.removeEventListener('online', handleOnline)
      window.removeEventListener('offline', handleOffline)
    }
  }, [])

  const copyMessage = (content) => {
    navigator.clipboard.writeText(content)
  }

  const submitFeedback = async (messageId, wasHelpful, rating = null, feedbackText = null) => {
    try {
      await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/api/feedback`, {
        message_id: messageId,
        was_helpful: wasHelpful,
        user_rating: rating,
        user_feedback: feedbackText
      })
      
      // Mark this message as having feedback
      setFeedbackGiven(prev => ({
        ...prev,
        [messageId]: { wasHelpful, rating, feedbackText }
      }))
      
      // Hide rating UI after submission
      setShowRating(prev => ({
        ...prev,
        [messageId]: false
      }))
      
      console.log('Feedback submitted successfully')
    } catch (error) {
      console.error('Error submitting feedback:', error)
    }
  }

  const sendMessageWithRetry = async (userMessage, retries = 3) => {
    for (let attempt = 1; attempt <= retries; attempt++) {
      try {
        const response = await axios.post(
          `${process.env.NEXT_PUBLIC_API_URL}/api/chat`,
          {
            message: userMessage,
            conversation_id: conversationId,
            user_email: session?.user?.email || null
          },
          {
            timeout: 30000
          }
        )
        return response
      } catch (error) {
        if (attempt === retries) {
          throw error
        }
        
        // Wait before retry (exponential backoff)
        await new Promise(resolve => setTimeout(resolve, 1000 * attempt))
      }
    }
  }

  const sendMessage = async () => {
    if (!input.trim() || isLoading) return
    
    // Validation
    if (input.trim().length > 2000) {
      setError('Message too long (max 2000 characters)')
      return
    }
    
    if (input.trim().length < 2) {
      setError('Message too short (min 2 characters)')
      return
    }

    const userMessage = input.trim()
    setInput('')
    setIsLoading(true)
    setError(null)

    setMessages(prev => [...prev, { role: 'user', content: userMessage }])
    
    const newCount = messageCount + 1
    setMessageCount(newCount)
    
    if (newCount === 15) {
      setShowBreakReminder(true)
      setTimeout(() => setShowBreakReminder(false), 10000)
    }

    try {
      // Use retry logic
      const response = await sendMessageWithRetry(userMessage)

      if (!conversationId) {
        setConversationId(response.data.conversation_id)
      }

      // Get message ID from response (we need to track it)
      const messageId = Date.now() // Temporary ID for frontend tracking

      setMessages(prev => [...prev, { 
        id: response.data.message_id,
        role: 'assistant', 
        content: response.data.response,
        is_crisis: response.data.is_crisis,
        crisis_severity: response.data.crisis_severity
      }])

    } catch (error) {
      console.error('Error sending message:', error)
      
      let errorMessage = 'Sorry, I had trouble connecting. Please try again.'
      
      if (error.code === 'ECONNABORTED') {
        errorMessage = 'Request timed out. The server might be slow. Please try again.'
      } else if (error.response) {
        if (error.response.status === 429) {
          errorMessage = 'Too many requests. Please wait a moment before trying again.'
        } else if (error.response.status === 500) {
          errorMessage = 'Server error. Please try again in a moment.'
        } else {
          errorMessage = error.response.data?.message || errorMessage
        }
      } else if (error.request) {
        errorMessage = 'Cannot reach server. Please check your internet connection.'
        setIsOffline(true)
      }
      
      setError(errorMessage)
      
      setMessages(prev => [...prev, { 
        id: Date.now(),
        role: 'assistant', 
        content: errorMessage,
        error: true
      }])
    } finally {
      setIsLoading(false)
    }
  }

  const handleKeyPress = (e) => {
    // Send on Enter (without Shift)
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
    }
    
    // Clear input on Escape
    if (e.key === 'Escape') {
      setInput('')
    }
  }

  return (
    <div className="flex flex-col h-screen bg-gray-50">
      {/* Header */}
      <nav className="bg-white border-b shadow-sm">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <Link href="/" className="text-2xl font-bold text-blue-600 flex items-center gap-2">
            🌱 Neurobud
          </Link>
          <div className="flex items-center gap-4">
            <Link href="/chat" className="text-blue-600 font-semibold border-b-2 border-blue-600">
              Chat
            </Link>
            <Link href="/mood" className="text-gray-600 hover:text-blue-600 font-medium">
              Mood
            </Link>
            <Link href="/resources" className="text-gray-600 hover:text-blue-600 font-medium">
              Resources
            </Link>
            {/* Admin Link - Only show if admin */}
            {isAdmin && (
              <Link href="/admin" className="text-purple-600 hover:text-purple-700 font-medium flex items-center gap-1">
                ⚙️ Admin
              </Link>
            )}
            {/* User Profile */}
            <UserProfile />
          </div>
        </div>
      </nav>

      {/* Disclaimer Banner */}
      <div className="bg-yellow-50 border-b border-yellow-200 px-4 py-2">
        <p className="text-center text-sm text-yellow-800">
          <strong>⚠️ Reminder:</strong> Neurobud is an AI companion, not a therapist. 
          For professional help: <Link href="/resources" className="underline font-bold">Find a therapist</Link> | 
          In crisis? <strong>Call 988</strong>
        </p>
      </div>

      {/* Error Banner */}
      {error && (
        <div className="bg-red-50 border-b border-red-200 px-4 py-3 animate-fade-in">
          <p className="text-center text-sm text-red-800">
            <strong>⚠️ Error:</strong> {error}
            {isOffline && (
              <button 
                onClick={() => window.location.reload()} 
                className="ml-2 underline font-bold"
              >
                Retry
              </button>
            )}
          </p>
        </div>
      )}

      {/* Break Reminder */}
      {showBreakReminder && (
        <div className="bg-purple-50 border-b border-purple-200 px-4 py-3 animate-fade-in">
          <p className="text-center text-sm text-purple-800">
            <strong>💜 Gentle reminder:</strong> You've been chatting for a while. 
            Consider taking a break, getting some water, or trying a 
            <Link href="/resources" className="underline font-bold ml-1">coping strategy</Link>.
          </p>
        </div>
      )}

      {/* Chat Messages */}
      <div className="flex-1 overflow-y-auto px-6 py-8">
        <div className="max-w-4xl mx-auto space-y-6">
          {messages.length === 0 && (
            <div className="text-center text-gray-500 mt-20 animate-fade-in">
              <div className="text-8xl mb-6 animate-bounce">💬</div>
              <p className="text-2xl font-semibold text-gray-700 mb-2">Start a conversation...</p>
              <p className="text-base text-gray-600 mb-6">Share what's on your mind. I'm here to listen.</p>
              <div className="bg-blue-50 border-2 border-blue-200 rounded-xl p-4 max-w-md mx-auto">
                <p className="text-sm text-blue-800">
                  💡 <strong>Try asking:</strong> "I'm feeling anxious" or "Can you help me relax?"
                </p>
              </div>
            </div>
          )}

          {messages.map((message, index) => (
            <div key={index}>
              {/* User Message */}
              {message.role === 'user' && (
                <div className="flex justify-end animate-fade-in">
                  <div className="bg-blue-600 text-white max-w-3xl px-6 py-4 rounded-2xl">
                    {message.content}
                  </div>
                </div>
              )}

              {/* Assistant Message */}
              {message.role === 'assistant' && (
                <div className="flex flex-col items-start gap-2 animate-fade-in group">
                  <div className="flex items-start gap-3 w-full">
                    <div className="w-8 h-8 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center text-white font-bold flex-shrink-0">
                      AI
                    </div>
                    <div className={`flex-1 max-w-3xl px-6 py-4 rounded-2xl rounded-tl-none ${
                      message.is_crisis
                        ? 'bg-red-50 border-2 border-red-300'
                        : message.error
                        ? 'bg-red-50 border-2 border-red-200'
                        : 'bg-white border border-gray-200 shadow-sm'
                    }`}>
                      {/* Header */}
                      <div className="flex items-center justify-between mb-2">
                        <div className="flex items-center gap-2">
                          <span className="font-semibold text-sm text-gray-700">Neurobud</span>
                          {message.is_crisis && (
                            <span className="text-red-600 font-bold text-xs">🆘 CRISIS ALERT</span>
                          )}
                        </div>
                        {!message.error && (
                          <button
                            onClick={() => copyMessage(message.content)}
                            className="opacity-0 group-hover:opacity-100 text-xs text-gray-500 hover:text-gray-700 transition-opacity"
                            title="Copy message"
                          >
                            📋 Copy
                          </button>
                        )}
                      </div>

                      {/* Message Content */}
                      <div className="prose prose-sm max-w-none">
                        <ReactMarkdown
                          components={{
                            strong: ({node, ...props}) => <span className="font-bold" {...props} />,
                            ul: ({node, ...props}) => <ul className="list-disc ml-4 my-2" {...props} />,
                            ol: ({node, ...props}) => <ol className="list-decimal ml-4 my-2" {...props} />,
                            p: ({node, ...props}) => <p className="mb-2" {...props} />,
                          }}
                        >
                          {message.content}
                        </ReactMarkdown>
                      </div>
                    </div>
                  </div>

                  {/* Feedback UI - Only for non-error, non-crisis messages */}
                  {!message.error && !message.is_crisis && message.id && (
                    <div className="ml-11 flex items-center gap-2">
                      {!feedbackGiven[message.id] ? (
                        <>
                          {/* Thumbs Up/Down */}
                          <button
                            onClick={() => submitFeedback(message.id, true)}
                            className="text-gray-400 hover:text-green-600 transition-colors p-1 rounded hover:bg-green-50"
                            title="Helpful"
                          >
                            👍
                          </button>
                          <button
                            onClick={() => submitFeedback(message.id, false)}
                            className="text-gray-400 hover:text-red-600 transition-colors p-1 rounded hover:bg-red-50"
                            title="Not helpful"
                          >
                            👎
                          </button>

                          {/* Star Rating Button */}
                          <button
                            onClick={() => setShowRating(prev => ({...prev, [message.id]: !prev[message.id]}))}
                            className="text-xs text-gray-500 hover:text-blue-600 ml-2 px-2 py-1 rounded hover:bg-blue-50 transition-colors"
                          >
                            ⭐ Rate
                          </button>
                        </>
                      ) : (
                        <span className="text-xs text-green-600 flex items-center gap-1">
                          ✓ Thanks for your feedback!
                          {feedbackGiven[message.id].rating && (
                            <span className="ml-2">
                              {'⭐'.repeat(feedbackGiven[message.id].rating)}
                            </span>
                          )}
                        </span>
                      )}
                    </div>
                  )}

                  {/* Star Rating UI */}
                  {showRating[message.id] && !feedbackGiven[message.id] && (
                    <div className="ml-11 bg-blue-50 border border-blue-200 rounded-lg p-3 max-w-xs animate-fade-in">
                      <p className="text-sm text-gray-700 mb-2">How helpful was this response?</p>
                      <div className="flex gap-2 mb-3">
                        {[1, 2, 3, 4, 5].map(rating => (
                          <button
                            key={rating}
                            onClick={() => submitFeedback(message.id, true, rating)}
                            className="text-2xl hover:scale-110 transition-transform"
                            title={`${rating} star${rating > 1 ? 's' : ''}`}
                          >
                            ⭐
                          </button>
                        ))}
                      </div>
                      <button
                        onClick={() => setShowRating(prev => ({...prev, [message.id]: false}))}
                        className="text-xs text-gray-500 hover:text-gray-700"
                      >
                        Cancel
                      </button>
                    </div>
                  )}
                </div>
              )}
            </div>
          ))}

          {isLoading && (
            <div className="flex justify-start animate-fade-in">
              <div className="bg-white px-6 py-4 rounded-2xl shadow-md">
                <div className="flex items-center gap-3">
                  <span className="text-2xl">🌱</span>
                  <div className="flex flex-col">
                    <div className="flex items-center gap-1 mb-1">
                      <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce"></div>
                      <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                      <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                    </div>
                    <span className="text-xs text-gray-600">Neurobud is thinking...</span>
                  </div>
                </div>
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Input Area */}
      <div className="bg-white border-t px-4 sm:px-6 py-4">
        <div className="max-w-4xl mx-auto flex gap-2 sm:gap-3">
          <div className="flex-1">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Share what's on your mind..."
              className="w-full border border-gray-300 rounded-xl px-3 sm:px-4 py-2 sm:py-3 text-sm sm:text-base focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
              rows={2}
              disabled={isLoading}
              maxLength={2000}
            />
            <div className="text-xs text-gray-500 mt-1 text-right">
              {input.length}/2000
            </div>
          </div>
          <button
            onClick={sendMessage}
            disabled={isLoading || !input.trim()}
            className="bg-blue-600 text-white px-4 sm:px-8 py-2 sm:py-3 rounded-xl hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed font-semibold transition-colors text-sm sm:text-base"
          >
            Send
          </button>
        </div>
        <p className="text-xs text-gray-500 text-center mt-3">
          This is not therapy or medical advice. For professional help, consult a licensed therapist.
          <span className="block mt-1 text-gray-400">
            💡 Tip: Press Enter to send, Shift+Enter for new line, Esc to clear
          </span>
        </p>
      </div>
    </div>
  )
}

function UserProfile() {
  const { data: session, status } = useSession()
  const [showMenu, setShowMenu] = useState(false)

  if (status === 'loading') {
    return (
      <div className="w-8 h-8 bg-gray-200 rounded-full animate-pulse"></div>
    )
  }

  if (!session) {
    return (
      <Link
        href="/auth/signin"
        className="bg-blue-600 text-white px-4 py-2 rounded-lg font-semibold hover:bg-blue-700 transition-colors text-sm"
      >
        Sign In
      </Link>
    )
  }

  return (
    <div className="relative">
      <button
        onClick={() => setShowMenu(!showMenu)}
        className="flex items-center gap-2 hover:opacity-80 transition-opacity"
      >
        {session.user.image ? (
          <img
            src={session.user.image}
            alt={session.user.name}
            className="w-8 h-8 rounded-full border-2 border-blue-600"
          />
        ) : (
          <div className="w-8 h-8 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold">
            {session.user.name?.[0]?.toUpperCase() || 'U'}
          </div>
        )}
      </button>

      {/* Dropdown Menu */}
      {showMenu && (
        <div className="absolute right-0 mt-2 w-64 bg-white border border-gray-200 rounded-xl shadow-lg py-2 z-50">
          <div className="px-4 py-3 border-b border-gray-200">
            <p className="font-semibold text-gray-800">{session.user.name}</p>
            <p className="text-sm text-gray-600">{session.user.email}</p>
          </div>
          <button
            onClick={() => signOut({ callbackUrl: '/' })}
            className="w-full text-left px-4 py-2 text-red-600 hover:bg-red-50 transition-colors"
          >
            Sign Out
          </button>
        </div>
      )}
    </div>
  )
}