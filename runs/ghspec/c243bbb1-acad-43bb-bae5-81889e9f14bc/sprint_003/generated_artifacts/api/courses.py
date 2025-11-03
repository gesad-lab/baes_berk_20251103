```python
# api/courses.py

from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
from sqlalchemy.exc import IntegrityError

courses_bp = Blueprint('courses', __name__)

# Database setup - adjust connection as needed
engine = create_engine('sqlite:///courses.db')
metadata = MetaData(bind=engine)

# Define the courses table
courses_table = Table('courses', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('level', String, nullable=False)
)

# Create the courses table in the database if it doesn't exist
metadata.create_all(engine)

@courses_bp.route('/courses', methods=['POST'])
def create_course():
    """Create a new course in the database."""
    data = request.get_json()

    # Validate presence of 'name' and 'level' fields
    name = data.get('name')
    level = data.get('level')
    if not name or not level:
        return jsonify({"error": {"code": "E001", "message": "Both 'name' and 'level' are required."}}), 400

    # Attempt to insert the new course into the database
    try:
        with engine.connect() as conn:
            result = conn.execute(courses_table.insert().values(name=name, level=level))
            new_course = {
                "id": result.inserted_primary_key[0],
                "name": name,
                "level": level
            }
            return jsonify({"message": "Course created successfully.", "course": new_course}), 201
    except IntegrityError as e:
        return jsonify({"error": {"code": "E002", "message": "Database error: " + str(e)} }), 500

@courses_bp.route('/courses', methods=['GET'])
def get_courses():
    """Retrieve a list of all courses."""
    try:
        with engine.connect() as conn:
            result = conn.execute(courses_table.select())
            courses = [{"id": row['id'], "name": row['name'], "level": row['level']} for row in result]
            return jsonify(courses), 200
    except Exception as e:
        return jsonify({"error": {"code": "E003", "message": "An error occurred while retrieving courses."}}), 500
```