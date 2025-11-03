```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration settings."""

    # Basic Flask settings
    FLASK_ENV = os.getenv("FLASK_ENV", "development")  # Set to 'production' or 'development'
    DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "t")  # Boolean environment variable for debug mode

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///./test.db")  # Default to SQLite for testing
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # To suppress a warning from SQLAlchemy

    # Other configurations can be added as needed
```