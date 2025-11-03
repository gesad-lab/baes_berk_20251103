```markdown
# Student Course Management System

A comprehensive application for managing students, courses, and teachers, allowing users to create, retrieve, and manage relationships between these entities.

## Main Functions

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records, including associating courses with teachers.
- **Teacher Management**: Create and retrieve teacher records.
- **Enrollment**: Enroll students in courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi sqlalchemy uvicorn
   ```

4. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

Once the application is running, you can interact with it through the API or a GUI (if implemented). Below are examples of how to use the API endpoints.

### API Endpoints

1. **Create a Student**:
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

2. **Retrieve All Students**:
   - **Endpoint**: `GET /students/`

3. **Create a Teacher**:
   - **Endpoint**: `POST /teachers/`
   - **Request Body**:
     ```json
     {
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
     }
     ```

4. **Retrieve All Teachers**:
   - **Endpoint**: `GET /teachers/`

5. **Create a Course**:
   - **Endpoint**: `POST /courses/`
   - **Request Body**:
     ```json
     {
       "name": "Mathematics 101",
       "level": "Beginner",
       "teacher_id": 1  // ID of the teacher associated with the course
     }
     ```

6. **Retrieve All Courses**:
   - **Endpoint**: `GET /courses/`

7. **Enroll a Student in a Course**:
   - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
   - **Path Parameters**:
     - `student_id`: ID of the student
     - `course_id`: ID of the course

### Example Usage with cURL

- **Create a Student**:
  ```bash
  curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
  ```

- **Create a Teacher**:
  ```bash
  curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "Jane Smith", "email": "jane.smith@example.com"}'
  ```

- **Create a Course**:
  ```bash
  curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics 101", "level": "Beginner", "teacher_id": 1}'
  ```

- **Enroll a Student in a Course**:
  ```bash
  curl -X POST "http://127.0.0.1:8000/students/1/courses/1"
  ```

## Database Migration

The application includes a migration feature that ensures the database schema is updated to support the new teacher relationship in the course entity while preserving existing data. The migration process is handled automatically when the application starts.

## Conclusion

This Student Course Management System provides a robust framework for managing educational entities and their relationships. For further customization or feature requests, please contact the development team.
```