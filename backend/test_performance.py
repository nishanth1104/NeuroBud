import time
import requests
import statistics

API_URL = "http://127.0.0.1:8000"

def test_endpoint(endpoint, method="GET", data=None, iterations=10):
    """Test endpoint performance"""
    times = []
    
    print(f"\n🧪 Testing {method} {endpoint}")
    print(f"Iterations: {iterations}")
    
    for i in range(iterations):
        start = time.time()
        
        if method == "GET":
            response = requests.get(f"{API_URL}{endpoint}")
        elif method == "POST":
            response = requests.post(f"{API_URL}{endpoint}", json=data)
        
        duration = (time.time() - start) * 1000
        times.append(duration)
        
        if response.status_code != 200:
            print(f"❌ Request {i+1} failed: {response.status_code}")
    
    # Calculate statistics
    avg = statistics.mean(times)
    median = statistics.median(times)
    p95 = sorted(times)[int(len(times) * 0.95)]
    
    print(f"✅ Average: {avg:.2f}ms")
    print(f"📊 Median: {median:.2f}ms")
    print(f"📈 95th percentile: {p95:.2f}ms")
    
    return {
        "avg": avg,
        "median": median,
        "p95": p95
    }

if __name__ == "__main__":
    print("🚀 Neurobud Performance Tests")
    print("="*50)
    
    # Test health check
    test_endpoint("/", iterations=20)
    
    # Test mood logging
    test_endpoint(
        "/api/mood",
        method="POST",
        data={"mood_score": 7, "note": "Performance test"},
        iterations=10
    )
    
    # Test mood history
    test_endpoint("/api/mood/history?days=7", iterations=10)
    
    # Test analytics
    test_endpoint("/api/analytics", iterations=10)
    
    print("\n✅ Performance tests complete!")