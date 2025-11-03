```python
# src/main.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from alembic import command
from alembic.config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Assuming the Student model is defined somewhere else
from models import Student  # Adjust according to your file structure

def run_migrations():
    """Run database migrations on application startup."""
    alembic_cfg = Config("alembic.ini")  # Path to alembic configuration file
    with app.app_context():
        command.upgrade(alembic_cfg, "head")  # Upgrade to the latest revision

@app.before_first_request
def setup():
    """Setup tasks that should be run before the first request such as initializing the database."""
    try:
        run_migrations()
        # Additional startup tasks can be executed here if needed
    except Exception as e:
        app.logger.error(f"Failed to run migrations: {str(e)}")
        raise

# Define your API routes and other functionality below
@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student record."""
    # Implementation of create student logic goes here...

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all student records."""
    # Implementation of get all students logic goes here...

if __name__ == "__main__":
    app.run(debug=True)
```