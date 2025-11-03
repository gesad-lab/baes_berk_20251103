```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import Teacher  # Assuming the Teacher model is defined in models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Existing endpoints...

@app.route('/api/v1/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """Retrieve teacher details by ID.

    Args:
        teacher_id (int): The ID of the teacher to retrieve.

    Returns:
        Response: JSON object containing teacher details or error message.
    """
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E404", "message": "Teacher not found."}}), 404

    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200

# Existing endpoints continue...
```