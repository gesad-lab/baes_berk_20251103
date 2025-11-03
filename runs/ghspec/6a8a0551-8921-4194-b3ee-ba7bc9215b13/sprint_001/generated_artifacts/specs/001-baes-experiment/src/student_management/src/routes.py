```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """Retrieve a student by ID."""
    student = Student.query.get(id)
    if student is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404
    return jsonify({"id": student.id, "name": student.name}), 200

# Initialize database
with app.app_context():
    db.create_all()
```