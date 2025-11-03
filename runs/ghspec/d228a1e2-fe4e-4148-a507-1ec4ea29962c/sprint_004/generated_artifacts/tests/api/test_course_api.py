```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.String, nullable=False)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Define the junction model for StudentCourse relationship
class StudentCourse(db.Model):
    __tablename__ = 'student_courses'
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

# Create the API endpoint to remove a student from a course
@app.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def remove_student_from_course(student_id, course_id):
    enrollment = StudentCourse.query.filter_by(student_id=student_id, course_id=course_id).first()
    
    if not enrollment:
        return jsonify({"error": {"code": "E002", "message": "Enrollment not found"}}), 404
    
    db.session.delete(enrollment)
    db.session.commit()
    
    return jsonify({"message": "Student removed from course successfully"}), 200

# Test Cases
@pytest.fixture()
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Sample data setup
            student = Student(id=1, name='John Doe')
            course = Course(id=1, name='Math 101', level='Beginner')
            db.session.add(student)
            db.session.add(course)
            db.session.commit()
            # Create an enrollment for testing
            enrollment = StudentCourse(student_id=1, course_id=1)
            db.session.add(enrollment)
            db.session.commit()
        yield client

def test_remove_student_from_course_success(client):
    response = client.delete('/students/1/courses/1')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Student removed from course successfully"}

def test_remove_student_from_course_not_found(client):
    response = client.delete('/students/1/courses/2')  # Assuming course with ID 2 does not exist
    assert response.status_code == 404
    assert response.get_json() == {"error": {"code": "E002", "message": "Enrollment not found"}}
```