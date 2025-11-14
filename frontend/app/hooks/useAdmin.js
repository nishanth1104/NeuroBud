import { useState, useEffect } from 'react'
import { useSession } from 'next-auth/react'
import axios from 'axios'

export function useAdmin() {
  const { data: session } = useSession()
  const [isAdmin, setIsAdmin] = useState(false)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const checkAdmin = async () => {
      if (!session?.user?.email) {
        setIsAdmin(false)
        setLoading(false)
        return
      }

      try {
        const response = await axios.get(
          `${process.env.NEXT_PUBLIC_API_URL}/api/auth/check-admin?user_email=${session.user.email}`
        )
        setIsAdmin(response.data.is_admin)
      } catch (error) {
        console.error('Error checking admin:', error)
        setIsAdmin(false)
      } finally {
        setLoading(false)
      }
    }

    checkAdmin()
  }, [session])

  return { isAdmin, loading }
}