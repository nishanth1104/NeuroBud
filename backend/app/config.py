# Existing imports...
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Existing settings...
    DATABASE_URL: str
    OPENAI_API_KEY: str
    ENVIRONMENT: str = "development"
    CORS_ORIGINS: str = "http://localhost:3000,http://127.0.0.1:3000"
    
    # Model Configuration
    BASE_MODEL: str = "gpt-4o-mini"
    FINE_TUNED_MODEL_ID: str = ""
    USE_FINE_TUNED_MODEL: bool = False
    AB_TESTING_ENABLED: bool = True
    AB_TEST_SPLIT: float = 0.5
    
    # NEW: OpenAI Pricing (per 1M tokens in USD)
    GPT4O_MINI_INPUT_PRICE: float = 0.150  # $0.150 per 1M input tokens
    GPT4O_MINI_OUTPUT_PRICE: float = 0.600  # $0.600 per 1M output tokens
    
    # Fine-tuned pricing (training + usage)
    FINE_TUNE_TRAINING_PRICE: float = 3.00  # $3.00 per 1M tokens
    FINE_TUNED_INPUT_PRICE: float = 0.150
    FINE_TUNED_OUTPUT_PRICE: float = 0.600
    
    # Embeddings pricing
    EMBEDDING_PRICE: float = 0.020  # $0.020 per 1M tokens (text-embedding-3-small)
    
    # Budget settings
    DAILY_BUDGET_LIMIT: float = 2.00  # $2 per day
    TOTAL_BUDGET: float = 20.00  # $20 total
    ALERT_THRESHOLD: float = 0.75  # Alert at 75% usage
    
    # NextAuth (existing)
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
        extra = "allow"

settings = Settings()