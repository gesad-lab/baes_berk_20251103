```markdown
# Student Management Application

A comprehensive application for managing student and course information, built using Python and FastAPI. This application allows users to add, fetch, and manage student and course data through a user-friendly graphical interface.

## Main Functions

- **Student Management**: Add new students with their names and email addresses, and fetch the list of existing students.
- **Course Management**: Create new courses by specifying the course name and level, and manage course data.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-management.git
   cd student-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Use pip to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   requests
   tkinter
   ```

4. **Initialize the Database**:
   Run the following command to create the database and tables:
   ```bash
   python database.py
   ```

## How to Use the Application

1. **Run the Application**:
   Start the application by running:
   ```bash
   python main.py
   ```

2. **Add a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to save the student information.

3. **Fetch Students**:
   - Click the "Fetch Students" button to retrieve and display the list of all students in the application.

4. **Add a Course**:
   - Enter the course name in the "Course Name" field.
   - Enter the course level in the "Course Level" field.
   - Click the "Add Course" button to save the course information.

5. **View Course Data**:
   - Currently, the application does not display the list of courses. This feature can be added in future updates.

## Database Migration

The application uses Alembic for database migrations. When you run the application for the first time, it will create the necessary tables for both students and courses while preserving any existing student data.

## Conclusion

This Student Management Application provides a simple yet effective way to manage student and course information. Future enhancements may include additional features such as course listing, editing, and deleting functionalities.

For any issues or feature requests, please contact the development team.
```