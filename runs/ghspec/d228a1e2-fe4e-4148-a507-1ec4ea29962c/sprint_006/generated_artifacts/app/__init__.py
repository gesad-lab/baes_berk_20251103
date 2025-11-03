```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import database models
from app.models import Teacher, Course

# API to assign a teacher to a course
@app.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
def assign_teacher_to_course(course_id):
    # Implementation for assigning teacher to course
    pass

# API to get course details
@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    # Implementation for retrieving course details
    pass

# API to list courses by teacher
@app.route('/teachers/<int:teacher_id>/courses', methods=['GET'])
def list_courses_by_teacher(teacher_id):
    # Implementation for listing courses by teacher
    pass

# Run the application (for development, if needed)
if __name__ == '__main__':
    app.run()
```