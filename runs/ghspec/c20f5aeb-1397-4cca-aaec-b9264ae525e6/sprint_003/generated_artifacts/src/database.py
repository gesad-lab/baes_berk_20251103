```python
# src/database.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.models import Student

# Initialize database and migration instances
db = SQLAlchemy()
migrate = Migrate()

class Course(db.Model):
    """Course model representing a course entity in the database."""
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing ID
    name = db.Column(db.String, nullable=False)    # Course name (required)
    level = db.Column(db.String, nullable=False)   # Course level (required)

def init_db(app):
    """Initialize the database with the Flask application context."""
    db.init_app(app)
    migrate.init_app(app, db)

def migrate_database():
    """Run database migrations to create the Course table."""
    with app.app_context():
        db.create_all()  # This will create all tables, including the new Course table
        # Additional migration logic can be included here

# Example for running the migration process
if __name__ == "__main__":
    from src.app import create_app
    
    app = create_app()
    migrate_database()
```