```markdown
# Student Management System

A comprehensive application for managing students and their course enrollments.

## Main Functions

The Student Management System allows users to:

- **Add Students**: Create new student profiles by entering their name and email.
- **View Students**: Retrieve and display a list of all registered students.
- **Add Courses**: Create new courses by specifying the course name and level.
- **View Courses**: Retrieve and display a list of all available courses.
- **Enroll Students in Courses**: Enroll a student in a specific course using their ID and the course ID.
- **View Student Courses**: Retrieve and display all courses a specific student is enrolled in.

## Installation

To set up the environment and run the application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-management-system.git
   cd student-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure you have Python 3.7 or higher installed. Then, install the required dependencies using pip:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migration commands:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the application using Uvicorn:
   ```bash
   python main.py
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

## How to Use the Application

1. **Adding a Student**:
   - Enter the student's name and email in the respective fields.
   - Click on the "Add Student" button to create a new student profile.

2. **Viewing Students**:
   - Click on the "Show Students" button to display a list of all registered students.

3. **Adding a Course**:
   - Enter the course name and level in the respective fields.
   - Click on the "Add Course" button to create a new course.

4. **Viewing Courses**:
   - Click on the "Show Courses" button to display a list of all available courses.

5. **Enrolling a Student in a Course**:
   - Enter the Student ID and Course ID in the enrollment section.
   - Click on the "Enroll" button to enroll the student in the specified course.

6. **Viewing Student Courses**:
   - To view the courses a specific student is enrolled in, you can implement a similar functionality as shown in the code, or extend the GUI to include this feature.

## Conclusion

This Student Management System provides a user-friendly interface for managing students and their course enrollments. With the ability to add, view, and enroll students in courses, it serves as a valuable tool for educational institutions.

For further assistance or feature requests, please contact the development team.
```