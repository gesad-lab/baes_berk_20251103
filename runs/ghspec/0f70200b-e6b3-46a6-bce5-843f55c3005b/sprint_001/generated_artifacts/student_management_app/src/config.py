import os

class Config:
    """Configuration settings for the Student Management Application."""

    # Database URI for the SQLite database
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///students.db")

    # Debug mode for Flask application
    DEBUG = os.getenv("DEBUG", "False").lower() in ('true', '1', 't')

    # Secret key for Flask application
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")

    # Additional settings can be added here as needed
    # For example, setting up session or logging configurations

def load_config():
    """Load application configuration. Can be expanded for future needs."""
    return Config()