```markdown
# Course Management System

A simple application for managing students and courses, allowing students to enroll in multiple courses and view their course list.

## Main Functions

- **Create Student**: Add a new student to the database.
- **View Students**: Retrieve and display a list of all students.
- **Create Course**: Add a new course to the database.
- **View Courses**: Retrieve and display a list of all courses.
- **Enroll Student in Course**: Enroll a student in a specific course.

## Installation

To set up the Course Management System, you need to install the required dependencies. Follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/course-management.git
   cd course-management
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

4. **Install Tkinter**:
   Tkinter is required for the GUI. It usually comes pre-installed with Python, but if it's not available, you can install it using your system's package manager.

   - For Ubuntu:
     ```bash
     sudo apt-get install python3-tk
     ```

   - For Windows, it should be included with the Python installation.

## How to Use the Application

1. **Run the Application**:
   Start the application by running the following command:
   ```bash
   python main.py
   ```

2. **Creating a Student**:
   - In the GUI, enter the student's name and email.
   - If you want to enroll the student in courses, provide the course IDs in the designated field.
   - Click on "Create Student" to add the student to the database.

3. **Viewing Students**:
   - Click on the "View Students" button to see a list of all registered students.

4. **Creating a Course**:
   - Enter the course name and level in the respective fields.
   - Click on "Create Course" to add the course to the database.

5. **Viewing Courses**:
   - Click on the "View Courses" button to see a list of all available courses.

6. **Enrolling a Student in a Course**:
   - Use the API endpoint `/students/{student_id}/courses/{course_id}` to enroll a student in a specific course.
   - You can do this by sending a POST request with the student ID and course ID.

## Database Migration

The application uses Alembic for database migrations. When you run the application for the first time, it will automatically create the necessary database tables and relationships. The migration script ensures that existing data is preserved during updates.

## Conclusion

This Course Management System provides a simple interface for managing students and courses, allowing for easy enrollment and retrieval of information. For any issues or feature requests, please reach out to the development team.
```