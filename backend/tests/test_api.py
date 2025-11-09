import pytest

def test_health_check(client):
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "Neurobud API"
    assert data["version"] == "1.0.0"

def test_mood_logging(client):
    """Test mood logging"""
    response = client.post(
        "/api/mood",
        json={"mood_score": 7, "note": "Feeling good today"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["mood_score"] == 7
    assert data["note"] == "Feeling good today"
    assert "created_at" in data
    assert "id" in data

def test_mood_invalid_score_too_high(client):
    """Test mood with score too high"""
    response = client.post(
        "/api/mood",
        json={"mood_score": 15}
    )
    assert response.status_code == 400
    assert "must be between 1 and 10" in response.json()["detail"]

def test_mood_invalid_score_too_low(client):
    """Test mood with score too low"""
    response = client.post(
        "/api/mood",
        json={"mood_score": 0}
    )
    assert response.status_code == 400

def test_mood_history_empty(client):
    """Test mood history when no entries"""
    response = client.get("/api/mood/history?days=7")
    assert response.status_code == 200
    data = response.json()
    assert "entries" in data
    assert isinstance(data["entries"], list)
    assert len(data["entries"]) == 0

def test_mood_history_with_entries(client):
    """Test mood history after logging moods"""
    # Log a mood
    client.post("/api/mood", json={"mood_score": 8, "note": "Great day"})
    client.post("/api/mood", json={"mood_score": 5, "note": "Okay day"})
    
    # Get history
    response = client.get("/api/mood/history?days=7")
    assert response.status_code == 200
    data = response.json()
    assert len(data["entries"]) == 2
    assert data["entries"][0]["mood_score"] in [5, 8]

def test_analytics_endpoint(client):
    """Test analytics endpoint"""
    response = client.get("/api/analytics")
    assert response.status_code == 200
    data = response.json()
    assert "total_conversations" in data
    assert "total_messages" in data
    assert "total_mood_entries" in data
    assert "version" in data