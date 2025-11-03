from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Course  # Assuming Course is defined in models.py
from validation import validate_course_data  # New validation function to be implemented
from migrations import run_migrations  # Migration function to be created

app = Flask(__name__)

# Configure SQLite database
DATABASE_URI = 'sqlite:///your_database.db'  # Update with your actual database URI
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

@app.before_first_request
def initialize_database():
    """Run database migrations and set up the initial state of the database."""
    run_migrations()  # Ensure automatic migrations
    print("Database initialized and migrations applied.")


@app.route('/courses', methods=['POST'])
def create_course():
    """Endpoint to create a new course.

    Returns:
        JSON response with course id, name, and level or error messages.
    """
    data = request.json
    
    # Validate incoming data
    is_valid, errors = validate_course_data(data.get('name'), data.get('level'))
    if not is_valid:
        return jsonify({'errors': errors}), 400

    # Create a new course
    session = Session()
    new_course = Course(name=data['name'], level=data['level'])
    session.add(new_course)
    session.commit()

    return jsonify({'id': new_course.id, 'name': new_course.name, 'level': new_course.level}), 201


@app.route('/courses', methods=['GET'])
def get_courses():
    """Endpoint to retrieve all courses.

    Returns:
        JSON response containing a list of courses.
    """
    session = Session()
    courses = session.query(Course).all()
    return jsonify([{'id': course.id, 'name': course.name, 'level': course.level} for course in courses]), 200


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify application status."""
    return jsonify({'status': 'OK'}), 200


if __name__ == '__main__':
    app.run(debug=True)  # Set debug False for production

# Import necessary modules at the top, and ensure proper organization of your app structure.
# This includes appropriate error handling, validation, and responses according to RESTful principles.