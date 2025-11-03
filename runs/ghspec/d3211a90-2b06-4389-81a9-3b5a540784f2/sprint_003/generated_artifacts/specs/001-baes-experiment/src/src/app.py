```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Table, Column, MetaData, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)

# Define the base for SQLAlchemy models
Base = declarative_base()

def create_courses_table():
    """
    Create the 'courses' table in the database.
    This function will ensure the table is created without data loss for existing data.
    """
    engine = create_engine('sqlite:///database.db')  # Ensure this matches the existing database path
    metadata = MetaData(bind=engine)

    courses_table = Table('courses', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),
        Column('level', String, nullable=False)
    )

    # Create table if it doesn't exist
    metadata.create_all(engine)

@app.route('/courses', methods=['POST'])
def create_course():
    """
    Create a new Course entity with the provided name and level.
    Expected JSON input format: {"name": "<course_name>", "level": "<course_level>"}
    """
    data = request.json
    
    # Input validation
    if not data.get('name'):
        return jsonify({"error": {"code": "E001", "message": "Name field is required."}}), 400
    if not data.get('level'):
        return jsonify({"error": {"code": "E002", "message": "Level field is required."}}), 400
    
    # Add the course to the database (simulated, actual model not implemented here)
    try:
        # Assuming you have a Course model somewhere
        new_course = Course(name=data['name'], level=data['level'])  # Replace with actual model creation logic
        # session.add(new_course) # Add to the actual database session
        # session.commit()  # Commit changes
        return jsonify({"id": 1, "name": new_course.name, "level": new_course.level}), 201  # Mock response
    except IntegrityError:
        return jsonify({"error": {"code": "E003", "message": "Course already exists."}}), 409

@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """
    Retrieve Course details by ID.
    """
    # Mock retrieving a course, replace with actual database call
    course = {"id": id, "name": "Example Course", "level": "Beginner"}  # Mock response
    
    if course:
        return jsonify(course), 200
    else:
        return jsonify({"error": {"code": "E004", "message": "Course not found."}}), 404

if __name__ == '__main__':
    create_courses_table()  # Ensure the table is created at application startup
    app.run(debug=True)
```