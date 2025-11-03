```python
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///courses.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Course model for migration and database management
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Course {self.name}, Level {self.level}>'

@app.route('/courses', methods=['POST'])
def create_course():
    """
    Create a new course record.
    
    Request JSON should contain:
      - name (str): Course name
      - level (str): Course level
      
    Returns:
      - JSON object with confirmation or error message
      - HTTP status code 201 for created or 400 for bad request
    """
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'level' not in data:
        return jsonify({"error": {"code": "E001", "message": "Both name and level fields are required."}}), 400

    name = data['name']
    level = data['level']

    # Create course instance
    new_course = Course(name=name, level=level)

    # Add to session and commit
    db.session.add(new_course)
    db.session.commit()

    return jsonify({"message": "Course created successfully."}), 201

@app.route('/courses', methods=['GET'])
def get_courses():
    """
    Retrieve all course records.

    Returns:
      - List of courses in JSON format
      - HTTP status code 200
    """
    courses = Course.query.all()
    return jsonify([{"name": course.name, "level": course.level} for course in courses]), 200

if __name__ == '__main__':
    # Run application with migration applied at startup
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
```