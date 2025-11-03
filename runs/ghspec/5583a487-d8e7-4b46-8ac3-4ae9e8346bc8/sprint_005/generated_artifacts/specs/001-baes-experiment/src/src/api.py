```
# .env.example

# Flask Configuration
FLASK_APP=app.py
FLASK_ENV=development

# Database Configuration
SQLALCHEMY_DATABASE_URI=sqlite:///app.db
SQLALCHEMY_TRACK_MODIFICATIONS=False

# Teacher Management Configuration
TEACHER_EMAIL_UNIQUE_VALIDATION=true  # This ensures uniqueness for teacher emails
TEACHER_DEFAULT_NAME=Default Teacher    # Default name if none supplied during creation, for testing purposes
```