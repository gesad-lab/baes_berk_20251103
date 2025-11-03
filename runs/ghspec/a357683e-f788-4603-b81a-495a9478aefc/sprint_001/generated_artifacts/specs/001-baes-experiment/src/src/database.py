from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    """Model representing a student in the database."""
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  # 'name' is required

def create_database_schema():
    """Create the database schema on application startup."""
    db.create_all()

if __name__ == "__main__":
    create_database_schema()
    app.run(debug=True)