from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    
    # OpenAI
    OPENAI_API_KEY: str
    
    # Application
    ENVIRONMENT: str = "development"
    CORS_ORIGINS: str = "http://localhost:3000,http://127.0.0.1:3000"
    
    # Model Configuration (A/B Testing)
    BASE_MODEL: str = "gpt-4o-mini"
    FINE_TUNED_MODEL_ID: str = ""
    USE_FINE_TUNED_MODEL: bool = False
    AB_TESTING_ENABLED: bool = True
    AB_TEST_SPLIT: float = 0.5
    
    # NextAuth (Frontend only - backend doesn't need these)
    # These are allowed but not used by backend
    NEXTAUTH_URL: str = ""
    NEXTAUTH_SECRET: str = ""
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    GITHUB_ID: str = ""
    GITHUB_SECRET: str = ""
    
    @property
    def cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]
    
    class Config:
        env_file = ".env"
        extra = "allow"  # Allow extra fields from .env

settings = Settings()