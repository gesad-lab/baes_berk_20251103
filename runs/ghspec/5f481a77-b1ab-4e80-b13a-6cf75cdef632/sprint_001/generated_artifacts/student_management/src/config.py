```python
import os

class Config:
    """Configuration settings for the application."""
    # SQLite database file path
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///students.db')  # Default to sqlite for local development
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disables track modifications for performance
    JSON_SORT_KEYS = False  # Prevents sorting keys in JSON responses for readability
```