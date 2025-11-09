'use client'

import Link from 'next/link'
import { useState } from 'react'

export default function ResourcesPage() {
  const [expandedSection, setExpandedSection] = useState(null)

  const toggleSection = (section) => {
    setExpandedSection(expandedSection === section ? null : section)
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <nav className="bg-white border-b shadow-sm">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <Link href="/" className="text-2xl font-bold text-blue-600 flex items-center gap-2">
            🌱 Neurobud
          </Link>
          <div className="flex gap-4">
            <Link href="/chat" className="text-gray-600 hover:text-blue-600 font-medium">
              Chat
            </Link>
            <Link href="/mood" className="text-gray-600 hover:text-blue-600 font-medium">
              Mood
            </Link>
            <Link href="/resources" className="text-blue-600 font-semibold border-b-2 border-blue-600">
              Resources
            </Link>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <div className="bg-gradient-to-br from-blue-600 to-purple-700 text-white py-12">
        <div className="max-w-4xl mx-auto px-6 text-center">
          <h1 className="text-5xl font-bold mb-4">Mental Health Resources</h1>
          <p className="text-xl">You don't have to face this alone. Help is available.</p>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-4xl mx-auto px-6 py-12">
        
        {/* Crisis Resources - ALWAYS VISIBLE */}
        <div className="bg-red-50 border-2 border-red-300 rounded-2xl p-8 mb-8">
          <h2 className="text-3xl font-bold text-red-900 mb-6 flex items-center gap-3">
            <span className="animate-pulse">🆘</span> Crisis Resources - Available 24/7
          </h2>
          
          <div className="space-y-4">
            <div className="bg-white rounded-xl p-6 shadow-md">
              <h3 className="text-2xl font-bold text-gray-800 mb-2">988 Suicide & Crisis Lifeline</h3>
              <p className="text-gray-600 mb-3">24/7 free and confidential support for people in distress</p>
              <div className="flex flex-col gap-2">
                <a href="tel:988" className="bg-red-600 text-white px-6 py-3 rounded-lg font-bold text-center hover:bg-red-700 transition-colors">
                  📞 Call 988
                </a>
                <a href="sms:988" className="bg-red-600 text-white px-6 py-3 rounded-lg font-bold text-center hover:bg-red-700 transition-colors">
                  💬 Text 988
                </a>
              </div>
            </div>

            <div className="bg-white rounded-xl p-6 shadow-md">
              <h3 className="text-xl font-bold text-gray-800 mb-2">Crisis Text Line</h3>
              <p className="text-gray-600 mb-3">Text HOME to 741741 for free, 24/7 crisis support</p>
              <a href="sms:741741&body=HOME" className="bg-blue-600 text-white px-6 py-3 rounded-lg font-bold inline-block hover:bg-blue-700 transition-colors">
                💬 Text HOME to 741741
              </a>
            </div>

            <div className="bg-white rounded-xl p-6 shadow-md">
              <h3 className="text-xl font-bold text-gray-800 mb-2">Emergency Services</h3>
              <p className="text-gray-600 mb-3">For immediate life-threatening emergencies</p>
              <a href="tel:911" className="bg-gray-800 text-white px-6 py-3 rounded-lg font-bold inline-block hover:bg-gray-900 transition-colors">
                🚨 Call 911
              </a>
            </div>

            <div className="bg-white rounded-xl p-6 shadow-md">
              <h3 className="text-xl font-bold text-gray-800 mb-2">SAMHSA National Helpline</h3>
              <p className="text-gray-600 mb-3">Treatment referral and information (substance abuse & mental health)</p>
              <a href="tel:1-800-662-4357" className="bg-green-600 text-white px-6 py-3 rounded-lg font-bold inline-block hover:bg-green-700 transition-colors">
                📞 1-800-662-HELP (4357)
              </a>
            </div>

            <div className="bg-white rounded-xl p-6 shadow-md">
              <h3 className="text-xl font-bold text-gray-800 mb-2">Trevor Project (LGBTQ+ Youth)</h3>
              <p className="text-gray-600 mb-3">Crisis intervention and suicide prevention for LGBTQ+ young people</p>
              <a href="tel:1-866-488-7386" className="bg-purple-600 text-white px-6 py-3 rounded-lg font-bold inline-block hover:bg-purple-700 transition-colors">
                📞 1-866-488-7386
              </a>
            </div>
          </div>
        </div>

        {/* Find a Therapist */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-8">
          <h2 className="text-3xl font-bold text-gray-800 mb-6 flex items-center gap-3">
            👨‍⚕️ Find a Therapist
          </h2>
          
          <div className="space-y-4">
            <div className="border-2 border-blue-200 rounded-xl p-6 hover:border-blue-400 hover:shadow-lg transform hover:scale-105 transition-all duration-200">
              <h3 className="text-xl font-bold text-gray-800 mb-2">Psychology Today Directory</h3>
              <p className="text-gray-600 mb-4">Search for therapists by location, insurance, specialty, and more</p>
              <a 
                href="https://www.psychologytoday.com/us/therapists" 
                target="_blank" 
                rel="noopener noreferrer"
                className="bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold inline-block hover:bg-blue-700 transition-colors"
              >
                🔍 Search Therapists →
              </a>
            </div>

            <div className="border-2 border-green-200 rounded-xl p-6 hover:border-green-400 hover:shadow-lg transform hover:scale-105 transition-all duration-200">
              <h3 className="text-xl font-bold text-gray-800 mb-2">BetterHelp</h3>
              <p className="text-gray-600 mb-4">Online therapy with licensed professionals ($60-90/week)</p>
              <a 
                href="https://www.betterhelp.com/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="bg-green-600 text-white px-6 py-3 rounded-lg font-semibold inline-block hover:bg-green-700 transition-colors"
              >
                💻 Try BetterHelp →
              </a>
            </div>

            <div className="border-2 border-purple-200 rounded-xl p-6 hover:border-purple-400 hover:shadow-lg transform hover:scale-105 transition-all duration-200">
              <h3 className="text-xl font-bold text-gray-800 mb-2">Open Path Collective</h3>
              <p className="text-gray-600 mb-4">Affordable therapy ($30-80/session) for people without insurance</p>
              <a 
                href="https://openpathcollective.org/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="bg-purple-600 text-white px-6 py-3 rounded-lg font-semibold inline-block hover:bg-purple-700 transition-colors"
              >
                💰 Find Affordable Therapy →
              </a>
            </div>

            <div className="border-2 border-orange-200 rounded-xl p-6 hover:border-orange-400 hover:shadow-lg transform hover:scale-105 transition-all duration-200">
              <h3 className="text-xl font-bold text-gray-800 mb-2">SAMHSA Treatment Locator</h3>
              <p className="text-gray-600 mb-4">Government-run directory for mental health and substance abuse treatment</p>
              <a 
                href="https://findtreatment.samhsa.gov/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="bg-orange-600 text-white px-6 py-3 rounded-lg font-semibold inline-block hover:bg-orange-700 transition-colors"
              >
                🏥 Find Treatment →
              </a>
            </div>
          </div>
        </div>

        {/* Coping Strategies (Expandable) */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-8">
          <h2 className="text-3xl font-bold text-gray-800 mb-6 flex items-center gap-3">
            🧘 Coping Strategies
          </h2>

          {/* 5-4-3-2-1 Grounding */}
          <div className="mb-4">
            <button
              onClick={() => toggleSection('grounding')}
              className="w-full text-left bg-blue-50 hover:bg-blue-100 border-2 border-blue-200 rounded-xl p-4 font-semibold text-lg transition-colors flex justify-between items-center"
            >
              <span>🌿 5-4-3-2-1 Grounding Technique (for anxiety/panic)</span>
              <span className="text-2xl">{expandedSection === 'grounding' ? '−' : '+'}</span>
            </button>
            {expandedSection === 'grounding' && (
              <div className="bg-blue-50 border-2 border-blue-200 border-t-0 rounded-b-xl p-6">
                <p className="text-gray-700 mb-4">
                  This technique helps you stay grounded in the present moment when feeling overwhelmed:
                </p>
                <ol className="list-decimal list-inside space-y-2 text-gray-700">
                  <li><strong>5 things you can see</strong> - Look around and name 5 things (e.g., lamp, tree, book)</li>
                  <li><strong>4 things you can touch</strong> - Notice textures (e.g., soft blanket, cold water)</li>
                  <li><strong>3 things you can hear</strong> - Listen carefully (e.g., birds, traffic, clock ticking)</li>
                  <li><strong>2 things you can smell</strong> - Notice scents (e.g., coffee, soap, fresh air)</li>
                  <li><strong>1 thing you can taste</strong> - Taste your mouth or have a sip of water</li>
                </ol>
                <p className="text-sm text-gray-600 mt-4 italic">
                  💡 This works by shifting your focus from anxious thoughts to your immediate sensory experience.
                </p>
              </div>
            )}
          </div>

          {/* Box Breathing */}
          <div className="mb-4">
            <button
              onClick={() => toggleSection('breathing')}
              className="w-full text-left bg-green-50 hover:bg-green-100 border-2 border-green-200 rounded-xl p-4 font-semibold text-lg transition-colors flex justify-between items-center"
            >
              <span>💨 Box Breathing (for stress/anxiety)</span>
              <span className="text-2xl">{expandedSection === 'breathing' ? '−' : '+'}</span>
            </button>
            {expandedSection === 'breathing' && (
              <div className="bg-green-50 border-2 border-green-200 border-t-0 rounded-b-xl p-6">
                <p className="text-gray-700 mb-4">
                  A powerful breathing technique used by Navy SEALs to stay calm under pressure:
                </p>
                <div className="bg-white rounded-lg p-6 mb-4">
                  <div className="grid grid-cols-2 gap-4 text-center">
                    <div className="bg-blue-100 rounded-lg p-4">
                      <div className="text-3xl font-bold text-blue-800">4</div>
                      <div className="text-sm text-blue-700">Breathe IN</div>
                    </div>
                    <div className="bg-purple-100 rounded-lg p-4">
                      <div className="text-3xl font-bold text-purple-800">4</div>
                      <div className="text-sm text-purple-700">HOLD</div>
                    </div>
                    <div className="bg-green-100 rounded-lg p-4">
                      <div className="text-3xl font-bold text-green-800">4</div>
                      <div className="text-sm text-green-700">Breathe OUT</div>
                    </div>
                    <div className="bg-orange-100 rounded-lg p-4">
                      <div className="text-3xl font-bold text-orange-800">4</div>
                      <div className="text-sm text-orange-700">HOLD</div>
                    </div>
                  </div>
                </div>
                <p className="text-sm text-gray-600 italic">
                  💡 Repeat for 5-10 cycles. This activates your parasympathetic nervous system (rest & digest mode).
                </p>
              </div>
            )}
          </div>

          {/* Progressive Muscle Relaxation */}
          <div className="mb-4">
            <button
              onClick={() => toggleSection('pmr')}
              className="w-full text-left bg-purple-50 hover:bg-purple-100 border-2 border-purple-200 rounded-xl p-4 font-semibold text-lg transition-colors flex justify-between items-center"
            >
              <span>💪 Progressive Muscle Relaxation (for tension/insomnia)</span>
              <span className="text-2xl">{expandedSection === 'pmr' ? '−' : '+'}</span>
            </button>
            {expandedSection === 'pmr' && (
              <div className="bg-purple-50 border-2 border-purple-200 border-t-0 rounded-b-xl p-6">
                <p className="text-gray-700 mb-4">
                  Systematically tense and relax muscle groups to release physical tension:
                </p>
                <ol className="list-decimal list-inside space-y-2 text-gray-700">
                  <li>Find a comfortable position (sitting or lying down)</li>
                  <li><strong>Tense</strong> one muscle group (e.g., fists) for 5 seconds</li>
                  <li><strong>Release</strong> and notice the relaxation for 10 seconds</li>
                  <li>Move through: hands → arms → shoulders → face → jaw → neck → chest → stomach → legs → feet</li>
                </ol>
                <p className="text-sm text-gray-600 mt-4 italic">
                  💡 Takes 10-15 minutes. Great before bed for people with insomnia.
                </p>
              </div>
            )}
          </div>

          {/* Behavioral Activation */}
          <div className="mb-4">
            <button
              onClick={() => toggleSection('behavioral')}
              className="w-full text-left bg-yellow-50 hover:bg-yellow-100 border-2 border-yellow-200 rounded-xl p-4 font-semibold text-lg transition-colors flex justify-between items-center"
            >
              <span>⚡ Behavioral Activation (for depression/low motivation)</span>
              <span className="text-2xl">{expandedSection === 'behavioral' ? '−' : '+'}</span>
            </button>
            {expandedSection === 'behavioral' && (
              <div className="bg-yellow-50 border-2 border-yellow-200 border-t-0 rounded-b-xl p-6">
                <p className="text-gray-700 mb-4">
                  When depressed, we avoid activities that could improve our mood. This breaks the cycle:
                </p>
                <div className="bg-white rounded-lg p-4 mb-4">
                  <h4 className="font-bold text-gray-800 mb-2">Small Mood-Boosting Activities:</h4>
                  <ul className="list-disc list-inside space-y-1 text-gray-700">
                    <li>☀️ Get 10 minutes of sunlight</li>
                    <li>🚶 Take a 5-minute walk</li>
                    <li>🎵 Listen to one favorite song</li>
                    <li>📞 Text a friend "hi"</li>
                    <li>🧹 Clean one small thing (make your bed)</li>
                    <li>🍎 Eat a healthy snack</li>
                    <li>🎨 Do 5 minutes of a hobby</li>
                  </ul>
                </div>
                <p className="text-sm text-gray-600 italic">
                  💡 Start with ONE tiny action. Momentum builds from there. Don't aim for perfection.
                </p>
              </div>
            )}
          </div>
        </div>

        {/* When to Seek Professional Help */}
        <div className="bg-white rounded-2xl shadow-lg p-8">
          <h2 className="text-3xl font-bold text-gray-800 mb-6 flex items-center gap-3">
            🩺 When to Seek Professional Help
          </h2>
          
          <p className="text-gray-700 mb-4">
            Consider reaching out to a therapist if you experience:
          </p>

          <div className="grid md:grid-cols-2 gap-4">
            <div className="bg-red-50 border-2 border-red-200 rounded-xl p-4">
              <h3 className="font-bold text-red-900 mb-2">🚨 Urgent (Seek Help Immediately)</h3>
              <ul className="text-sm text-red-800 space-y-1">
                <li>• Thoughts of suicide or self-harm</li>
                <li>• Unable to function in daily life</li>
                <li>• Severe panic attacks (daily)</li>
                <li>• Not eating or sleeping for days</li>
                <li>• Hearing voices or hallucinations</li>
              </ul>
            </div>

            <div className="bg-orange-50 border-2 border-orange-200 rounded-xl p-4">
              <h3 className="font-bold text-orange-900 mb-2">⚠️ Soon (Within 1-2 Weeks)</h3>
              <ul className="text-sm text-orange-800 space-y-1">
                <li>• Persistent sadness (2+ weeks)</li>
                <li>• Anxiety interfering with work/school</li>
                <li>• Substance use affecting your life</li>
                <li>• Relationship problems causing distress</li>
                <li>• Trauma symptoms (flashbacks, nightmares)</li>
              </ul>
            </div>
          </div>

          <div className="bg-blue-50 border-2 border-blue-200 rounded-xl p-4 mt-4">
            <p className="text-blue-900 font-semibold">
              💙 Remember: You don't need to be in crisis to deserve therapy. Prevention is just as important as treatment!
            </p>
          </div>
        </div>

      </div>
    </div>
  )
}