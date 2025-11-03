```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers. This system allows users to add and view students, courses, and teachers, ensuring a smooth management experience.

## Main Functions

- **Add Student**: Allows users to input student details (name and email) and save them to the database.
- **View Students**: Displays a list of all students currently in the database.
- **Add Course**: Enables users to create new courses by specifying the course name and level.
- **View Courses**: Lists all courses available in the system.
- **Enroll Student in Course**: Facilitates the enrollment of students in selected courses.
- **Add Teacher**: Users can add new teachers by providing their name and email.
- **View Teachers**: Displays a list of all teachers in the system.

## Installation

To run the Teacher Management System, you need to set up the environment and install the necessary dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure you have `pip` installed, then run:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migration**:
   Ensure that the database schema is up to date by running the migration script:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the application using:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

1. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:8000`.

2. **Adding Students**:
   - Enter the student's name and email in the respective fields.
   - Click on the "Add Student" button to save the information.

3. **Viewing Students**:
   - Click on the "View Students" button to see a list of all students.

4. **Adding Courses**:
   - Fill in the course name and level.
   - Click on the "Add Course" button to create the course.

5. **Viewing Courses**:
   - Click on the "View Courses" button to see all available courses.

6. **Enrolling Students in Courses**:
   - Select a student from the list and a course from the courses list.
   - Click on the "Enroll Student in Course" button to enroll the selected student.

7. **Adding Teachers**:
   - Enter the teacher's name and email in the respective fields.
   - Click on the "Add Teacher" button to save the teacher's information.

8. **Viewing Teachers**:
   - Click on the "View Teachers" button to see a list of all teachers.

## Conclusion

The Teacher Management System is designed to simplify the management of students, courses, and teachers. By following the installation and usage instructions, you can easily set up and operate the application. For further assistance, feel free to reach out for support.
```