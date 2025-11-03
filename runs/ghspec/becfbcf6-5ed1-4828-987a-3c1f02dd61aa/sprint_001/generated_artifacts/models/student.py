```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save memory

# Initialize the SQLAlchemy object with the Flask application
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    """Create tables in the database based on the defined models."""
    db.create_all()
```