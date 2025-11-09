# 🤝 Contributing to Neurobud

Thank you for your interest in contributing to Neurobud!

---

## 📋 Code of Conduct

Be respectful, inclusive, and professional.

---

## 🐛 Reporting Bugs

**Before submitting:**
1. Check existing issues
2. Use latest version
3. Provide reproduction steps

**Include:**
- OS and version
- Python/Node version
- Error messages
- Steps to reproduce

---

## 💡 Suggesting Features

**Good feature requests include:**
- Clear use case
- Expected behavior
- Why it's valuable

---

## 🔧 Development Setup

See [SETUP.md](SETUP.md) for complete setup instructions.

**Quick start:**
```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

---

## 📝 Coding Standards

### Python (Backend)

- Follow PEP 8
- Use type hints
- Write docstrings
- Max line length: 100 characters

**Example:**
```python
def log_mood(mood_data: MoodRequest, db: Session) -> MoodResponse:
    """
    Log user mood entry.
    
    Args:
        mood_data: Mood request with score and note
        db: Database session
        
    Returns:
        Created mood entry
    """
    # Implementation
```

### JavaScript (Frontend)

- Use ES6+ features
- Prefer functional components
- Use meaningful variable names
- Add comments for complex logic

**Example:**
```javascript
// Load mood history from API
const loadMoodHistory = async () => {
  try {
    const response = await axios.get(...)
    setHistory(response.data.entries)
  } catch (error) {
    console.error('Error loading mood history:', error)
  }
}
```

---

## ✅ Pull Request Process

1. **Fork the repo**
2. **Create branch:** `git checkout -b feature/your-feature`
3. **Make changes**
4. **Write tests**
5. **Run tests:** `pytest tests/ -v`
6. **Commit:** `git commit -m "Add: your feature"`
7. **Push:** `git push origin feature/your-feature`
8. **Open PR**

**PR checklist:**
- [ ] Tests pass
- [ ] Code follows style guide
- [ ] Documentation updated
- [ ] No breaking changes (or documented)

---

## 🧪 Testing

**Run all tests:**
```bash
cd backend
pytest tests/ -v
```

**Write tests for:**
- New endpoints
- New features
- Bug fixes

---

## 📚 Documentation

**Update when adding:**
- New endpoints → `API.md`
- New features → `README.md`
- Setup changes → `SETUP.md`

---

## 🎯 Priority Areas

**High priority:**
- Bug fixes
- Performance improvements
- Security enhancements
- Test coverage

**Medium priority:**
- New features
- UI improvements
- Documentation

**Low priority:**
- Code refactoring
- Minor optimizations

---

## ❓ Questions?

Open a discussion or issue on GitHub.

---

**Thank you for contributing!** 🙏