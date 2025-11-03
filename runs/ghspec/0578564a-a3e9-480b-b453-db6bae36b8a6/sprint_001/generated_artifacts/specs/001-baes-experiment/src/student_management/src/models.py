```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database URI
DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///students.db')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Create Student model (this will be defined in models.py but can be referenced here to complete the setup)
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
# Create database tables if they don't exist
with app.app_context():
    db.create_all()

# Import routes after app and db creation to avoid circular dependencies
from routes import *

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```