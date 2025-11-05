'use client'

import { useState, useRef, useEffect } from 'react'
import axios from 'axios'
import Link from 'next/link'

export default function ChatPage() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [conversationId, setConversationId] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef(null)

  // Auto-scroll to bottom
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const sendMessage = async () => {
    if (!input.trim() || isLoading) return

    const userMessage = input.trim()
    setInput('')
    setIsLoading(true)

    // Add user message to UI
    setMessages(prev => [...prev, { role: 'user', content: userMessage }])

    try {
      // Call API
      const response = await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/api/chat`, {
        message: userMessage,
        conversation_id: conversationId
      })

      // Update conversation ID
      if (!conversationId) {
        setConversationId(response.data.conversation_id)
      }

      // Add assistant message to UI
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: response.data.response,
        is_crisis: response.data.is_crisis,
        crisis_severity: response.data.crisis_severity
      }])

    } catch (error) {
      console.error('Error sending message:', error)
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: 'Sorry, I had trouble connecting. Please try again.',
        error: true
      }])
    } finally {
      setIsLoading(false)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
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
          <div className="flex gap-4">
            <Link href="/chat" className="text-blue-600 font-semibold border-b-2 border-blue-600">
              Chat
            </Link>
            <Link href="/mood" className="text-gray-600 hover:text-blue-600 font-medium">
              Mood
            </Link>
            <Link href="/resources" className="text-gray-600 hover:text-blue-600 font-medium">
              Resources
            </Link>
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

      {/* Chat Messages */}
      <div className="flex-1 overflow-y-auto px-6 py-8">
        <div className="max-w-4xl mx-auto space-y-6">
          {messages.length === 0 && (
            <div className="text-center text-gray-500 mt-20">
              <div className="text-6xl mb-4">💬</div>
              <p className="text-xl">Start a conversation...</p>
              <p className="text-sm mt-2">Share what's on your mind. I'm here to listen.</p>
            </div>
          )}

          {messages.map((message, index) => (
            <div
              key={index}
              className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              <div
                className={`max-w-3xl px-6 py-4 rounded-2xl ${
                  message.role === 'user'
                    ? 'bg-blue-600 text-white'
                    : message.is_crisis
                    ? 'bg-red-50 border-2 border-red-300 text-gray-800'
                    : 'bg-white text-gray-800 shadow-md'
                }`}
              >
                {message.role === 'assistant' && (
                  <div className="flex items-center gap-2 mb-2">
                    <span className="text-2xl">🌱</span>
                    <span className="font-semibold text-sm">Neurobud</span>
                    {message.is_crisis && (
                      <span className="text-red-600 font-bold text-xs">🆘 CRISIS ALERT</span>
                    )}
                  </div>
                )}
                <div className="whitespace-pre-wrap">{message.content}</div>
              </div>
            </div>
          ))}

          {isLoading && (
            <div className="flex justify-start">
              <div className="bg-white px-6 py-4 rounded-2xl shadow-md">
                <div className="flex items-center gap-2">
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.4s'}}></div>
                </div>
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Input Area */}
      <div className="bg-white border-t px-6 py-4">
        <div className="max-w-4xl mx-auto flex gap-3">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Share what's on your mind..."
            className="flex-1 border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
            rows={2}
            disabled={isLoading}
          />
          <button
            onClick={sendMessage}
            disabled={isLoading || !input.trim()}
            className="bg-blue-600 text-white px-8 py-3 rounded-xl hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed font-semibold transition-colors"
          >
            Send
          </button>
        </div>
        <p className="text-xs text-gray-500 text-center mt-3">
          This is not therapy or medical advice. For professional help, consult a licensed therapist.
        </p>
      </div>
    </div>
  )
}