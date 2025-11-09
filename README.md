# 🌱 Neurobud - AI Mental Wellness Companion

> An empathetic AI chatbot providing mental health support, crisis detection, and mood tracking.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Next.js 14](https://img.shields.io/badge/next.js-14-black)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)

---

## ⚠️ Important Disclaimer

**Neurobud is NOT a replacement for professional mental health care.** It is an AI companion for emotional support and wellness tracking. If you're experiencing a mental health crisis, please:

- 🆘 **Call 988** (Suicide & Crisis Lifeline - US)
- 🏥 **Call 911** for immediate emergencies
- 💬 **Text "HELLO" to 741741** (Crisis Text Line)
- 👨‍⚕️ **Contact a licensed therapist** for professional help

---

## ✨ Features

### 🤖 AI-Powered Chat
- Empathetic conversations using OpenAI GPT-4o-mini
- Context-aware responses with conversation history
- Natural language understanding
- Average response time: <3 seconds

### 🚨 Real-Time Crisis Detection
- Keyword-based detection system
- Three severity levels: Low, Moderate, Critical
- Automatic 988 hotline recommendations
- Crisis event logging for safety monitoring

### 📊 Mood Tracking
- Daily mood logging (1-10 scale)
- 7-day mood history visualization
- Optional notes for context
- Trend analysis and insights

### 🎯 Mental Health Resources
- National crisis hotlines
- CBT coping strategies
- Breathing exercises
- Grounding techniques
- Professional therapist finder

### 🛡️ Safety Features
- Multiple safety disclaimers
- Rate limiting (20 chat/min, 10 mood/min)
- Input sanitization (XSS protection)
- Error handling and validation
- Offline detection

---

## 🏗️ Tech Stack

### Backend
- **Framework:** FastAPI 0.104+
- **Database:** PostgreSQL (Supabase) / SQLite
- **AI:** OpenAI GPT-4o-mini
- **ORM:** SQLAlchemy 2.0
- **Testing:** pytest (7 tests, 100% passing)
- **Rate Limiting:** SlowAPI

### Frontend
- **Framework:** Next.js 14 (App Router)
- **Styling:** Tailwind CSS
- **HTTP Client:** Axios
- **Deployment:** Vercel-ready

---

## 📊 Performance Metrics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Health Check | 3.84ms | <10ms | ✅ |
| Mood Logging | 12.78ms | <100ms | ✅ |
| Mood History | 5.69ms | <200ms | ✅ |
| Analytics | 9.60ms | <200ms | ✅ |
| Test Coverage | 100% | 80%+ | ✅ |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Node.js 18+
- OpenAI API Key
- PostgreSQL or Supabase account

### Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your OPENAI_API_KEY and DATABASE_URL

# Run server
uvicorn app.main:app --reload
```

Backend runs on `http://127.0.0.1:8000`

### Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Configure environment
cp .env.local.example .env.local
# Edit .env.local with NEXT_PUBLIC_API_URL

# Run dev server
npm run dev
```

Frontend runs on `http://localhost:3000`

---

## 🧪 Testing
```bash
cd backend
pytest tests/ -v

# Performance testing
python test_performance.py
```

**Test Results:**
- 7/7 tests passing ✅
- Health check, mood logging, analytics covered
- SQLite test database (no internet needed)

---

## 📚 Documentation

- **[Setup Guide](SETUP.md)** - Complete development setup
- **[API Documentation](API.md)** - Endpoint reference
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute

---

## 🗂️ Project Structure
```
neurobud/
├── backend/
│   ├── app/
│   │   ├── ai/              # AI engines (chat, crisis detection)
│   │   ├── database/        # Database connection
│   │   ├── models/          # SQLAlchemy models
│   │   ├── utils/           # Utilities (sanitizer, cleanup)
│   │   ├── middleware/      # Request logging
│   │   └── main.py          # FastAPI app
│   ├── tests/               # pytest tests
│   ├── requirements.txt     # Python dependencies
│   └── .env.example         # Environment template
├── frontend/
│   ├── app/
│   │   ├── chat/            # Chat page
│   │   ├── mood/            # Mood tracker
│   │   ├── resources/       # Resources page
│   │   └── page.js          # Landing page
│   ├── package.json         # Node dependencies
│   └── .env.local.example   # Environment template
├── SETUP.md                 # Setup instructions
├── API.md                   # API documentation
├── CONTRIBUTING.md          # Contribution guidelines
└── README.md                # This file
```

---

## 🔐 Security Features

- ✅ Input sanitization (XSS, null bytes, script tags)
- ✅ Rate limiting per IP address
- ✅ SQL injection prevention (ORM)
- ✅ Request validation with Pydantic
- ✅ CORS configuration
- ✅ Error handling and logging
- ✅ Database connection pooling

---

## 🎨 Screenshots

### Landing Page
*Professional hero section with clear CTA buttons*

### AI Chat Interface
*Real-time empathetic conversations with crisis detection*

### Mood Tracker
*Daily mood logging with 7-day history visualization*

### Resources Page
*Crisis hotlines and CBT coping strategies*

---

## 📈 Roadmap

### Week 2 (Days 8-14)
- [ ] User authentication (OAuth 2.0)
- [ ] Fine-tuned GPT model for mental health
- [ ] RAG system with Qdrant vector database
- [ ] Advanced sentiment analysis
- [ ] A/B testing framework
- [ ] Email notifications

### Week 3 (Days 15-21)
- [ ] Production deployment (Vercel + Railway)
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Monitoring & analytics (Sentry)
- [ ] User feedback system
- [ ] Mobile responsiveness optimization
- [ ] Final portfolio polish

---

## 🤝 Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

### Development Workflow
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Nishanth Ayyalasomayajula**

- GitHub: [@nishanth1104](https://github.com/nishanth1104)
- LinkedIn: [Nishanth Ayyalasomayajula](https://linkedin.com/in/your-profile)
- Portfolio: [your-portfolio.com](https://your-portfolio.com)

---

## 🙏 Acknowledgments

- OpenAI for GPT-4o-mini API
- FastAPI for the excellent web framework
- Next.js for the React framework
- Supabase for database hosting
- Crisis Text Line and 988 Lifeline for resources

---

## ⚖️ Ethical Considerations

**Neurobud is built with mental health ethics in mind:**

- ✅ Clear disclaimers that it's not therapy
- ✅ Multiple crisis intervention touchpoints
- ✅ No data collection without consent
- ✅ Transparent about AI limitations
- ✅ Privacy-first design
- ✅ Responsible AI usage

**If you're experiencing a mental health crisis, please seek professional help immediately.**

---

## 📊 Project Stats

- **Lines of Code:** ~4,000+
- **API Endpoints:** 6
- **Database Tables:** 4
- **Frontend Pages:** 4
- **Tests:** 7 (100% passing)
- **Performance:** <20ms average response time
- **Development Time:** 7 days (MVP)

---

## 🌟 Star History

If you find Neurobud helpful, please consider giving it a star! ⭐

---

**Built with ❤️ for mental wellness**