```python
from flask import Flask, request, jsonify
from src.services import create_teacher, get_teacher_by_id
from src.models import Teacher

app = Flask(__name__)

@app.route('/teachers', methods=['POST'])
def create_teacher_endpoint():
    """
    Create a new teacher profile from provided JSON data.
    
    Expects a JSON body containing 'name' and 'email'.
    Returns the created teacher's details.
    """
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400

    try:
        new_teacher = create_teacher(name, email)
        return jsonify({"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}), 201
    except ValueError as e:
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 400

@app.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher_endpoint(teacher_id):
    """
    Retrieve details of a teacher given their unique ID.
    
    Returns the teacher's 'id', 'name', and 'email'.
    """
    teacher = get_teacher_by_id(teacher_id)
    
    if not teacher:
        return jsonify({"error": {"code": "E003", "message": "Teacher not found."}}), 404

    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email})

if __name__ == '__main__':
    app.run(debug=True)
```