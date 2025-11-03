```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.student import Base, Student  # Assuming the Student model and Base are defined in models/student.py

app = Flask(__name__)

DATABASE_URL = 'sqlite:///students.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def initialize_database():
    """Create the database tables if they do not already exist."""
    Base.metadata.create_all(engine)

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student record."""
    data = request.get_json()
    name = data.get('name')
    
    if not name:
        return jsonify({'error': {'code': 'E001', 'message': 'The name field is required.'}}), 400
    
    session = Session()
    new_student = Student(name=name)
    session.add(new_student)
    session.commit()
    
    return jsonify({'message': 'Student created successfully.', 'student': {'id': new_student.id, 'name': new_student.name}}), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a student's details."""
    session = Session()
    student = session.query(Student).filter(Student.id == student_id).first()
    
    if student is None:
        return jsonify({'error': {'code': 'E002', 'message': 'Student not found.'}}), 404
    
    return jsonify({'id': student.id, 'name': student.name}), 200

if __name__ == '__main__':
    initialize_database()  # Initialize the database
    app.run(debug=True)  # Start the Flask application
```