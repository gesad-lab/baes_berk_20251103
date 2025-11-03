```markdown
# Student, Teacher, and Course Management System

A comprehensive application for managing students, teachers, and courses. This software allows users to add and manage students, teachers, and courses, as well as enroll students in courses.

## Main Functions

- **Add Student**: Allows users to input student details (name and email) and add them to the database.
- **View Students**: Fetches and displays a list of all students in the database.
- **Add Teacher**: Allows users to input teacher details (name and email) and add them to the database.
- **View Teachers**: Fetches and displays a list of all teachers in the database.
- **Add Course**: Allows users to input course details (name, level, and teacher ID) and add them to the database.
- **View Courses**: Fetches and displays a list of all courses in the database.
- **Enroll Student in Course**: Allows users to enroll a student in a specific course.

## Installation

To run this application, you need to set up your environment and install the required dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-teacher-course-management.git
   cd student-teacher-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

5. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000` to access the application.

## How to Use the Application

1. **Adding Students**:
   - Enter the student's name and email in the respective fields.
   - Click on "Add Student" to save the information.
   - Click on "Get Students" to view the list of all students.

2. **Adding Teachers**:
   - Enter the teacher's name and email in the respective fields.
   - Click on "Add Teacher" to save the information.
   - Click on "Get Teachers" to view the list of all teachers.

3. **Adding Courses**:
   - Enter the course name, level, and the teacher ID associated with the course.
   - Click on "Add Course" to save the information.
   - Click on "Get Courses" to view the list of all courses.

4. **Enrolling Students in Courses**:
   - Enter the student ID and course ID in the respective fields.
   - Click on "Enroll" to enroll the student in the specified course.

## Database Migration

The application includes a migration script (`migration.py`) to add the Teacher table and the teacher_id column to the Course table while preserving existing data. To run the migration, execute the following command:

```bash
python migration.py
```

This will ensure that your database schema is updated without losing any existing data.

## Conclusion

This application provides a user-friendly interface for managing students, teachers, and courses. By following the installation and usage instructions, you can easily set up and operate the system. For any issues or feature requests, please contact the support team.
```