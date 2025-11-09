# 🚀 Neurobud Setup Guide

Complete guide to set up Neurobud locally for development.

---

## 📋 Prerequisites

- **Python 3.12+** ([Download](https://www.python.org/downloads/))
- **Node.js 18+** ([Download](https://nodejs.org/))
- **PostgreSQL** (or Supabase account) ([Supabase](https://supabase.com))
- **OpenAI API Key** ([Get key](https://platform.openai.com/api-keys))

---

## ⚙️ Backend Setup

### 1. Navigate to Backend
```bash
cd backend
```

### 2. Create Virtual Environment

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy example env file
cp .env.example .env

# Edit .env with your values
```

**Required values:**
- `OPENAI_API_KEY`: Your OpenAI API key
- `DATABASE_URL`: PostgreSQL connection string

### 5. Run Backend
```bash
uvicorn app.main:app --reload
```

**Backend will run on:** `http://127.0.0.1:8000`

**API docs:** `http://127.0.0.1:8000/docs`

---

## 🎨 Frontend Setup

### 1. Navigate to Frontend
```bash
cd frontend
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Configure Environment Variables
```bash
# Copy example env file
cp .env.local.example .env.local

# Edit .env.local with your values
```

**Required values:**
- `NEXT_PUBLIC_API_URL`: Backend URL (default: `http://127.0.0.1:8000`)

### 4. Run Frontend
```bash
npm run dev
```

**Frontend will run on:** `http://localhost:3000`

---

## 🧪 Running Tests

### Backend Tests
```bash
cd backend
pytest tests/ -v
```

### Frontend Tests (if implemented)
```bash
cd frontend
npm test
```

---

## 🗄️ Database Setup

### Option 1: Supabase (Recommended)

1. Create account at [supabase.com](https://supabase.com)
2. Create new project
3. Copy connection string from project settings
4. Add to `backend/.env` as `DATABASE_URL`

### Option 2: Local PostgreSQL

1. Install PostgreSQL
2. Create database: `createdb neurobud`
3. Update `DATABASE_URL` in `backend/.env`

### Option 3: SQLite (Development Only)
```bash
# In backend/.env
DATABASE_URL=sqlite:///./neurobud.db
```

---

## 🐛 Troubleshooting

### Backend won't start

**Error:** `No module named 'app'`
**Solution:** Make sure you're in the `backend` folder with venv activated

**Error:** `Could not connect to database`
**Solution:** Check your `DATABASE_URL` in `.env`

### Frontend won't start

**Error:** `Cannot find module 'next'`
**Solution:** Run `npm install` in frontend folder

**Error:** `API connection failed`
**Solution:** Make sure backend is running and `NEXT_PUBLIC_API_URL` is correct

### Tests failing

**Error:** `Database connection error`
**Solution:** Tests use SQLite, check `conftest.py` exists

---

## 📞 Support

- **GitHub Issues:** [Report a bug](https://github.com/nishanth1104/neurobud/issues)
- **Documentation:** See README.md

---

## ✅ Verify Setup

**Backend:**
```bash
curl http://127.0.0.1:8000
# Should return: {"status":"healthy","service":"Neurobud API","version":"1.0.0"}
```

**Frontend:**
```bash
# Open http://localhost:3000 in browser
# Should see Neurobud landing page
```

**Database:**
```bash
# In backend folder with venv active
python -c "from app.database.connection import engine; print(engine.connect())"
# Should connect without errors
```

---

## 🎉 You're Ready!

Once all checks pass, you're ready to develop!

**Next steps:**
- Read [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines
- Check [API.md](API.md) for API documentation
- See [README.md](README.md) for project overview