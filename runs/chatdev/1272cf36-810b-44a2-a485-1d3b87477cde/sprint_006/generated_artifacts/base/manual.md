```markdown
# Teacher Management Application

A simple application for managing students, courses, and teachers. This application allows users to add students and teachers, create courses, and enroll students in courses.

## Main Functions

- **Add Student**: Allows users to register a new student with a name and email.
- **Add Course**: Enables users to create a new course with a name and level.
- **Enroll Student in Course**: Facilitates enrolling a student in a specific course.
- **Add Teacher**: Allows users to register a new teacher with a name and email.
- **View Students, Courses, and Teachers**: Retrieve lists of registered students, courses, and teachers.

## Installation

To run the application, you need to install the required dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/teacher-management-app.git
   cd teacher-management-app
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests tkinter
   ```

4. **Run the Application**:
   ```bash
   uvicorn app:app --reload
   ```

5. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:8000`.

## How to Use the Application

1. **Adding a Student**:
   - Enter the student's name and email in the respective fields.
   - Click on the "Add Student" button to register the student.

2. **Adding a Course**:
   - Enter the course name and level in the respective fields.
   - Click on the "Add Course" button to create the course.

3. **Enrolling a Student in a Course**:
   - Enter the student ID and course ID in the respective fields.
   - Click on the "Enroll Student in Course" button to enroll the student.

4. **Adding a Teacher**:
   - Enter the teacher's name and email in the respective fields.
   - Click on the "Add Teacher" button to register the teacher.

5. **Viewing Students, Courses, and Teachers**:
   - You can retrieve lists of students, courses, and teachers through the respective API endpoints.

## API Endpoints

- **POST /students/**: Create a new student.
- **GET /students/**: Retrieve a list of students.
- **POST /courses/**: Create a new course.
- **GET /courses/**: Retrieve a list of courses.
- **POST /students/{student_id}/courses/{course_id}**: Enroll a student in a course.
- **POST /teachers/**: Create a new teacher.
- **GET /teachers/**: Retrieve a list of teachers.

## Conclusion

This application provides a simple interface for managing educational entities. Feel free to explore the code and modify it according to your needs. For any issues or feature requests, please reach out to the development team.
```