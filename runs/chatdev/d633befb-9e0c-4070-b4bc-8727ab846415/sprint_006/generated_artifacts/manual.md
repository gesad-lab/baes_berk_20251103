```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. You can create and manage relationships between these entities, making it easier to handle educational data.

## Main Functions

1. **Student Management**: Add, view, and manage student information.
2. **Course Management**: Create and manage courses, including assigning teachers to courses.
3. **Teacher Management**: Add and manage teacher information.
4. **Enrollment**: Enroll students in courses and manage their course selections.

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
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migrations**:
   To set up the database schema, run the following command:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application using:
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API Documentation**:
   Open your browser and go to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## How to Use the Application

### Adding a Student

1. Navigate to the "Student" section in the GUI.
2. Enter the student's name and email.
3. Click the "Add Student" button to create a new student record.

### Adding a Teacher

1. Navigate to the "Teacher" section in the GUI.
2. Enter the teacher's name and email.
3. Click the "Add Teacher" button to create a new teacher record.

### Adding a Course

1. Navigate to the "Course" section in the GUI.
2. Enter the course name, level, and the teacher ID (ensure the teacher exists).
3. Click the "Add Course" button to create a new course record.

### Enrolling a Student in a Course

1. Navigate to the "Enrollment" section in the GUI.
2. Enter the student ID and the course ID.
3. Click the "Enroll" button to enroll the student in the specified course.

## Database Schema

The application uses SQLite as the database backend. The schema includes three main entities:

- **Students**: Contains student information and their enrolled courses.
- **Courses**: Contains course details and the associated teacher.
- **Teachers**: Contains teacher information and the courses they teach.

## Conclusion

This Course Management System is designed to simplify educational administration tasks. By following the instructions above, you can set up and start using the application effectively. For further assistance or feature requests, please contact our support team.

Happy managing!
```