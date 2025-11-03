from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Student model definition
class Student(db.Model):
    """Model for Student entity."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Function to create the database and tables
def create_db():
    """Create the database and tables if they do not exist."""
    with app.app_context():
        db.create_all()

# Create the database upon startup
create_db()

# Define entry point for the application
if __name__ == '__main__':
    app.run(debug=True)