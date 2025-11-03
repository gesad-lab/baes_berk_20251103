```python
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    """Configuration class for environment variables."""
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///students.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Application settings
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
    PORT = int(os.getenv('PORT', 5000))  # Default port to 5000 if not specified

    @classmethod
    def validate(cls):
        """Validate required environment variables."""
        if not cls.SQLALCHEMY_DATABASE_URI:
            raise ValueError("E001: DATABASE_URL is required")
        # Additional validation can be added here

# Run configuration validation to ensure all required variables are set
Config.validate()
```