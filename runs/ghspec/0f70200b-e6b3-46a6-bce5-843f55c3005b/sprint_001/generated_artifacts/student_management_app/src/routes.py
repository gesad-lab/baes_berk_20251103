from flask import Flask, jsonify, request
from models import db, Student

app = Flask(__name__)

# Health check endpoint to verify application status
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify application status."""
    return jsonify({"status": "healthy"}), 200

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with the required name field."""
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name field is required."}}), 400

    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()

    return jsonify(new_student.serialize()), 201

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve a list of all students."""
    students = Student.query.all()
    return jsonify([student.serialize() for student in students]), 200

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """Retrieve a specific student by their ID."""
    student = Student.query.get_or_404(id)
    return jsonify(student.serialize()), 200

if __name__ == '__main__':
    db.create_all()  # Ensure database tables are created on startup
    app.run(debug=True)  # Remove debug=True for production environments