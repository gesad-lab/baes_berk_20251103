```markdown
# Student Course Management System

A comprehensive application for managing students, courses, and teachers, allowing for easy registration, enrollment, and relationship management.

## Main Functions

- **Add Student**: Register a new student by providing their name and email.
- **Add Course**: Create a new course by specifying its name, level, and associated teacher.
- **Enroll Student in Course**: Enroll a student in a specific course.
- **Add Teacher**: Register a new teacher by providing their name and email.
- **View Students, Courses, and Teachers**: Retrieve and display lists of registered students, courses, and teachers.

## Installation

To run the application, you need to set up the environment and install the required dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-course-management.git
   cd student-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests tkinter
   ```

4. **Initialize the Database**:
   Run the following command to create the database schema:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

## How to Use the Application

1. **Run the FastAPI Server**:
   Start the FastAPI application by running:
   ```bash
   uvicorn app:app --reload
   ```

2. **Launch the GUI**:
   In a separate terminal, run the GUI application:
   ```bash
   python gui.py
   ```

3. **Using the GUI**:
   - **Add Student**: Enter the student's name and email, then click "Add Student".
   - **Add Course**: Enter the course name, level, and teacher ID, then click "Add Course".
   - **Enroll Student in Course**: Enter the student ID and course ID, then click "Enroll Student in Course".
   - **Add Teacher**: Enter the teacher's name and email, then click "Add Teacher".

4. **View Data**:
   You can view the lists of students, courses, and teachers by accessing the respective endpoints in your browser or using a tool like Postman:
   - Students: `http://127.0.0.1:8000/students/`
   - Courses: `http://127.0.0.1:8000/courses/`
   - Teachers: `http://127.0.0.1:8000/teachers/`

## Conclusion

This application provides a user-friendly interface for managing students, courses, and teachers, making it easier for educational institutions to handle their administrative tasks efficiently. For further assistance, please refer to the code documentation or contact support.
```