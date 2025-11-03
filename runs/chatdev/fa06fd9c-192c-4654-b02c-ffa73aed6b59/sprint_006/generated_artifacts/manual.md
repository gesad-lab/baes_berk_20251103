```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. You can create, read, and update entities while maintaining relationships between them.

## Main Functions

- **Student Management**: Create and manage student records.
- **Course Management**: Create and manage courses, including assigning teachers to courses.
- **Teacher Management**: Create and manage teacher records.
- **Enrollment**: Enroll students in courses.
- **API Endpoints**: Interact with the system through RESTful API endpoints.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy
   ```

4. **Initialize the Database**:
   Run the following command to create the necessary tables:
   ```bash
   python main.py
   ```

## How to Use the Software

### Starting the Server

To start the FastAPI server, run the following command:
```bash
uvicorn routes:router --reload
```
This will start the server on `http://127.0.0.1:8000`.

### API Endpoints

Here are the available API endpoints you can use:

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of all students.

- **Courses**:
  - `POST /courses/`: Create a new course (optionally assign a teacher).
  - `GET /courses/`: Retrieve a list of all courses.
  - `PUT /courses/{course_id}/assign_teacher/{teacher_id}/`: Assign a teacher to a course.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of all teachers.

- **Enrollment**:
  - `POST /students/{student_id}/courses/{course_id}/`: Enroll a student in a course.

### Example Usage

1. **Creating a Teacher**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}'
   ```

2. **Creating a Course**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner", "teacher_id": 1}'
   ```

3. **Enrolling a Student in a Course**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/students/1/courses/1/"
   ```

## Conclusion

The ChatDev Course Management System is designed to streamline the management of educational entities. With the provided API endpoints, you can easily manage students, courses, and teachers, ensuring a smooth educational experience.

For further assistance, please refer to the documentation or contact our support team.
```