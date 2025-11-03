```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, exc

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save memory

# Initialize the SQLAlchemy object with the Flask application
db = SQLAlchemy(app)

class Student(db.Model):
    """Model representing a student."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field
    
    def __init__(self, name: str, email: str):
        """Initialize a new student with name and email."""
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        self.name = name
        self.email = email

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate the email format."""
        # Basic email validation logic (can be improved with regex)
        return isinstance(email, str) and "@" in email and "." in email

@app.before_first_request
def create_tables():
    """Create tables in the database based on the current model."""
    db.create_all()  # This will now include the email column

# Add error handling for when a Student is created with invalid data
@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with name and email."""
    data = request.get_json()
    try:
        name = data['name']
        email = data['email']
        new_student = Student(name=name, email=email)
        db.session.add(new_student)
        db.session.commit()
        return {
            "id": new_student.id,
            "name": new_student.name,
            "email": new_student.email
        }, 201
    except KeyError as e:
        return {"error": {"code": "E001", "message": f"Missing field: {str(e)}"}}, 400
    except ValueError as e:
        return {"error": {"code": "E002", "message": str(e)}}, 400
    except exc.IntegrityError:
        return {"error": {"code": "E003", "message": "Integrity error."}}, 400
    except Exception as e:
        return {"error": {"code": "E004", "message": "An unexpected error occurred."}}, 500
```