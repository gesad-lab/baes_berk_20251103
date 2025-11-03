from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Model for the Student
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create the database tables on startup
with app.app_context():
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student."""
    data = request.get_json()
    name = data.get('name')
    
    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400

    new_student = Student(name=name)
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify({"id": new_student.id, "name": new_student.name}), 201

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all registered students."""
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    """Update the name of a student."""
    student = Student.query.get(id)
    if student is None:
        abort(404)

    data = request.get_json()
    name = data.get('name')
    
    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400

    student.name = name
    db.session.commit()
    
    return jsonify({"id": student.id, "name": student.name}), 200

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    """Delete a student."""
    student = Student.query.get(id)
    if student is None:
        abort(404)

    db.session.delete(student)
    db.session.commit()
    
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)