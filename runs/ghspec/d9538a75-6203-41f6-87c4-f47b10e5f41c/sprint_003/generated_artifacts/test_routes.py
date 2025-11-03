```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Assuming a Course model is defined in models.py
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    level = db.Column(db.String(50), nullable=False)

# Sample API endpoint to create a course
@app.route('/api/v1/courses', methods=['POST'])
def create_course():
    data = request.json
    # Logic to create the course will go here...

@app.route('/api/v1/courses', methods=['GET'])
def get_all_courses():
    """
    Retrieve all courses in JSON format.
    
    Returns:
        JSON response containing a list of all courses with their names and levels.
    """
    try:
        # Fetch all courses from the database
        courses = Course.query.all()
        
        # Convert courses to a list of dictionaries
        course_list = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
        
        return jsonify(course_list), 200  # Return 200 OK with the course list
    except Exception as e:
        # Log the error details (excluding sensitive data)
        print(f"Error occurred while retrieving courses: {str(e)}")
        return jsonify({"error": {"code": "E500", "message": "Failed to retrieve courses."}}), 500  # Internal Server Error

@pytest.mark.parametrize("expected_status", [200])
def test_get_all_courses(client, expected_status):
    # Assuming client is provided for the tests
    response = client.get('/api/v1/courses')
    assert response.status_code == expected_status
    assert isinstance(response.json, list)  # Ensure the response is a list
```