'use client'

import { useSearchParams } from 'next/navigation'
import Link from 'next/link'
import { Suspense } from 'react'

function ErrorContent() {
  const searchParams = useSearchParams()
  const error = searchParams.get('error')
  const message = searchParams.get('message')

  let errorTitle = 'Authentication Error'
  let errorMessage = 'An error occurred during authentication. Please try again.'

  if (error === 'AccessDenied') {
    errorTitle = 'Access Denied'
    errorMessage = message || 'Your account has been blocked by an administrator. Please contact support for assistance.'
  } else if (error === 'Configuration') {
    errorTitle = 'Configuration Error'
    errorMessage = 'There is a problem with the server configuration.'
  } else if (error === 'Verification') {
    errorTitle = 'Verification Error'
    errorMessage = 'The verification token has expired or has already been used.'
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50 flex items-center justify-center p-4">
      <div className="max-w-md w-full">
        {/* Error Icon */}
        <div className="text-center mb-8">
          <div className="text-6xl mb-4">🚫</div>
          <h1 className="text-3xl font-bold text-gray-800 mb-2">{errorTitle}</h1>
          <p className="text-gray-600">{errorMessage}</p>
        </div>

        {/* Error Card */}
        <div className="bg-white rounded-2xl shadow-xl p-8 border border-gray-200">
          {error === 'AccessDenied' && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
              <div className="flex items-start gap-3">
                <div className="text-2xl">⚠️</div>
                <div>
                  <h3 className="font-semibold text-red-900 mb-1">Account Blocked</h3>
                  <p className="text-sm text-red-800">
                    Your account has been disabled by an administrator. If you believe this is a mistake,
                    please contact support.
                  </p>
                </div>
              </div>
            </div>
          )}

          {/* Action Buttons */}
          <div className="space-y-3">
            <Link
              href="/auth/signin"
              className="block w-full text-center px-6 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition-all"
            >
              Try Again
            </Link>
            <Link
              href="/"
              className="block w-full text-center px-6 py-3 bg-gray-100 text-gray-700 rounded-lg font-semibold hover:bg-gray-200 transition-all"
            >
              Go Home
            </Link>
          </div>

          {/* Support Info */}
          {error === 'AccessDenied' && (
            <div className="mt-6 pt-6 border-t border-gray-200">
              <p className="text-sm text-gray-600 text-center">
                Need help? Contact support at{' '}
                <a href="mailto:support@neurobud.com" className="text-blue-600 hover:underline">
                  support@neurobud.com
                </a>
              </p>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="text-center mt-6 text-sm text-gray-500">
          <p>Neurobud - Mental Wellness Companion</p>
        </div>
      </div>
    </div>
  )
}

export default function AuthError() {
  return (
    <Suspense fallback={
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50 flex items-center justify-center">
        <div className="text-4xl animate-spin">⚙️</div>
      </div>
    }>
      <ErrorContent />
    </Suspense>
  )
}
