import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Log all API requests and responses"""
    
    async def dispatch(self, request: Request, call_next):
        # Start timer
        start_time = time.time()
        
        # Log request
        print(f"\n{'='*50}")
        print(f"📥 {request.method} {request.url.path}")
        print(f"Client: {request.client.host}")
        
        # Process request
        response = await call_next(request)
        
        # Calculate duration
        duration = (time.time() - start_time) * 1000
        
        # Log response
        print(f"📤 Status: {response.status_code}")
        print(f"⏱️  Duration: {duration:.2f}ms")
        print(f"{'='*50}\n")
        
        # Add custom header with response time
        response.headers["X-Response-Time"] = f"{duration:.2f}ms"
        
        return response