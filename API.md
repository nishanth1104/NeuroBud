# 📚 Neurobud API Documentation

Complete API reference for Neurobud backend.

**Base URL:** `http://127.0.0.1:8000` (development)

---

## 📋 Table of Contents

- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [Health Check](#health-check)
  - [Chat](#chat)
  - [Mood Tracking](#mood-tracking)
  - [Analytics](#analytics)
- [Error Handling](#error-handling)
- [Rate Limiting](#rate-limiting)

---

## 🔐 Authentication

**Current:** No authentication required (anonymous usage)

**Coming in Week 2:** OAuth 2.0 (Google, GitHub)

---

## 🔗 Endpoints

### Health Check

**GET** `/`

Check if API is running.

**Response:**
```json
{
  "status": "healthy",
  "service": "Neurobud API",
  "version": "1.0.0"
}
```

---

### Chat

**POST** `/api/chat`

Send a message to the AI chatbot.

**Rate Limit:** 20 requests/minute

**Request Body:**
```json
{
  "message": "I'm feeling anxious today",
  "conversation_id": 1  // Optional, omit for new conversation
}
```

**Response:**
```json
{
  "conversation_id": 1,
  "message": "I'm feeling anxious today",
  "response": "I hear you - anxiety can feel overwhelming...",
  "is_crisis": false,
  "crisis_severity": null,
  "tokens_used": 150,
  "response_time_ms": 1234.56
}
```

**Crisis Detection Response:**
```json
{
  "conversation_id": 2,
  "message": "I don't want to live anymore",
  "response": "🆘 I'm really concerned... Call 988...",
  "is_crisis": true,
  "crisis_severity": "critical",
  "tokens_used": 80,
  "response_time_ms": 0
}
```

**Validation:**
- `message`: Required, 2-2000 characters
- `conversation_id`: Optional integer

**Errors:**
- `400`: Invalid message (empty, too long)
- `404`: Conversation not found
- `429`: Rate limit exceeded
- `500`: Server error

---

### Mood Tracking

#### Log Mood

**POST** `/api/mood`

Log a mood entry.

**Rate Limit:** 10 requests/minute

**Request Body:**
```json
{
  "mood_score": 7,
  "note": "Had a good workout today"  // Optional
}
```

**Response:**
```json
{
  "id": 1,
  "mood_score": 7,
  "note": "Had a good workout today",
  "created_at": "2025-01-08T10:30:00Z"
}
```

**Validation:**
- `mood_score`: Required, integer 1-10
- `note`: Optional, max 500 characters

**Errors:**
- `400`: Invalid mood score (not 1-10)
- `429`: Rate limit exceeded

---

#### Get Mood History

**GET** `/api/mood/history?days=7`

Get mood history for past X days.

**Query Parameters:**
- `days`: Number of days (default: 30, max: 365)

**Response:**
```json
{
  "entries": [
    {
      "id": 1,
      "mood_score": 7,
      "note": "Had a good workout today",
      "created_at": "2025-01-08T10:30:00Z"
    }
  ]
}
```

---

### Analytics

**GET** `/api/analytics`

Get system analytics and metrics.

**Response:**
```json
{
  "total_conversations": 150,
  "total_messages": 842,
  "total_mood_entries": 234,
  "total_crisis_events": 12,
  "conversations_last_24h": 23,
  "avg_mood_last_7d": 6.8,
  "uptime": "99.9%",
  "version": "1.0.0"
}
```

---

## ⚠️ Error Handling

All errors return JSON with this structure:
```json
{
  "error": "Error Type",
  "message": "Human-readable error message",
  "detail": "Technical details (optional)"
}
```

**Common Status Codes:**
- `200`: Success
- `400`: Bad Request (invalid input)
- `404`: Not Found
- `422`: Validation Error
- `429`: Rate Limit Exceeded
- `500`: Internal Server Error

---

## ⏱️ Rate Limiting

**Limits:**
- Chat: 20 requests/minute per IP
- Mood: 10 requests/minute per IP
- Other endpoints: No limit

**Rate limit response (429):**
```json
{
  "error": "Rate limit exceeded: 20 per 1 minute"
}
```

**Headers:**
- `X-RateLimit-Limit`: Max requests per window
- `X-RateLimit-Remaining`: Requests remaining
- `X-RateLimit-Reset`: Time until limit resets

---

## 🧪 Testing the API

### Using cURL
```bash
# Health check
curl http://127.0.0.1:8000

# Chat
curl -X POST http://127.0.0.1:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello"}'

# Log mood
curl -X POST http://127.0.0.1:8000/api/mood \
  -H "Content-Type: application/json" \
  -d '{"mood_score":8,"note":"Great day!"}'

# Get analytics
curl http://127.0.0.1:8000/api/analytics
```

### Using Swagger UI

Interactive API documentation:
```
http://127.0.0.1:8000/docs
```

---

## 📊 Response Times

**Target latencies:**
- Health check: <10ms
- Chat (crisis): <100ms (no AI call)
- Chat (normal): <3000ms (includes AI)
- Mood logging: <100ms
- Analytics: <200ms

---

## 🔄 Versioning

**Current version:** 1.0.0

**Breaking changes:** Will increment major version (2.0.0)

**New features:** Will increment minor version (1.1.0)

**Bug fixes:** Will increment patch version (1.0.1)

---

## 📞 Support

**Issues:** [GitHub Issues](https://github.com/nishanth1104/neurobud/issues)

**Questions:** See [SETUP.md](SETUP.md) or [README.md](README.md)