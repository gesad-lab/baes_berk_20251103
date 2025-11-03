from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the SQLAlchemy object
db = SQLAlchemy()
# Initialize the Migrate object for handling database migrations
migrate = Migrate()

class Student(db.Model):
    """
    Student model definition for the application.
    Represents a student with a unique ID and a name.
    """
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

def init_db(app):
    """
    Initialize the database with the application.
    
    Args:
        app: The Flask application instance.
    """
    # Bind the database to the app
    db.init_app(app)
    # Bind the migration to the app
    migrate.init_app(app, db)
    
    # Create the database tables from the schema
    with app.app_context():
        db.create_all()  # This will create the tables based on the defined models

# Note: The init_db function should be called in the main application file
# to ensure the database schema is created upon startup. 
# Example usage: init_db(app)