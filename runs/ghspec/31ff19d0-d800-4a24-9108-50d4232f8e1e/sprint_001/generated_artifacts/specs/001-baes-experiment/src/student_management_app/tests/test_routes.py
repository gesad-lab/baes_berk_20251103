```python
import os

class Config:
    """Application configuration settings."""
    
    # General settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')  # Default secret key for sessions
    DEBUG = os.getenv('FLASK_DEBUG', 'false').lower() in ['true', '1']  # Enable/disable debug mode

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///students.db')  # Default to SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking

# Optionally, you can enable different configurations based on the environment
class DevelopmentConfig(Config):
    """Development specific configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production specific configuration."""
    DEBUG = False

# Here we define a way to get the appropriate config based on the environment
def get_config():
    """Get the appropriate config class based on the environment."""
    env = os.getenv('FLASK_ENV', 'development')
    if env == 'production':
        return ProductionConfig
    return DevelopmentConfig
```