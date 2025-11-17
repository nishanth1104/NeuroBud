'use client'

import { useState, useEffect } from 'react'
import axios from 'axios'
import Link from 'next/link'
import { useSession } from 'next-auth/react'
import { useRouter } from 'next/navigation'
import { BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

export default function AdminDashboard() {
  const { data: session, status } = useSession()
  const router = useRouter()
  const [activeTab, setActiveTab] = useState('analytics') // 'analytics', 'cost', or 'users'
  const [stats, setStats] = useState(null)
  const [abStats, setAbStats] = useState(null)
  const [analytics, setAnalytics] = useState(null)
  const [costData, setCostData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [lastUpdated, setLastUpdated] = useState(null)
  const [isAdmin, setIsAdmin] = useState(false)
  const [checking, setChecking] = useState(true)

  // User management state
  const [users, setUsers] = useState([])
  const [usersLoading, setUsersLoading] = useState(false)
  const [actionLoading, setActionLoading] = useState(null) // Track which user action is loading

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
      
      const abResponse = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/api/ab-testing/stats`)
      setAbStats(abResponse.data)
      
      const analyticsResponse = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/api/analytics`)
      setAnalytics(analyticsResponse.data)
      
      const costResponse = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/api/admin/cost-analytics?days=7`)
      setCostData(costResponse.data)
      
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
      const interval = setInterval(fetchStats, 30000)
      return () => clearInterval(interval)
    }
  }, [isAdmin])

  // Fetch all users
  const fetchUsers = async () => {
    try {
      setUsersLoading(true)
      const response = await axios.get(
        `${process.env.NEXT_PUBLIC_API_URL}/api/admin/users?current_user_email=${session.user.email}`
      )
      setUsers(response.data.users || [])
    } catch (error) {
      console.error('Error fetching users:', error)
      alert('Failed to fetch users')
    } finally {
      setUsersLoading(false)
    }
  }

  // Toggle admin status
  const toggleAdmin = async (userId, currentStatus) => {
    if (!confirm(`Are you sure you want to ${currentStatus ? 'remove admin from' : 'make admin'} this user?`)) {
      return
    }

    try {
      setActionLoading(`admin-${userId}`)
      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_API_URL}/api/admin/users/${userId}/toggle-admin?current_user_email=${session.user.email}`
      )
      alert(response.data.message)
      fetchUsers() // Refresh the list
    } catch (error) {
      console.error('Error toggling admin:', error)
      alert(error.response?.data?.detail || 'Failed to update admin status')
    } finally {
      setActionLoading(null)
    }
  }

  // Toggle active status
  const toggleActive = async (userId, currentStatus) => {
    if (!confirm(`Are you sure you want to ${currentStatus ? 'block' : 'unblock'} this user?`)) {
      return
    }

    try {
      setActionLoading(`active-${userId}`)
      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_API_URL}/api/admin/users/${userId}/toggle-active?current_user_email=${session.user.email}`
      )
      alert(response.data.message)
      fetchUsers() // Refresh the list
    } catch (error) {
      console.error('Error toggling active status:', error)
      alert(error.response?.data?.detail || 'Failed to update active status')
    } finally {
      setActionLoading(null)
    }
  }

  // Delete user
  const deleteUser = async (userId, userEmail) => {
    if (!confirm(`⚠️ DANGER: Are you sure you want to PERMANENTLY DELETE ${userEmail}?\n\nThis action CANNOT be undone!`)) {
      return
    }

    // Double confirmation for safety
    const confirmText = prompt(`Type "DELETE" to confirm permanent deletion of ${userEmail}:`)
    if (confirmText !== 'DELETE') {
      alert('Deletion cancelled.')
      return
    }

    try {
      setActionLoading(`delete-${userId}`)
      const response = await axios.delete(
        `${process.env.NEXT_PUBLIC_API_URL}/api/admin/users/${userId}?current_user_email=${session.user.email}`
      )
      alert(response.data.message)
      fetchUsers() // Refresh the list
    } catch (error) {
      console.error('Error deleting user:', error)
      alert(error.response?.data?.detail || 'Failed to delete user')
    } finally {
      setActionLoading(null)
    }
  }

  // Load users when switching to users tab
  useEffect(() => {
    if (isAdmin && activeTab === 'users') {
      fetchUsers()
    }
  }, [isAdmin, activeTab])

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

  const getHelpfulnessPieData = () => {
    if (!abStats?.stats?.base) return []
    
    const base = abStats.stats.base
    return [
      { name: 'Helpful', value: base.helpful_count || 0, color: '#10b981' },
      { name: 'Not Helpful', value: base.not_helpful_count || 0, color: '#ef4444' },
    ]
  }

  const getCostBreakdownData = () => {
    if (!costData?.by_feature) return []
    
    return costData.by_feature.map(item => ({
      name: item.feature.charAt(0).toUpperCase() + item.feature.slice(1),
      cost: item.cost,
      requests: item.requests
    }))
  }

  const getDailyCostData = () => {
    if (!costData?.daily_breakdown) return []
    
    return costData.daily_breakdown.map(item => ({
      date: new Date(item.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
      cost: item.cost,
      requests: item.requests
    }))
  }

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
              <img 
                src="/neurobud-logo.png" 
                alt="Neurobud Logo" 
                className="w-12 h-12 mx-auto mb-0"
              /> Neurobud
            </Link>
            <span className="text-gray-400">|</span>
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
        {/* Header Section with Tabs */}
        <div className="mb-8">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-3xl font-bold text-gray-800">Admin Dashboard</h2>
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

          {/* Tab Navigation */}
          <div className="flex gap-2 border-b border-gray-200">
            <button
              onClick={() => setActiveTab('analytics')}
              className={`px-6 py-3 font-semibold transition-all ${
                activeTab === 'analytics'
                  ? 'text-blue-600 border-b-2 border-blue-600'
                  : 'text-gray-600 hover:text-gray-800'
              }`}
            >
              📈 Analytics Dashboard
            </button>
            <button
              onClick={() => setActiveTab('cost')}
              className={`px-6 py-3 font-semibold transition-all ${
                activeTab === 'cost'
                  ? 'text-blue-600 border-b-2 border-blue-600'
                  : 'text-gray-600 hover:text-gray-800'
              }`}
            >
              💰 Cost Dashboard
            </button>
            <button
              onClick={() => setActiveTab('users')}
              className={`px-6 py-3 font-semibold transition-all ${
                activeTab === 'users'
                  ? 'text-blue-600 border-b-2 border-blue-600'
                  : 'text-gray-600 hover:text-gray-800'
              }`}
            >
              👥 User Management
            </button>
          </div>
        </div>

        {/* Analytics Dashboard */}
        {activeTab === 'analytics' && (
          <>
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
          </>
        )}

        {/* Cost Dashboard */}
        {activeTab === 'cost' && costData && (
          <>
            {/* Budget Summary */}
            <div className="bg-gradient-to-r from-green-50 to-blue-50 rounded-xl p-6 mb-8 border border-green-200">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-lg font-semibold text-gray-800">💰 Budget Status</h3>
                {costData.summary.alert_triggered && (
                  <span className="bg-red-100 text-red-800 text-xs px-3 py-1 rounded-full font-semibold">
                    ⚠️ Alert Triggered
                  </span>
                )}
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div>
                  <div className="text-sm text-gray-600">Total Budget</div>
                  <div className="text-2xl font-bold text-gray-800">
                    ${costData.summary.total_budget.toFixed(2)}
                  </div>
                </div>
                
                <div>
                  <div className="text-sm text-gray-600">Spent</div>
                  <div className="text-2xl font-bold text-blue-600">
                    ${costData.summary.all_time_spend.toFixed(4)}
                  </div>
                  <div className="text-xs text-gray-500 mt-1">
                    {costData.summary.budget_used_percent.toFixed(2)}% used
                  </div>
                </div>
                
                <div>
                  <div className="text-sm text-gray-600">Remaining</div>
                  <div className="text-2xl font-bold text-green-600">
                    ${costData.summary.budget_remaining.toFixed(2)}
                  </div>
                </div>
                
                <div>
                  <div className="text-sm text-gray-600">Today's Spend</div>
                  <div className="text-2xl font-bold text-purple-600">
                    ${costData.summary.today_spend.toFixed(4)}
                  </div>
                  <div className="text-xs text-gray-500 mt-1">
                    ${costData.summary.daily_budget_limit} daily limit
                  </div>
                </div>
              </div>
              
              {/* Progress Bar */}
              <div className="mt-4">
                <div className="flex justify-between text-xs text-gray-600 mb-1">
                  <span>Budget Progress</span>
                  <span>{costData.summary.budget_used_percent.toFixed(2)}%</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-3">
                  <div 
                    className={`h-3 rounded-full transition-all ${
                      costData.summary.budget_used_percent >= 90 ? 'bg-red-600' :
                      costData.summary.budget_used_percent >= 75 ? 'bg-yellow-600' :
                      'bg-green-600'
                    }`}
                    style={{ width: `${Math.min(costData.summary.budget_used_percent, 100)}%` }}
                  />
                </div>
              </div>
            </div>

            {/* Cost Metrics Cards */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
              <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                <div className="text-sm text-gray-600 mb-1">Avg Cost per Request</div>
                <div className="text-3xl font-bold text-gray-800">
                  ${costData.summary.avg_cost_per_request.toFixed(6)}
                </div>
                <div className="text-xs text-gray-500 mt-2">
                  Per API call
                </div>
              </div>

              <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                <div className="text-sm text-gray-600 mb-1">Period Spend</div>
                <div className="text-3xl font-bold text-gray-800">
                  ${costData.summary.period_spend.toFixed(4)}
                </div>
                <div className="text-xs text-gray-500 mt-2">
                  Last {costData.period_days} days
                </div>
              </div>

              <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                <div className="text-sm text-gray-600 mb-1">Cost per 1K Tokens</div>
                <div className="text-3xl font-bold text-gray-800">
                  ${costData.by_model[0]?.cost_per_1k_tokens.toFixed(4) || '0.0000'}
                </div>
                <div className="text-xs text-gray-500 mt-2">
                  {costData.by_model[0]?.model || 'N/A'}
                </div>
              </div>
            </div>

            {/* Cost Charts */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
              {/* Daily Cost Trend */}
              <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                <h3 className="text-lg font-semibold text-gray-800 mb-4">Daily Cost Trend</h3>
                <ResponsiveContainer width="100%" height={300}>
                  <LineChart data={getDailyCostData()}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="date" />
                    <YAxis />
                    <Tooltip formatter={(value) => `$${value.toFixed(4)}`} />
                    <Legend />
                    <Line type="monotone" dataKey="cost" stroke="#3b82f6" name="Cost ($)" />
                  </LineChart>
                </ResponsiveContainer>
              </div>

              {/* Cost by Feature */}
              <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                <h3 className="text-lg font-semibold text-gray-800 mb-4">Cost by Feature</h3>
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={getCostBreakdownData()}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip formatter={(value) => `$${value.toFixed(4)}`} />
                    <Legend />
                    <Bar dataKey="cost" fill="#10b981" name="Cost ($)" />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>

            {/* Cost Details Table */}
            <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200 mb-8">
              <h3 className="text-lg font-semibold text-gray-800 mb-4">Cost Breakdown by Feature</h3>
              <div className="overflow-x-auto">
                <table className="w-full text-left">
                  <thead className="border-b border-gray-200">
                    <tr>
                      <th className="pb-3 font-semibold text-gray-700">Feature</th>
                      <th className="pb-3 font-semibold text-gray-700">Total Cost</th>
                      <th className="pb-3 font-semibold text-gray-700">Requests</th>
                      <th className="pb-3 font-semibold text-gray-700">Avg Cost</th>
                    </tr>
                  </thead>
                  <tbody>
                    {costData.by_feature.map((feature, index) => (
                      <tr key={index} className="border-b border-gray-100">
                        <td className="py-3 font-medium capitalize">{feature.feature}</td>
                        <td className="py-3 text-blue-600">${feature.cost.toFixed(4)}</td>
                        <td className="py-3">{feature.requests}</td>
                        <td className="py-3 text-gray-600">${feature.avg_cost.toFixed(6)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Top Users by Cost */}
            {costData.top_users && costData.top_users.length > 0 && (
              <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                <h3 className="text-lg font-semibold text-gray-800 mb-4">Top Users by Cost</h3>
                <div className="overflow-x-auto">
                  <table className="w-full text-left">
                    <thead className="border-b border-gray-200">
                      <tr>
                        <th className="pb-3 font-semibold text-gray-700">User ID</th>
                        <th className="pb-3 font-semibold text-gray-700">Total Cost</th>
                        <th className="pb-3 font-semibold text-gray-700">Requests</th>
                        <th className="pb-3 font-semibold text-gray-700">Avg Cost</th>
                      </tr>
                    </thead>
                    <tbody>
                      {costData.top_users.map((user, index) => (
                        <tr key={index} className="border-b border-gray-100">
                          <td className="py-3 font-medium">User #{user.user_id}</td>
                          <td className="py-3 text-purple-600">${user.cost.toFixed(4)}</td>
                          <td className="py-3">{user.requests}</td>
                          <td className="py-3 text-gray-600">${user.avg_cost.toFixed(6)}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            )}
          </>
        )}

        {/* User Management Dashboard */}
        {activeTab === 'users' && (
          <>
            {/* Summary Cards */}
            <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
              <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                <div className="text-sm text-gray-600 mb-1">Total Users</div>
                <div className="text-3xl font-bold text-gray-800">
                  {users.length}
                </div>
              </div>

              <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                <div className="text-sm text-gray-600 mb-1">Admin Users</div>
                <div className="text-3xl font-bold text-purple-600">
                  {users.filter(u => u.is_admin).length}
                </div>
              </div>

              <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                <div className="text-sm text-gray-600 mb-1">Active Users</div>
                <div className="text-3xl font-bold text-green-600">
                  {users.filter(u => u.is_active).length}
                </div>
              </div>

              <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                <div className="text-sm text-gray-600 mb-1">Blocked Users</div>
                <div className="text-3xl font-bold text-red-600">
                  {users.filter(u => !u.is_active).length}
                </div>
              </div>
            </div>

            {/* Users Table */}
            <div className="bg-white rounded-xl shadow-sm border border-gray-200">
              <div className="p-6 border-b border-gray-200 flex items-center justify-between">
                <h3 className="text-lg font-semibold text-gray-800">All Users</h3>
                <button
                  onClick={fetchUsers}
                  disabled={usersLoading}
                  className="text-blue-600 hover:text-blue-700 font-medium text-sm disabled:opacity-50"
                >
                  🔄 {usersLoading ? 'Loading...' : 'Refresh'}
                </button>
              </div>

              {usersLoading && !users.length ? (
                <div className="p-12 text-center">
                  <div className="text-4xl mb-4 animate-spin">⚙️</div>
                  <p className="text-gray-600">Loading users...</p>
                </div>
              ) : users.length === 0 ? (
                <div className="p-12 text-center">
                  <div className="text-4xl mb-4">👤</div>
                  <p className="text-gray-600">No users found</p>
                </div>
              ) : (
                <div className="overflow-x-auto">
                  <table className="w-full">
                    <thead className="bg-gray-50 border-b border-gray-200">
                      <tr>
                        <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                          User
                        </th>
                        <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                          Provider
                        </th>
                        <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                          Status
                        </th>
                        <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                          Role
                        </th>
                        <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                          Joined
                        </th>
                        <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                          Last Login
                        </th>
                        <th className="px-6 py-4 text-right text-xs font-semibold text-gray-700 uppercase tracking-wider">
                          Actions
                        </th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-200">
                      {users.map((user) => {
                        const isCurrentUser = user.email === session?.user?.email
                        return (
                          <tr key={user.id} className={isCurrentUser ? 'bg-blue-50' : 'hover:bg-gray-50'}>
                            <td className="px-6 py-4">
                              <div className="flex items-center gap-3">
                                <div className="w-10 h-10 rounded-full bg-gradient-to-r from-blue-500 to-purple-500 text-white flex items-center justify-center font-bold">
                                  {user.name?.[0]?.toUpperCase() || user.email[0].toUpperCase()}
                                </div>
                                <div>
                                  <div className="font-medium text-gray-800">
                                    {user.name || 'No name'}
                                    {isCurrentUser && (
                                      <span className="ml-2 text-xs bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full">
                                        You
                                      </span>
                                    )}
                                  </div>
                                  <div className="text-sm text-gray-500">{user.email}</div>
                                </div>
                              </div>
                            </td>
                            <td className="px-6 py-4">
                              <span className="inline-flex items-center gap-1 text-sm capitalize">
                                {user.provider === 'google' ? '🔵' : '⚫'} {user.provider}
                              </span>
                            </td>
                            <td className="px-6 py-4">
                              {user.is_active ? (
                                <span className="inline-flex items-center gap-1 text-sm text-green-700 bg-green-100 px-3 py-1 rounded-full font-medium">
                                  ✓ Active
                                </span>
                              ) : (
                                <span className="inline-flex items-center gap-1 text-sm text-red-700 bg-red-100 px-3 py-1 rounded-full font-medium">
                                  ✗ Blocked
                                </span>
                              )}
                            </td>
                            <td className="px-6 py-4">
                              {user.is_admin ? (
                                <span className="inline-flex items-center gap-1 text-sm text-purple-700 bg-purple-100 px-3 py-1 rounded-full font-medium">
                                  ⚙️ Admin
                                </span>
                              ) : (
                                <span className="inline-flex items-center gap-1 text-sm text-gray-700 bg-gray-100 px-3 py-1 rounded-full font-medium">
                                  👤 User
                                </span>
                              )}
                            </td>
                            <td className="px-6 py-4 text-sm text-gray-600">
                              {new Date(user.created_at).toLocaleDateString('en-US', {
                                year: 'numeric',
                                month: 'short',
                                day: 'numeric'
                              })}
                            </td>
                            <td className="px-6 py-4 text-sm text-gray-600">
                              {user.last_login ? (
                                new Date(user.last_login).toLocaleDateString('en-US', {
                                  year: 'numeric',
                                  month: 'short',
                                  day: 'numeric'
                                })
                              ) : (
                                <span className="text-gray-400">Never</span>
                              )}
                            </td>
                            <td className="px-6 py-4">
                              <div className="flex items-center justify-end gap-2">
                                {/* Toggle Admin Button */}
                                <button
                                  onClick={() => toggleAdmin(user.id, user.is_admin)}
                                  disabled={isCurrentUser || actionLoading === `admin-${user.id}`}
                                  className={`px-3 py-1.5 text-xs font-medium rounded-lg transition-all ${
                                    user.is_admin
                                      ? 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                                      : 'bg-purple-100 text-purple-700 hover:bg-purple-200'
                                  } disabled:opacity-50 disabled:cursor-not-allowed`}
                                  title={isCurrentUser ? 'Cannot modify your own admin status' : user.is_admin ? 'Remove admin' : 'Make admin'}
                                >
                                  {actionLoading === `admin-${user.id}` ? '...' : user.is_admin ? 'Remove Admin' : 'Make Admin'}
                                </button>

                                {/* Toggle Active Button */}
                                <button
                                  onClick={() => toggleActive(user.id, user.is_active)}
                                  disabled={isCurrentUser || actionLoading === `active-${user.id}`}
                                  className={`px-3 py-1.5 text-xs font-medium rounded-lg transition-all ${
                                    user.is_active
                                      ? 'bg-yellow-100 text-yellow-700 hover:bg-yellow-200'
                                      : 'bg-green-100 text-green-700 hover:bg-green-200'
                                  } disabled:opacity-50 disabled:cursor-not-allowed`}
                                  title={isCurrentUser ? 'Cannot block yourself' : user.is_active ? 'Block user' : 'Unblock user'}
                                >
                                  {actionLoading === `active-${user.id}` ? '...' : user.is_active ? 'Block' : 'Unblock'}
                                </button>

                                {/* Delete Button */}
                                <button
                                  onClick={() => deleteUser(user.id, user.email)}
                                  disabled={isCurrentUser || actionLoading === `delete-${user.id}`}
                                  className="px-3 py-1.5 text-xs font-medium bg-red-100 text-red-700 hover:bg-red-200 rounded-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                                  title={isCurrentUser ? 'Cannot delete yourself' : 'Permanently delete user'}
                                >
                                  {actionLoading === `delete-${user.id}` ? '...' : 'Delete'}
                                </button>
                              </div>
                            </td>
                          </tr>
                        )
                      })}
                    </tbody>
                  </table>
                </div>
              )}
            </div>

            {/* Warning Notice */}
            <div className="mt-8 bg-yellow-50 border border-yellow-200 rounded-xl p-6">
              <div className="flex items-start gap-3">
                <div className="text-2xl">⚠️</div>
                <div>
                  <h4 className="font-semibold text-yellow-900 mb-2">Important Safety Notes</h4>
                  <ul className="text-sm text-yellow-800 space-y-1 list-disc list-inside">
                    <li>You cannot modify your own admin status, block yourself, or delete your own account</li>
                    <li>Deleting a user is PERMANENT and cannot be undone</li>
                    <li>Blocked users cannot sign in to the application</li>
                    <li>Removing admin status will revoke access to this dashboard</li>
                  </ul>
                </div>
              </div>
            </div>
          </>
        )}

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