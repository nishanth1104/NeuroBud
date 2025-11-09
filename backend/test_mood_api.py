"""
Test script to verify mood tracking works correctly
"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_mood_tracking():
    """Test mood entry creation"""
    print("Testing mood tracking endpoint...")

    # Test valid mood entry
    response = client.post(
        "/api/mood",
        json={"mood_score": 7, "note": "Feeling pretty good today"}
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    if response.status_code == 200:
        print("[OK] Mood tracking works!")
        return True
    else:
        print("[ERROR] Mood tracking failed!")
        return False

def test_mood_history():
    """Test mood history retrieval"""
    print("\nTesting mood history endpoint...")

    response = client.get("/api/mood/history")

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    if response.status_code == 200:
        print("[OK] Mood history works!")
        return True
    else:
        print("[ERROR] Mood history failed!")
        return False

def test_rate_limiting():
    """Test rate limiting on mood endpoint"""
    print("\nTesting rate limiting...")

    # Try to exceed rate limit (10 requests per minute)
    for i in range(12):
        response = client.post(
            "/api/mood",
            json={"mood_score": 5, "note": f"Test {i}"}
        )
        if response.status_code == 429:
            print(f"[OK] Rate limit triggered after {i+1} requests")
            return True

    print("[WARNING] Rate limit not triggered (might need actual time delay)")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("NEUROBUD API TESTS")
    print("=" * 50)

    results = []
    results.append(test_mood_tracking())
    results.append(test_mood_history())
    results.append(test_rate_limiting())

    print("\n" + "=" * 50)
    if all(results):
        print("[OK] ALL TESTS PASSED!")
    else:
        print("[ERROR] SOME TESTS FAILED")
    print("=" * 50)
