```markdown
# Student Management Application

A comprehensive application for managing students, courses, and teachers in an educational environment.

## Main Functions

The Student Management Application provides the following functionalities:

- **Student Management**: Add, view, and manage student information, including names and emails.
- **Course Management**: Create and manage courses, including assigning students and teachers to courses.
- **Teacher Management**: Add and manage teacher information, including names and emails.
- **Teacher-Course Relationship**: Each course can be assigned to a specific teacher, allowing for better organization and management of educational resources.

## Installation

To run the Student Management Application, you need to set up your environment and install the required dependencies. Follow these steps:

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
   Use pip to install the required packages:
   ```bash
   pip install sqlalchemy alembic requests tkinter
   ```

4. **Set Up the Database**:
   The application uses SQLite for the database. The database will be initialized automatically when you run the application for the first time.

## How to Use the Application

1. **Run the Application**:
   Start the application by running the following command:
   ```bash
   python main.py
   ```

2. **Adding Students**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to save the student information.
   - Use the "Fetch Students" button to view the list of added students.

3. **Adding Teachers**:
   - Enter the teacher's name and email in the respective fields.
   - Click the "Add Teacher" button to save the teacher information.
   - Use the "Fetch Teachers" button to view the list of added teachers.

4. **Adding Courses**:
   - Enter the course name and level in the respective fields.
   - Select a student from the list and choose a teacher from the dropdown menu.
   - Click the "Add Course" button to save the course information.

5. **Viewing Data**:
   - The application provides lists for students and teachers, allowing you to view all added entries.

## Additional Notes

- Ensure that the FastAPI server is running on `http://127.0.0.1:8000` for the application to function correctly.
- The application is designed to maintain data integrity, ensuring that existing student, course, and teacher data is preserved during updates.

For any issues or feature requests, please contact the development team.
```