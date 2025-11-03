# student_registration/src/config.py

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    """Configuration class to store application settings."""

    # General configurations
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key")
    
    # Database settings
    DATABASE_URI: str = os.getenv("DATABASE_URI", "sqlite:///students.db")

    # Add any other configuration variables needed for your app here

    @classmethod
    def validate(cls):
        """Validate that required configuration variables are set."""
        if not cls.DATABASE_URI:
            raise ValueError("DATABASE_URI is required in configuration.")
        if not cls.SECRET_KEY:
            raise ValueError("SECRET_KEY is required in configuration.")

# Validate configuration on import
Config.validate()