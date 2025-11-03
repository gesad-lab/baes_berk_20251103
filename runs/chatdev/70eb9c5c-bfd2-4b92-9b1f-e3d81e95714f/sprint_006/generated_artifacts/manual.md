```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers effectively. You can create, retrieve, and associate students with courses while also managing teacher assignments.

## Main Functions

- **Student Management**: Create and manage student records.
- **Course Management**: Create and manage courses, including assigning teachers to courses.
- **Teacher Management**: Create and manage teacher records.
- **Student-Course Relationship**: Associate students with courses they are enrolled in.
- **Teacher-Course Relationship**: Assign teachers to courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**:
   Ensure that you have Alembic installed and run the migrations to set up the database schema:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### Accessing the API

Once the application is running, you can access the API at `http://127.0.0.1:8000`. The following endpoints are available:

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of students.

- **Courses**:
  - `POST /courses/`: Create a new course (assign a teacher using `teacher_id`).
  - `GET /courses/`: Retrieve a list of courses.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of teachers.

- **Student-Course Relationship**:
  - `POST /students/{student_id}/courses/`: Enroll a student in a course.

### Example Usage

1. **Create a Teacher**:
   ```json
   POST /teachers/
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

2. **Create a Course**:
   ```json
   POST /courses/
   {
       "name": "Mathematics 101",
       "level": "Beginner",
       "teacher_id": 1  # Assuming the teacher ID is 1
   }
   ```

3. **Create a Student**:
   ```json
   POST /students/
   {
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
   }
   ```

4. **Enroll a Student in a Course**:
   ```json
   POST /students/1/courses/
   {
       "name": "Mathematics 101",
       "level": "Beginner",
       "teacher_id": 1
   }
   ```

## Documentation

For more detailed documentation, including API specifications and examples, please refer to the [API Documentation](https://your-api-docs-url.com).

## Support

If you encounter any issues or have questions, please reach out to our support team at support@chatdev.com.

Thank you for using the ChatDev Course Management System!
```