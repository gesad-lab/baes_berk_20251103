```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from models import Student  # Assuming an import from models that contains the Student model
from database import db  # Importing the db instance from database.py
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Automatic database schema creation
with app.app_context():
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new Student."""
    data = request.get_json()
    name = data.get('name')

    # Validate request data
    if not name:
        return jsonify({"error": "Name is required."}), 400

    new_student = Student(name=name)

    try:
        db.session.add(new_student)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "A student with this name already exists."}), 400

    return jsonify({"id": new_student.id, "name": new_student.name}), 201

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """Retrieve a Student by ID."""
    student = Student.query.get(id)

    if not student:
        return jsonify({"error": "Student not found."}), 404

    return jsonify({"id": student.id, "name": student.name}), 200

if __name__ == '__main__':
    app.run(debug=True)
```