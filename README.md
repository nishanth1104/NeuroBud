# 🌱 NeuroBud - AI Mental Wellness Companion

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Next.js 14](https://img.shields.io/badge/next.js-14-black)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)

---

## ⚠️ Important Disclaimer

**NeuroBud is NOT a replacement for professional mental health care.** If you're experiencing a mental health crisis:
- 🆘 **Call 988** (Suicide & Crisis Lifeline - US)
- 🏥 **Call 911** for immediate emergencies
- 💬 **Text "HELLO" to 741741** (Crisis Text Line)
- 👨‍⚕️ **Contact a licensed therapist** for professional help

---

## 🎯 The Problem

Mental health challenges affect **1 in 5 adults** globally, yet access to timely, affordable, and stigma-free support remains a significant barrier:

- **Long Wait Times:** Average wait for a therapist appointment is 4-6 weeks
- **High Costs:** Therapy sessions can cost $100-$200 per hour without insurance
- **Stigma & Privacy:** Many people hesitate to seek help due to social stigma
- **24/7 Availability:** Mental health crises don't follow business hours
- **Early Intervention:** Many people need someone to talk to before reaching crisis point

Traditional mental health services, while essential, often fail to provide immediate, accessible, and judgment-free support for those in need.

---

## 💡 Why NeuroBud?

NeuroBud was built to bridge the gap between crisis moments and professional care by providing:

✅ **Immediate Support:** 24/7 availability with AI-powered empathetic conversations
✅ **Privacy-First:** Anonymous, stigma-free space to express emotions
✅ **Crisis Detection:** Real-time monitoring with automatic safety interventions
✅ **Mood Tracking:** Daily check-ins to identify patterns and trends
✅ **Resource Connection:** Quick access to crisis hotlines and coping strategies
✅ **Accessibility:** Free, web-based platform requiring no downloads

**NeuroBud is not therapy** - it's a companion that provides emotional support, tracks mental wellness, and connects users to professional help when needed.

---

## ✨ Features (Version 1.0)

### 🤖 AI-Powered Empathetic Chat
- Natural conversations using OpenAI GPT-4o-mini
- Context-aware responses with conversation history
- Average response time: <3 seconds
- Emotionally intelligent language understanding

### 🚨 Real-Time Crisis Detection
- Keyword-based detection system analyzing user messages
- Three severity levels: Low, Moderate, Critical
- Automatic 988 Lifeline recommendations for critical cases
- Crisis event logging for safety monitoring

### 📊 Daily Mood Tracking
- Simple 1-10 mood scale logging
- 7-day mood history with visual charts
- Optional notes for context and reflection
- Trend identification for self-awareness

### 🎯 Mental Health Resources
- National crisis hotlines (988, Crisis Text Line, NAMI)
- Evidence-based CBT coping strategies
- Breathing exercises and grounding techniques
- Professional therapist finder links

### 🔐 User Authentication & Admin Panel
- Secure OAuth authentication (Google, GitHub)
- User profile management
- Admin dashboard for monitoring and analytics
- User management capabilities

### 🛡️ Safety & Security
- Input sanitization (XSS protection)
- Rate limiting (20 chat/min, 10 mood/min)
- SQL injection prevention via ORM
- Error boundaries and offline detection
- Multiple safety disclaimers throughout the app

---

## 🏗️ Tech Stack

### Backend
- **Framework:** FastAPI 0.104+ (Python 3.12)
- **Database:** SQLite with SQLAlchemy 2.0 ORM
- **AI Engine:** OpenAI GPT-4o-mini API
- **Authentication:** NextAuth.js integration
- **Rate Limiting:** SlowAPI (IP-based throttling)
- **Vector Database:** ChromaDB 0.4.22 (for RAG capabilities)
- **Testing:** pytest with 100% passing tests
- **Deployment:** Railway (production backend)

### Frontend
- **Framework:** Next.js 14 (App Router, React 18)
- **Styling:** Tailwind CSS 3.3
- **Authentication:** NextAuth.js (OAuth providers)
- **Data Visualization:** Recharts 3.4
- **HTTP Client:** Axios 1.13
- **Markdown Rendering:** react-markdown 10.1
- **Deployment:** Vercel (production frontend)

### DevOps & Infrastructure
- **Version Control:** Git & GitHub
- **Database Hosting:** SQLite
- **Backend Hosting:** Railway
- **Frontend Hosting:** Vercel
- **Environment Management:** python-dotenv, .env files

---

## 📊 Current Performance Metrics

| Metric | Value | Status |
|--------|-------|--------|
| Health Check Response | 3.84ms | ✅ |
| Mood Logging | 12.78ms | ✅ |
| Mood History Retrieval | 5.69ms | ✅ |
| Analytics Query | 9.60ms | ✅ |
| Test Coverage | 100% | ✅ |
| Chat Response Time | <3s | ✅ |

---

## 🔮 Roadmap: Version 2.0 (Coming Soon)

NeuroBud Version 2.0 will include major enhancements focused on personalization, advanced analytics, and security:

### 🎨 Enhanced User Experience
- **Mobile Responsive Design:** Fully optimized for smartphones and tablets
- **Progressive Web App (PWA):** Installable app with offline capabilities
- **Dark Mode:** Reduce eye strain with customizable themes
- **Multi-language Support:** Accessibility for non-English speakers

### 🧠 Advanced Mental Health Features
- **CBT Interactive Exercises:** Guided cognitive behavioral therapy activities
  - Thought records and cognitive restructuring
  - Behavioral activation planning
  - Exposure hierarchy creation
- **30-Day Mood Analysis:** Extended mood tracking with:
  - Monthly trends and pattern recognition
  - Correlation with activities, sleep, and weather
  - Exportable PDF reports for therapists
- **Advanced Sentiment Analysis:** NLP-powered emotion detection
  - Multi-dimensional emotion tracking (joy, sadness, anxiety, anger)
  - Sentiment trends over time
  - Early warning system for mood deterioration

### 🔐 Security & Privacy Enhancements
- **Client-Side Encryption:** End-to-end encryption for all messages
  - Zero-knowledge architecture
  - User-controlled encryption keys
- **Two-Factor Authentication (2FA):** Enhanced account security
- **Data Export & Deletion:** GDPR-compliant user data management
- **Anonymization Features:** Pseudonymous usage options

### 🤖 AI & Personalization
- **Fine-Tuned Mental Health Model:** Custom GPT model trained on:
  - Mental health conversation datasets
  - Crisis intervention best practices
  - Therapeutic communication patterns
- **RAG System Integration:** Context-aware responses using:
  - Vector database of mental health resources
  - Personalized coping strategy recommendations
- **Voice Interaction:** Speech-to-text for accessibility
- **Personalized Insights:** AI-generated weekly wellness summaries

### 📈 Analytics & Insights
- **Advanced Dashboard:** Comprehensive mental wellness overview
  - Mood patterns and triggers
  - Chat engagement metrics
  - Crisis event timeline
- **Journaling Integration:** Free-form journaling with AI insights
- **Goal Setting & Tracking:** Mental wellness objectives with progress monitoring

### 🌐 Community & Resources
- **Peer Support Forums:** Moderated community discussions (anonymous)
- **Therapist Directory:** Vetted mental health professional matching
- **Educational Content:** Mental health literacy articles and videos
- **Crisis Intervention Training:** Resources for helping others

### 🔧 Technical Improvements
- **A/B Testing Framework:** Model performance comparison
- **Email Notifications:** Daily reminders, mood check-ins, crisis alerts
- **CI/CD Pipeline:** GitHub Actions for automated testing and deployment
- **Monitoring & Observability:** Sentry for error tracking, analytics dashboards
- **WebSocket Support:** Real-time chat with typing indicators
- **API Rate Limit Tiers:** Premium features for power users

---

## 🏛️ Project Architecture

```
NeuroBud/
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── ai/                # AI engines (chat, crisis detection)
│   │   ├── database/          # Database connection & session management
│   │   ├── models/            # SQLAlchemy models (User, Conversation, Mood, Crisis)
│   │   ├── utils/             # Utilities (sanitizer, validators)
│   │   ├── middleware/        # Request logging, auth middleware
│   │   └── main.py            # FastAPI app entry point
│   ├── tests/                 # pytest test suite
│   └── requirements.txt       # Python dependencies
├── frontend/                   # Next.js frontend
│   ├── app/
│   │   ├── chat/              # AI chat interface
│   │   ├── mood/              # Mood tracker page
│   │   ├── resources/         # Mental health resources
│   │   ├── admin/             # Admin dashboard
│   │   └── api/auth/          # NextAuth.js API routes
│   └── package.json           # Node.js dependencies
└── README.md                   # This file
```

---

## 🎨 Screenshots

### Landing Page
<img width="1895" height="959" alt="image" src="https://github.com/user-attachments/assets/25be4e35-bff1-4ca7-addb-57e904bfd762" />


### AI Chat Interface
<img width="1915" height="958" alt="image" src="https://github.com/user-attachments/assets/267e2a4c-e83a-43af-82b6-90b63c40e6b2" />


### Mood Tracker
<img width="1772" height="948" alt="image" src="https://github.com/user-attachments/assets/6e8ad099-89d1-4aa1-a63d-c0976950fc05" />


### Resources Page
<img width="1348" height="940" alt="image" src="https://github.com/user-attachments/assets/ad852864-5ae7-45d3-9ff7-90d4784c4176" />
<img width="1324" height="937" alt="image" src="https://github.com/user-attachments/assets/8cf1a075-7a10-482c-86b8-4bf6b2ea98db" />
<img width="1384" height="729" alt="image" src="https://github.com/user-attachments/assets/aee9b5fd-c612-48b2-8894-a5e3194679ea" />



---

## 📝 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Nishanth Ayyalasomayajula

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Note:** This software is intended for supportive purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

---

## 👤 Author

**Nishanth Ayyalasomayajula**

- GitHub: [@nishanth1104](https://github.com/nishanth1104)
- LinkedIn: [Nishanth Ayyalasomayajula](https://linkedin.com/in/nishanth-ayyalasomayajula)
- Email: nishanthayyalasomayajula@gmail.com

---

## 🙏 Acknowledgments

- **OpenAI** for GPT-4o-mini API enabling empathetic conversations
- **FastAPI** for the high-performance web framework
- **Next.js** for the React framework and excellent developer experience
- **Supabase** for SQLite hosting and real-time capabilities
- **988 Lifeline & Crisis Text Line** for crisis intervention resources
- **Mental Health America & NAMI** for educational resources
- **Open-source community** for the amazing tools and libraries

---

## ⚖️ Ethical Considerations

NeuroBud is built with mental health ethics at its core:

✅ **Transparency:** Clear disclaimers that it's AI, not therapy
✅ **Crisis Intervention:** Multiple touchpoints connecting users to 988 Lifeline
✅ **Privacy:** User data handled with care, minimal collection
✅ **No Medical Claims:** Never positioned as medical treatment
✅ **Responsible AI:** Prompts engineered to avoid harmful advice
✅ **Accessibility:** Free and open-source for maximum reach

**Mental health is a human right.** This project respects the gravity of mental wellness and aims to complement, not replace, professional care.

---

## 📊 Project Statistics

- **Version:** 1.0 (Production Ready)
- **Lines of Code:** ~5,500+
- **API Endpoints:** 10+
- **Database Tables:** 5 (User, Conversation, Message, Mood, CrisisEvent)
- **Frontend Pages:** 6 (Home, Chat, Mood, Resources, Admin, Sign In)
- **Tests:** 7 (100% passing)
- **Performance:** <20ms average API response time
- **Development Time:** 3 weeks (MVP + Auth + Admin)

---

## 🌟 Star This Project

If NeuroBud resonates with you or you believe in accessible mental health support, please consider:
- Giving this repository a star
- Sharing it with others who might benefit
- Contributing to its development
- Providing feedback and suggestions

Together, we can make mental wellness support more accessible to everyone.

---

**Built with care for mental wellness by Nishanth Ayyalasomayajula**

*Remember: You are not alone. Help is available. Recovery is possible.*
