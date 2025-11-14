'use client'

import { useState, useEffect } from 'react'
import axios from 'axios'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import { useSession, signOut } from 'next-auth/react'
import { useAdmin } from '../hooks/useAdmin'

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

export default function MoodPage() {
  const router = useRouter()
  const { data: session, status } = useSession()
  const { isAdmin } = useAdmin() 
  const [moodScore, setMoodScore] = useState(5)
  const [note, setNote] = useState('')
  const [history, setHistory] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const [historyLoading, setHistoryLoading] = useState(true)
  const [justLogged, setJustLogged] = useState(false)
  const [error, setError] = useState(null)

  // Redirect to sign in if not authenticated
  useEffect(() => {
    if (status === 'unauthenticated') {
      router.push('/auth/signin')
    }
  }, [status, router])

  // Load mood history on page load
  useEffect(() => {
    if (session) {
      loadMoodHistory()
    }
  }, [session])

  // Show loading while checking authentication
  if (status === 'loading') {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="text-6xl mb-4">🌱</div>
          <p className="text-xl text-gray-600">Loading...</p>
        </div>
      </div>
    )
  }

  // Don't render anything if not authenticated (redirecting)
  if (!session) {
    return null
  }

  const loadMoodHistory = async () => {
    if (!session?.user?.email) return

    setHistoryLoading(true)
    try {
      const response = await axios.get(
        `${process.env.NEXT_PUBLIC_API_URL}/api/mood/history?days=7&user_email=${encodeURIComponent(session.user.email)}`
      )
      setHistory(response.data.entries)
    } catch (error) {
      console.error('Error loading mood history:', error)
    } finally {
      setHistoryLoading(false)
    }
  }

  const logMood = async () => {
    if (!session?.user?.email) {
      setError('You must be logged in to log mood.')
      return
    }

    setIsLoading(true)
    setError(null)

    try {
      await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/api/mood`, {
        mood_score: moodScore,
        note: note.trim() || null,
        user_email: session.user.email
      })

      setJustLogged(true)
      setNote('')
      setTimeout(() => setJustLogged(false), 3000)

      loadMoodHistory()
    } catch (error) {
      console.error('Error logging mood:', error)

      let errorMessage = 'Failed to log mood. Please try again.'

      if (error.response?.status === 429) {
        errorMessage = 'Too many requests. Please wait a moment.'
      } else if (error.response?.status === 400) {
        errorMessage = error.response.data?.detail || errorMessage
      }

      setError(errorMessage)
    } finally {
      setIsLoading(false)
    }
  }

  const getMoodEmoji = (score) => {
    if (score <= 2) return '😢'
    if (score <= 4) return '😔'
    if (score <= 6) return '😐'
    if (score <= 8) return '🙂'
    return '😄'
  }

  const getMoodLabel = (score) => {
    if (score <= 2) return 'Very Low'
    if (score <= 4) return 'Low'
    if (score <= 6) return 'Neutral'
    if (score <= 8) return 'Good'
    return 'Great'
  }

  const getMoodColor = (score) => {
    if (score <= 2) return 'bg-red-100 border-red-300'
    if (score <= 4) return 'bg-orange-100 border-orange-300'
    if (score <= 6) return 'bg-yellow-100 border-yellow-300'
    if (score <= 8) return 'bg-green-100 border-green-300'
    return 'bg-blue-100 border-blue-300'
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
        <nav className="bg-white border-b shadow-sm">
          <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
            <Link href="/" className="text-2xl font-bold text-blue-600 flex items-center gap-2">
              🌱 Neurobud
            </Link>
            <div className="flex items-center gap-4">
              <Link href="/chat" className="text-gray-600 hover:text-blue-600 font-medium">
                Chat
              </Link>
              <Link href="/mood" className="text-blue-600 font-semibold border-b-2 border-blue-600">
                Mood
              </Link>
              <Link href="/resources" className="text-gray-600 hover:text-blue-600 font-medium">
                Resources
              </Link>

              {/* Admin Link */}
              {isAdmin && (
                <Link href="/admin" className="text-purple-600 hover:text-purple-700 font-medium flex items-center gap-1">
                  ⚙️ Admin
                </Link>
              )}

              <UserProfile />
            </div>
          </div>
        </nav>

      {/* Sign Out Button */}
      

      {/* Main Content */}
      <div className="max-w-4xl mx-auto px-6 py-12">
        {/* Page Title */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-800 mb-3">Track Your Mood</h1>
          <p className="text-lg text-gray-600">How are you feeling today?</p>
        </div>

        {/* Mood Logger Card */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-8">
          {/* Error Message */}
          {error && (
            <div className="mb-6 bg-red-50 border-2 border-red-300 rounded-xl px-4 py-3 animate-fade-in">
              <p className="text-red-800 font-semibold text-center flex items-center justify-center gap-2">
                <span className="text-2xl">❌</span>
                {error}
              </p>
            </div>
          )}

          {/* Success Message */}
          {justLogged && !error && (
            <div className="mb-6 bg-green-50 border-2 border-green-300 rounded-xl px-4 py-3 animate-fade-in">
              <p className="text-green-800 font-semibold text-center flex items-center justify-center gap-2">
                <span className="text-2xl">✅</span>
                Mood logged successfully! Keep tracking to see patterns.
              </p>
            </div>
          )}

          {/* Mood Emoji Display */}
          <div className="text-center mb-8">
            <div className="text-8xl mb-4">{getMoodEmoji(moodScore)}</div>
            <div className="text-3xl font-bold text-gray-800">{getMoodLabel(moodScore)}</div>
            <div className="text-xl text-gray-600 mt-2">{moodScore}/10</div>
          </div>

          {/* Mood Slider */}
          <div className="mb-8">
            <label className="block text-sm font-semibold text-gray-700 mb-3">
              Rate your mood (1 = Very Low, 10 = Excellent)
            </label>
            <input
              type="range"
              min="1"
              max="10"
              value={moodScore}
              onChange={(e) => setMoodScore(parseInt(e.target.value))}
              className="w-full h-3 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-blue-600"
            />
            <div className="flex justify-between text-xs text-gray-500 mt-2">
              <span>1</span>
              <span>2</span>
              <span>3</span>
              <span>4</span>
              <span>5</span>
              <span>6</span>
              <span>7</span>
              <span>8</span>
              <span>9</span>
              <span>10</span>
            </div>
          </div>

          {/* Optional Note */}
          <div className="mb-6">
            <label className="block text-sm font-semibold text-gray-700 mb-2">
              What's affecting your mood today? (optional)
            </label>
            <textarea
              value={note}
              onChange={(e) => setNote(e.target.value)}
              placeholder="e.g., Had a good workout, stressed about deadline, feeling lonely..."
              className="w-full border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
              rows={3}
              maxLength={500}
            />
            <div className="text-xs text-gray-500 mt-1 text-right">
              {note.length}/500
            </div>
          </div>

          {/* Log Button */}
          <button
            onClick={logMood}
            disabled={isLoading}
            className="w-full bg-blue-600 text-white py-4 rounded-xl font-semibold text-lg hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors"
          >
            {isLoading ? 'Logging...' : 'Log Mood'}
          </button>
        </div>

        {/* Mood History */}
        <div className="bg-white rounded-2xl shadow-lg p-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-6">Recent Mood History (7 Days)</h2>
          
          {historyLoading ? (
            // Loading skeleton
            <div className="space-y-4">
              {[1, 2, 3].map((i) => (
                <div key={i} className="border-2 border-gray-200 rounded-xl p-4 animate-pulse">
                  <div className="flex items-center gap-3">
                    <div className="w-12 h-12 bg-gray-200 rounded-full"></div>
                    <div className="flex-1">
                      <div className="h-4 bg-gray-200 rounded w-32 mb-2"></div>
                      <div className="h-3 bg-gray-200 rounded w-48"></div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          ) : history.length === 0 ? (
            <div className="text-center py-12 text-gray-500">
              <div className="text-5xl mb-4">📊</div>
              <p className="text-lg">No mood entries yet.</p>
              <p className="text-sm mt-2">Start tracking your mood to see trends!</p>
            </div>
          ) : (
            <div className="space-y-4">
              {history.map((entry) => (
                <div
                  key={entry.id}
                  className={`border-2 rounded-xl p-4 ${getMoodColor(entry.mood_score)}`}
                >
                  <div className="flex items-center justify-between mb-2">
                    <div className="flex items-center gap-3">
                      <span className="text-3xl">{getMoodEmoji(entry.mood_score)}</span>
                      <div>
                        <div className="font-bold text-gray-800">
                          {getMoodLabel(entry.mood_score)} ({entry.mood_score}/10)
                        </div>
                        <div className="text-sm text-gray-600">
                          {new Date(entry.created_at).toLocaleDateString('en-US', {
                            weekday: 'short',
                            month: 'short',
                            day: 'numeric',
                            hour: 'numeric',
                            minute: '2-digit'
                          })}
                        </div>
                      </div>
                    </div>
                  </div>
                  {entry.note && (
                    <div className="text-sm text-gray-700 mt-2 pl-12">
                      "{entry.note}"
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Helpful Tip */}
        <div className="mt-8 bg-blue-50 border border-blue-200 rounded-xl p-6">
          <h3 className="font-semibold text-blue-900 mb-2">💡 Tip: Track Daily for Insights</h3>
          <p className="text-sm text-blue-800">
            Tracking your mood regularly helps you notice patterns. You might discover that exercise, 
            sleep, or social connection affect your mood more than you realized!
          </p>
        </div>
      </div>
    </div>
  )
}