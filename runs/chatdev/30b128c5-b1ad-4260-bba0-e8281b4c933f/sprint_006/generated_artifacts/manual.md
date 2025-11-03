```markdown
# Student Management Application

A comprehensive application for managing students, courses, and teachers in an educational environment.

## Main Functions

The Student Management Application provides the following key functionalities:

- **Manage Students**: Add, view, and manage student records.
- **Manage Courses**: Add, view, and manage courses offered, including associating them with teachers.
- **Manage Teachers**: Add, view, and manage teacher records.
- **Teacher-Course Relationship**: Each course can be associated with a teacher, allowing for better organization and management of educational resources.

## Installation

To run the Student Management Application, you need to set up the environment and install the required dependencies. Follow these steps:

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

3. **Install Required Dependencies**:
   You need to install the following Python packages:
   ```bash
   pip install sqlalchemy alembic requests tkinter
   ```

4. **Set Up the Database**:
   The application uses SQLite for the database. The database schema will be created automatically when you run the application for the first time.

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI server and the GUI application:
   ```bash
   uvicorn main:app --reload
   python main.py
   ```

2. **Using the GUI**:
   - **Add Student**: Enter the student's name and email, then click "Add Student".
   - **Fetch Students**: Click "Fetch Students" to view the list of registered students.
   - **Add Course**: Enter the course name and level, select a teacher from the dropdown, and click "Add Course".
   - **Add Teacher**: Enter the teacher's name and email, then click "Add Teacher".
   - **Fetch Teachers**: Click "Fetch Teachers" to view the list of registered teachers.

3. **Teacher Selection**:
   When adding a course, ensure you select a teacher from the dropdown menu. This establishes the relationship between the course and the teacher.

## Additional Information

- The application is built using Python and utilizes the FastAPI framework for the backend.
- The database schema includes tables for students, courses, and teachers, with relationships defined to manage associations effectively.
- The GUI is built using Tkinter, providing a user-friendly interface for managing records.

## Support

For any issues or questions, please reach out to our support team at [support@example.com](mailto:support@example.com).

```
