```python
from flask import Flask, request, jsonify
from models import Teacher
from services import TeacherService
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Make sure to configure your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TeacherService:
    """Service layer for handling Teacher operations."""
    
    @staticmethod
    def create_teacher(name: str, email: str):
        """Creates a new Teacher and saves it to the database."""
        teacher = Teacher(name=name, email=email)
        db.session.add(teacher)
        db.session.commit()
        return teacher

@app.route('/teachers', methods=['POST'])
def create_teacher():
    """Endpoint to create a new Teacher."""
    data = request.get_json()

    # Validate input data
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Name and email are required."
            }
        }), 400

    name = data['name']
    email = data['email']

    try:
        # Create teacher through the service layer
        teacher = TeacherService.create_teacher(name, email)

        return jsonify({
            "message": "Teacher created successfully.",
            "teacher": {
                "id": teacher.id,
                "name": teacher.name,
                "email": teacher.email
            }
        }), 201
    except IntegrityError:
        db.session.rollback()  # Rollback the session on error
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Email already exists."
            }
        }), 400
    except Exception as e:
        db.session.rollback()  # Rollback on any unexpected error
        return jsonify({
            "error": {
                "code": "E003",
                "message": str(e)
            }
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
```