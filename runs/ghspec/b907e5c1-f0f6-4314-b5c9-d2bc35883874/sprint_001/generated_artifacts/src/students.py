from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Base

app = Flask(__name__)

# Database setup (assuming SQLite for simplicity)
DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # Create tables
Session = sessionmaker(bind=engine)

@app.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student.
    :return: JSON response with student creation status.
    """
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400

    session = Session()
    new_student = Student(name=data['name'])
    session.add(new_student)
    session.commit()
    session.refresh(new_student)

    return jsonify({"message": "Student created successfully.", "student": {"id": new_student.id, "name": new_student.name}}), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Retrieve a student by ID.
    :param student_id: The ID of the student to retrieve.
    :return: JSON response with student details or error.
    """
    session = Session()
    student = session.query(Student).filter(Student.id == student_id).first()

    if student is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404
    
    return jsonify({"id": student.id, "name": student.name}), 200

@app.route('/students', methods=['GET'])
def list_students():
    """
    List all students.
    :return: JSON response with all students' details.
    """
    session = Session()
    students = session.query(Student).all()
    student_list = [{"id": student.id, "name": student.name} for student in students]

    return jsonify(student_list), 200

if __name__ == '__main__':
    app.run(debug=True)