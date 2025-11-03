```python
from flask import Flask, request, jsonify
from models import Student, db

app = Flask(__name__)

@app.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student.

    Request body should contain 'name' and 'email'.
    Responds with a 201 status and a confirmation message on success.
    Responds with a 400 status and an error message if required fields are missing.
    """
    # Get the JSON data from the request
    data = request.get_json()
    
    # Validate input
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "The 'name' and 'email' fields are required."
            }
        }), 400
    
    # Create a new Student instance
    new_student = Student(name=data['name'], email=data['email'])
    
    # Save to the database
    db.session.add(new_student)
    db.session.commit()
    
    # Respond with success message
    return jsonify({
        "message": "Student created successfully.",
        "student_id": new_student.id
    }), 201

@app.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve all students.

    Responds with a JSON array of students, each containing their unique identifier,
    name, and email.
    """
    students = Student.query.all()
    student_list = [{"id": student.id, "name": student.name, "email": student.email} for student in students]
    
    return jsonify(student_list), 200

if __name__ == '__main__':
    app.run(debug=True)
```