from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()

class Student(db.Model):
    """
    Student model for database representation.

    Attributes:
        id (int): Primary key, unique identifier for each student.
        name (str): Name of the student, required field.
        created_at (datetime): Timestamp for when the student was created.
        updated_at (datetime): Timestamp for when the student was last updated.
    """
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)  # Name is a required field
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name})>"
    
def create_database(app):
    """
    Creates the SQLite database and the tables upon application startup.

    Args:
        app: The Flask application instance.
    """
    with app.app_context():
        db.create_all()  # Creates the database tables according to the models defined

# Ensure to call create_database(app) when the application starts to set up the database