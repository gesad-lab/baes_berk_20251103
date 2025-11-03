```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src.models import Student, Course  # Assuming Student and Course models exist
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# Fixture to set up a test database session
@pytest.fixture
def db_session():
    """Create a new database session for a test."""
    with app.app_context():
        db.create_all()  # Setup database before tests
        yield db.session
        db.drop_all()  # Cleanup after tests

# Sample data for testing
@pytest.fixture
def sample_data(db_session):
    """Inject sample data into the test database."""
    course1 = Course(id=1, name='Math 101', level='Beginner')
    course2 = Course(id=2, name='History 201', level='Intermediate')
    student1 = Student(id=1, name='Alice')
    student2 = Student(id=2, name='Bob')
    
    db_session.add(course1)
    db_session.add(course2)
    db_session.add(student1)
    db_session.add(student2)
    db_session.commit()
    
    return student1, student2, course1, course2

def test_enroll_student_in_course(db_session, sample_data):
    """Test successful enrollment of a student in a course."""
    student, _, course, _ = sample_data
    
    response = app.test_client().post('/enroll', json={
        'student_id': student.id,
        'course_id': course.id
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Enrollment successful'
    assert data['student_id'] == student.id
    assert data['course_id'] == course.id

def test_enroll_student_in_nonexistent_course(db_session, sample_data):
    """Test attempting to enroll a student in a non-existent course."""
    student, _, _, _ = sample_data
    
    response = app.test_client().post('/enroll', json={
        'student_id': student.id,
        'course_id': 999  # Non-existent course ID
    })
    
    assert response.status_code == 400
    data = response.get_json()
    assert data['error']['code'] == 'E001'
    assert data['error']['message'] == 'Invalid course ID'

def test_retrieve_courses_for_student(db_session, sample_data):
    """Test retrieving courses for a specific student."""
    student, _, course, _ = sample_data
    db_session.execute('INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)', (student.id, course.id))
    db_session.commit()
    
    response = app.test_client().get(f'/students/{student.id}/courses')
    
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['course_id'] == course.id
    assert data[0]['name'] == course.name
    assert data[0]['level'] == course.level

def test_remove_student_from_course(db_session, sample_data):
    """Test removing a student from a specific course."""
    student, _, course, _ = sample_data
    db_session.execute('INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)', (student.id, course.id))
    db_session.commit()
    
    response = app.test_client().delete('/enroll', json={
        'student_id': student.id,
        'course_id': course.id
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Removal successful'

def test_remove_student_from_nonexistent_course(db_session, sample_data):
    """Test attempting to remove a student from a non-existent course."""
    student, _, _, _ = sample_data
    
    response = app.test_client().delete('/enroll', json={
        'student_id': student.id,
        'course_id': 999  # Non-existent course ID
    })
    
    assert response.status_code == 400
    data = response.get_json()
    assert data['error']['code'] == 'E001'
    assert data['error']['message'] == 'Invalid course ID'
```