import Link from 'next/link'

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50 flex items-center justify-center p-6">
      <div className="max-w-2xl text-center">
        <div className="text-7xl mb-6">🌱</div>
        
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
        
        <Link 
          href="/chat"
          className="inline-block bg-blue-600 text-white px-10 py-4 rounded-xl text-xl font-semibold hover:bg-blue-700 transition-colors shadow-lg hover:shadow-xl"
        >
          Start Chatting 💬
        </Link>
        
        <p className="text-sm text-gray-500 mt-8">
          Neurobud is an AI companion, not a therapist. For professional help, 
          <Link href="/resources" className="underline ml-1">see our resources</Link>.
        </p>
      </div>
    </div>
  )
}