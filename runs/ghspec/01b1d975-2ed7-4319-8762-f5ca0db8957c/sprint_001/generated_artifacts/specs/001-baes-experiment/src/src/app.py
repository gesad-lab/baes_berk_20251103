from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Student(db.Model):
    """Represents a student in the database."""
    
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each student
    name = db.Column(db.String(100), nullable=False)  # Student's name, cannot be null

    def __repr__(self):
        """Return a string representation of the Student instance."""
        return f'<Student id={self.id}, name={self.name}>'


@app.before_first_request
def create_tables():
    """Create the database tables based on defined models."""
    db.create_all()  # Create tables for all registered models


if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask application