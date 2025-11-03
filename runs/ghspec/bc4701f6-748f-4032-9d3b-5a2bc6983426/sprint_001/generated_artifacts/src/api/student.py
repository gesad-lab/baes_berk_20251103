```python
import json
from flask import Flask, request, jsonify
from your_database_module import initialize_database  # Assuming this function exists in your_database_module

app = Flask(__name__)

@app.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student record.
    Request body must contain a 'name' field.
    """
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name field is required."}}), 400

    # Logic to add the student to the database would go here...

    return jsonify({"message": "Student created successfully.", "student": {"name": name}}), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Retrieve a student record by its ID.
    """
    # Logic to retrieve the student from the database would go here...

    return jsonify({"student": {"id": student_id, "name": "Example Name"}}), 200

if __name__ == '__main__':
    initialize_database()  # Calling the function to set up the database
    app.run(debug=True)
```