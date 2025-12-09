from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings"""
    
    # App settings
    APP_NAME: str = "AI Calling Agent"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # API settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    
    # OpenAI settings (optional)
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str = "gpt-4"
    OPENAI_TTS_MODEL: str = "tts-1"
    OPENAI_WHISPER_MODEL: str = "whisper-1"
    
    # Twilio settings (optional)
    TWILIO_ACCOUNT_SID: Optional[str] = None
    TWILIO_AUTH_TOKEN: Optional[str] = None
    TWILIO_PHONE_NUMBER: Optional[str] = None
    
    # Database (optional)
    DATABASE_URL: Optional[str] = None
    
    # Redis (optional)
    REDIS_URL: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()