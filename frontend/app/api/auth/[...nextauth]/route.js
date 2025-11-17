import NextAuth from "next-auth"
import GoogleProvider from "next-auth/providers/google"
import GitHubProvider from "next-auth/providers/github"

export const authOptions = {
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    }),
    GitHubProvider({
      clientId: process.env.GITHUB_ID,
      clientSecret: process.env.GITHUB_SECRET,
    }),
  ],
  callbacks: {
    async signIn({ user, account, profile }) {
      // Send user data to backend
      try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/auth/login`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: user.email,
            name: user.name,
            provider: account.provider,
            provider_id: account.providerAccountId,
            avatar_url: user.image,
          }),
        })

        if (response.ok) {
          const data = await response.json()
          // Check if user is active
          if (data.is_active === false) {
            // User is blocked - prevent sign in
            return false
          }
          return true
        } else if (response.status === 403) {
          // User is blocked by admin
          const errorData = await response.json()
          console.error('Account blocked:', errorData.detail)
          // Redirect to error page with message
          return `/auth/error?error=AccessDenied&message=${encodeURIComponent(errorData.detail || 'Your account has been blocked.')}`
        }

        // Other errors - prevent sign in
        console.error('Login failed with status:', response.status)
        return false
      } catch (error) {
        console.error('Error logging in:', error)
        return false
      }
    },
    async session({ session, token }) {
      // Add custom fields to session
      session.user.id = token.sub
      return session
    },
  },
  pages: {
    signIn: '/auth/signin',
    error: '/auth/error',
  },
  session: {
    strategy: 'jwt',
    maxAge: 30 * 24 * 60 * 60, // 30 days
  },
}

const handler = NextAuth(authOptions)

export { handler as GET, handler as POST }