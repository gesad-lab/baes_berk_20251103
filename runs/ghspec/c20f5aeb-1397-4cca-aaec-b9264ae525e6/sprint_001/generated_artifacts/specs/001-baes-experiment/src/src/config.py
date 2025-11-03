```python
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    """Configuration settings for the application."""
    
    # Database URI configuration
    DATABASE_URI: str = os.getenv('DATABASE_URI', 'sqlite:///default.db')
    
    # Example of additional configurations that might be included
    DEBUG: bool = os.getenv('DEBUG', 'false').lower() in ('true', '1', 't')
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'default_secret_key')

    @classmethod
    def validate(cls):
        """Validate required configuration values."""
        if not cls.DATABASE_URI:
            raise ValueError("E001: DATABASE_URI is required.")
        if cls.DEBUG not in [True, False]:
            raise ValueError("E002: DEBUG must be 'true' or 'false'.")
        if not cls.SECRET_KEY:
            raise ValueError("E003: SECRET_KEY is required.")

# Validate configuration at startup
Config.validate()
```