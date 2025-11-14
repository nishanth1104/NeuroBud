'use client'

import { useAdmin } from './hooks/useAdmin'
import { useSession } from 'next-auth/react'
import Link from 'next/link'

export default function Home() {
  const { isAdmin } = useAdmin()
  const { data: session } = useSession()
  
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50">
      {/* Header Navigation */}
      <nav className="bg-white/80 backdrop-blur-sm border-b border-gray-200">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <Link href="/" className="text-2xl font-bold text-blue-600 flex items-center gap-2">
            🌱 Neurobud
          </Link>
          <div className="flex items-center gap-4">
            <Link href="/chat" className="text-gray-600 hover:text-blue-600 font-medium">
              Chat
            </Link>
            <Link href="/mood" className="text-gray-600 hover:text-blue-600 font-medium">
              Mood
            </Link>
            <Link href="/resources" className="text-gray-600 hover:text-blue-600 font-medium">
              Resources
            </Link>
            
            {/* Admin Link - Only for admins */}
            {isAdmin && (
              <Link href="/admin" className="text-purple-600 hover:text-purple-700 font-semibold flex items-center gap-1">
                ⚙️ Admin
              </Link>
            )}
            
            {/* Sign In / User Profile */}
            {session ? (
              <div className="flex items-center gap-2">
                {session.user.image ? (
                  <img
                    src={session.user.image}
                    alt={session.user.name}
                    className="w-8 h-8 rounded-full border-2 border-blue-600"
                  />
                ) : (
                  <div className="w-8 h-8 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-sm">
                    {session.user.name?.[0]?.toUpperCase() || 'U'}
                  </div>
                )}
              </div>
            ) : (
              <Link
                href="/auth/signin"
                className="bg-blue-600 text-white px-4 py-2 rounded-lg font-semibold hover:bg-blue-700 transition-colors text-sm"
              >
                Sign In
              </Link>
            )}
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <div className="flex items-center justify-center p-6" style={{ minHeight: 'calc(100vh - 80px)' }}>
        <div className="max-w-2xl text-center">
          <div className="text-7xl mb-6 animate-bounce">🌱</div>
          
          <h1 className="text-6xl font-bold text-gray-800 mb-4">
            Neurobud
          </h1>
          
          <p className="text-2xl text-gray-600 mb-8">
            A Safe Space to Process Your Feelings
          </p>
          
          <p className="text-lg text-gray-600 mb-12 max-w-xl mx-auto">
            Talk to an AI companion that listens without judgment, teaches coping strategies, 
            and helps you understand your emotions.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link 
              href="/chat"
              className="bg-blue-600 text-white px-8 py-4 rounded-xl font-semibold text-lg hover:bg-blue-700 transition-all hover:scale-105 shadow-lg"
            >
              Start Chatting →
            </Link>
            {!session && (
              <Link 
                href="/auth/signin"
                className="bg-white text-blue-600 border-2 border-blue-600 px-8 py-4 rounded-xl font-semibold text-lg hover:bg-blue-50 transition-all hover:scale-105"
              >
                Sign In
              </Link>
            )}
            {session && (
              <Link 
                href="/mood"
                className="bg-white text-purple-600 border-2 border-purple-600 px-8 py-4 rounded-xl font-semibold text-lg hover:bg-purple-50 transition-all hover:scale-105"
              >
                Track Your Mood
              </Link>
            )}
          </div>

          {/* Features */}
          <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-white/80 backdrop-blur-sm rounded-xl p-6 border border-gray-200 hover:shadow-lg transition-shadow">
              <div className="text-4xl mb-3">💬</div>
              <h3 className="font-semibold text-gray-800 mb-2">Empathetic Chat</h3>
              <p className="text-sm text-gray-600">AI-powered conversations that understand and support you</p>
            </div>
            
            <div className="bg-white/80 backdrop-blur-sm rounded-xl p-6 border border-gray-200 hover:shadow-lg transition-shadow">
              <div className="text-4xl mb-3">📊</div>
              <h3 className="font-semibold text-gray-800 mb-2">Mood Tracking</h3>
              <p className="text-sm text-gray-600">Monitor your emotional wellbeing over time</p>
            </div>
            
            <div className="bg-white/80 backdrop-blur-sm rounded-xl p-6 border border-gray-200 hover:shadow-lg transition-shadow">
              <div className="text-4xl mb-3">🆘</div>
              <h3 className="font-semibold text-gray-800 mb-2">Crisis Detection</h3>
              <p className="text-sm text-gray-600">Immediate resources when you need them most</p>
            </div>
          </div>

          {/* Disclaimer */}
          <div className="mt-12 bg-yellow-50 border border-yellow-200 rounded-xl p-4">
            <p className="text-sm text-yellow-800">
              <strong>⚠️ Important:</strong> Neurobud is not a replacement for professional mental health care. 
              If you're in crisis, please call <strong>988</strong> (Suicide & Crisis Lifeline).
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}