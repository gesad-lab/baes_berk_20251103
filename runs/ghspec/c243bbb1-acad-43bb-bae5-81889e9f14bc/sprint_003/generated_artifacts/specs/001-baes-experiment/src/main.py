```python
# main.py

from flask import Flask
from api.students import students_bp
# Import new courses blueprint for course functionalities
from api.courses import courses_bp  # New import

app = Flask(__name__)

# Register blueprints
app.register_blueprint(students_bp, url_prefix='/api/v1')
# Register courses blueprint
app.register_blueprint(courses_bp, url_prefix='/api/v1/courses')  # New registration

@app.route('/')
def home():
    return "Welcome to the Course Management API!"

if __name__ == '__main__':
    app.run(debug=True)

"""
Project Documentation for Course Functionality

Functional Requirements
1. The application exposes the following API endpoints for the Course entity:
   - **POST `/courses`**: Create a new course.
     - **Request Body**:
       - `name`: string (required)
       - `level`: string (required)
     - **Response**: JSON object including a success message and the created course data.

   - **GET `/courses`**: Retrieve a list of all courses.
     - **Response**: JSON array of course objects, where each object contains a name and level.

2. The application updates the existing database schema on startup to include the new Course table with the following attributes:
   - `id`: int (auto-generated primary key)
   - `name`: string (required)
   - `level`: string (required)

3. The application returns JSON responses for all course-related API requests and performs input validation to ensure that:
   - Both `name` and `level` fields are provided when creating a course.

Assumptions:
- Existing student data remains unaffected by the new course entity and migration.
- Users interacting with the API have a basic understanding of how to send HTTP requests.
- The application will run in a controlled environment where the necessary infrastructure is set up.

Out of Scope:
- User interface for course management; this feature focuses on API functionality.
- Advanced error handling and logging mechanisms are outside the scope of this implementation.
- Integration with external education systems or platforms regarding course content delivery is not included in this scope.

"""
```