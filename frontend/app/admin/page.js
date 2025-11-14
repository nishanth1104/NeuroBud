'use client'

import { useState, useEffect } from 'react'
import axios from 'axios'
import Link from 'next/link'
import { useSession } from 'next-auth/react'
import { useRouter } from 'next/navigation'
import { BarChart, Bar, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

export default function AdminDashboard() {
  const { data: session, status } = useSession()
  const router = useRouter()
  const [stats, setStats] = useState(null)
  const [abStats, setAbStats] = useState(null)
  const [analytics, setAnalytics] = useState(null)
  const [loading, setLoading] = useState(true)
  const [lastUpdated, setLastUpdated] = useState(null)
  const [isAdmin, setIsAdmin] = useState(false)
  const [checking, setChecking] = useState(true)

  // Check if user is admin
  useEffect(() => {
    const checkAdmin = async () => {
      if (status === 'loading') return
      
      if (!session) {
        router.push('/auth/signin')
        return
      }

      try {
        const response = await axios.get(
          `${process.env.NEXT_PUBLIC_API_URL}/api/auth/check-admin?user_email=${session.user.email}`
        )
        
        if (response.data.is_admin) {
          setIsAdmin(true)
          setChecking(false)
        } else {
          // Not admin - redirect to home
          router.push('/')
        }
      } catch (error) {
        console.error('Error checking admin status:', error)
        router.push('/')
      }
    }

    checkAdmin()
  }, [session, status, router])

  // Fetch all stats
  const fetchStats = async () => {
    try {
      setLoading(true)
      
      // Fetch A/B testing stats
      const abResponse = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/api/ab-testing/stats`)
      setAbStats(abResponse.data)
      
      // Fetch general analytics
      const analyticsResponse = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/api/analytics`)
      setAnalytics(analyticsResponse.data)
      
      setLastUpdated(new Date())
    } catch (error) {
      console.error('Error fetching stats:', error)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    if (isAdmin) {
      fetchStats()
      
      // Auto-refresh every 30 seconds
      const interval = setInterval(fetchStats, 30000)
      return () => clearInterval(interval)
    }
  }, [isAdmin])

  // Prepare data for charts
  const getModelComparisonData = () => {
    if (!abStats?.stats) return []
    
    return Object.entries(abStats.stats).map(([variant, data]) => ({
      model: variant === 'base' ? 'Base Model' : 'Fine-tuned',
      responses: data.total_responses,
      avgRating: data.avg_user_rating || 0,
      helpfulRatio: data.helpfulness_ratio || 0,
      avgTime: data.avg_response_time_ms,
    }))
  }

  const getFeedbackData = () => {
    if (!abStats?.stats) return []
    
    return Object.entries(abStats.stats).map(([variant, data]) => ({
      name: variant === 'base' ? 'Base' : 'Fine-tuned',
      helpful: data.helpful_count,
      notHelpful: data.not_helpful_count,
    }))
  }

  const getHelpfulnessPieData = () => {
    if (!abStats?.stats?.base) return []
    
    const base = abStats.stats.base
    return [
      { name: 'Helpful', value: base.helpful_count || 0, color: '#10b981' },
      { name: 'Not Helpful', value: base.not_helpful_count || 0, color: '#ef4444' },
    ]
  }

  const COLORS = ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b']

  // Show loading while checking auth
  if (checking || status === 'loading') {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="text-6xl mb-4 animate-spin">🔒</div>
          <p className="text-gray-600 text-lg">Checking admin access...</p>
        </div>
      </div>
    )
  }

  // Don't show anything if not admin (will redirect)
  if (!isAdmin) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="text-6xl mb-4">🚫</div>
          <p className="text-gray-600 text-lg">Access denied. Redirecting...</p>
        </div>
      </div>
    )
  }

  // Show loading while fetching data
  if (loading && !abStats) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="text-6xl mb-4 animate-spin">⚙️</div>
          <p className="text-gray-600 text-lg">Loading dashboard...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <nav className="bg-white border-b shadow-sm">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <Link href="/" className="text-2xl font-bold text-blue-600">
              🌱 Neurobud
            </Link>
            <span className="text-gray-400">|</span>
            <h1 className="text-xl font-semibold text-gray-800">Admin Dashboard</h1>
            <span className="bg-red-100 text-red-800 text-xs px-2 py-1 rounded font-semibold">
              ADMIN ONLY
            </span>
          </div>
          <div className="flex items-center gap-4">
            <Link href="/chat" className="text-gray-600 hover:text-blue-600 font-medium">
              Chat
            </Link>
            <Link href="/mood" className="text-gray-600 hover:text-blue-600 font-medium">
              Mood
            </Link>
            <div className="flex items-center gap-2">
              {session?.user?.image ? (
                <img
                  src={session.user.image}
                  alt={session.user.name}
                  className="w-8 h-8 rounded-full"
                />
              ) : (
                <div className="w-8 h-8 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-sm">
                  {session?.user?.name?.[0]?.toUpperCase() || 'A'}
                </div>
              )}
              <span className="text-sm text-gray-600">{session?.user?.name}</span>
            </div>
          </div>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto px-6 py-8">
        {/* Header Section */}
        <div className="mb-8">
          <h2 className="text-3xl font-bold text-gray-800 mb-2">Analytics Dashboard</h2>
          <div className="flex items-center gap-4 text-sm text-gray-600">
            <span>Last updated: {lastUpdated?.toLocaleTimeString()}</span>
            <button
              onClick={fetchStats}
              className="text-blue-600 hover:text-blue-700 font-medium"
            >
              🔄 Refresh
            </button>
          </div>
        </div>

        {/* Key Metrics */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
            <div className="text-sm text-gray-600 mb-1">Total Conversations</div>
            <div className="text-3xl font-bold text-gray-800">
              {analytics?.total_conversations || 0}
            </div>
            <div className="text-xs text-gray-500 mt-2">
              {analytics?.conversations_last_24h || 0} in last 24h
            </div>
          </div>

          <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
            <div className="text-sm text-gray-600 mb-1">Total Messages</div>
            <div className="text-3xl font-bold text-gray-800">
              {analytics?.total_messages || 0}
            </div>
            <div className="text-xs text-gray-500 mt-2">
              Avg {analytics?.total_messages && analytics?.total_conversations 
                ? Math.round(analytics.total_messages / analytics.total_conversations) 
                : 0} per conversation
            </div>
          </div>

          <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
            <div className="text-sm text-gray-600 mb-1">Crisis Events</div>
            <div className="text-3xl font-bold text-red-600">
              {analytics?.total_crisis_events || 0}
            </div>
            <div className="text-xs text-gray-500 mt-2">
              Detected and handled
            </div>
          </div>

          <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
            <div className="text-sm text-gray-600 mb-1">Avg Mood (7d)</div>
            <div className="text-3xl font-bold text-green-600">
              {analytics?.avg_mood_last_7d || 0}/10
            </div>
            <div className="text-xs text-gray-500 mt-2">
              {analytics?.total_mood_entries || 0} total entries
            </div>
          </div>
        </div>

        {/* A/B Testing Status */}
        <div className="bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl p-6 mb-8 border border-blue-200">
          <h3 className="text-lg font-semibold text-gray-800 mb-4">A/B Testing Status</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div>
              <div className="text-sm text-gray-600">Status</div>
              <div className="text-lg font-semibold text-gray-800">
                {abStats?.ab_testing_enabled ? '✅ Enabled' : '❌ Disabled'}
              </div>
            </div>
            <div>
              <div className="text-sm text-gray-600">Split Ratio</div>
              <div className="text-lg font-semibold text-gray-800">
                {abStats?.split_ratio ? `${abStats.split_ratio * 100}% / ${(1 - abStats.split_ratio) * 100}%` : 'N/A'}
              </div>
            </div>
            <div>
              <div className="text-sm text-gray-600">Fine-tuned Model</div>
              <div className="text-lg font-semibold text-gray-800">
                {abStats?.fine_tuned_model_available ? '✅ Available' : '❌ Not Available'}
              </div>
            </div>
          </div>
        </div>

        {/* Charts Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
          {/* Model Comparison - Response Count */}
          <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
            <h3 className="text-lg font-semibold text-gray-800 mb-4">Model Response Count</h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={getModelComparisonData()}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="model" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="responses" fill="#3b82f6" name="Total Responses" />
              </BarChart>
            </ResponsiveContainer>
          </div>

          {/* Average Rating */}
          <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
            <h3 className="text-lg font-semibold text-gray-800 mb-4">Average User Rating</h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={getModelComparisonData()}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="model" />
                <YAxis domain={[0, 5]} />
                <Tooltip />
                <Legend />
                <Bar dataKey="avgRating" fill="#10b981" name="Avg Rating (out of 5)" />
              </BarChart>
            </ResponsiveContainer>
          </div>

          {/* Helpfulness Feedback */}
          <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
            <h3 className="text-lg font-semibold text-gray-800 mb-4">Helpfulness Distribution</h3>
            <ResponsiveContainer width="100%" height={300}>
              <PieChart>
                <Pie
                  data={getHelpfulnessPieData()}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={({ name, value }) => `${name}: ${value}`}
                  outerRadius={100}
                  fill="#8884d8"
                  dataKey="value"
                >
                  {getHelpfulnessPieData().map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>

          {/* Response Time */}
          <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
            <h3 className="text-lg font-semibold text-gray-800 mb-4">Avg Response Time</h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={getModelComparisonData()}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="model" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="avgTime" fill="#f59e0b" name="Response Time (ms)" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Detailed Stats Table */}
        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <h3 className="text-lg font-semibold text-gray-800 mb-4">Detailed Model Comparison</h3>
          <div className="overflow-x-auto">
            <table className="w-full text-left">
              <thead className="border-b border-gray-200">
                <tr>
                  <th className="pb-3 font-semibold text-gray-700">Model</th>
                  <th className="pb-3 font-semibold text-gray-700">Responses</th>
                  <th className="pb-3 font-semibold text-gray-700">Avg Rating</th>
                  <th className="pb-3 font-semibold text-gray-700">Helpful</th>
                  <th className="pb-3 font-semibold text-gray-700">Not Helpful</th>
                  <th className="pb-3 font-semibold text-gray-700">Ratio</th>
                  <th className="pb-3 font-semibold text-gray-700">Avg Time</th>
                </tr>
              </thead>
              <tbody>
                {Object.entries(abStats?.stats || {}).map(([variant, data]) => (
                  <tr key={variant} className="border-b border-gray-100">
                    <td className="py-3 font-medium">{variant === 'base' ? 'Base Model' : 'Fine-tuned'}</td>
                    <td className="py-3">{data.total_responses}</td>
                    <td className="py-3">
                      {data.avg_user_rating ? (
                        <span className="text-yellow-600">
                          {'⭐'.repeat(Math.round(data.avg_user_rating))} ({data.avg_user_rating.toFixed(2)})
                        </span>
                      ) : (
                        <span className="text-gray-400">No ratings</span>
                      )}
                    </td>
                    <td className="py-3 text-green-600">{data.helpful_count}</td>
                    <td className="py-3 text-red-600">{data.not_helpful_count}</td>
                    <td className="py-3">
                      {data.helpfulness_ratio ? (
                        <span className={data.helpfulness_ratio > 0.7 ? 'text-green-600' : 'text-yellow-600'}>
                          {(data.helpfulness_ratio * 100).toFixed(0)}%
                        </span>
                      ) : (
                        <span className="text-gray-400">N/A</span>
                      )}
                    </td>
                    <td className="py-3">{data.avg_response_time_ms.toFixed(0)} ms</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Footer Info */}
        <div className="mt-8 text-center text-sm text-gray-500">
          <p>Dashboard auto-refreshes every 30 seconds</p>
          <p className="mt-2">
            System Version: {analytics?.version} | Uptime: {analytics?.uptime}
          </p>
        </div>
      </div>
    </div>
  )
}