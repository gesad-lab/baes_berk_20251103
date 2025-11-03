import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for the Student Management Web Application."""
    
    # Database configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///students.db")
    
    # Debugging mode
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

    # Define any additional application settings here
    # For instance, secret keys, CORS settings, etc.
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")  # Change in production
    
    @staticmethod
    def validate_config():
        """Validate that required configuration variables are set."""
        if not os.getenv("DATABASE_URL"):
            raise ValueError("DATABASE_URL environment variable is required.")
        if not os.getenv("SECRET_KEY"):
            raise ValueError("SECRET_KEY environment variable is required.")

# Example usage
# To use this configuration in your application, you can import it like:
# from config import Config
# and then access configuration settings as follows:
# db_url = Config.DATABASE_URL
# debug_mode = Config.DEBUG

# Ensure configuration is valid
Config.validate_config()