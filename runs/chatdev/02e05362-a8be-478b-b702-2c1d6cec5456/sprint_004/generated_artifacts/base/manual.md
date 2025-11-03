Here's a detailed user manual for the Student Management application, including installation instructions and usage guidelines.

```markdown
# Student Management Application

A simple application for managing students and courses, allowing users to add and view student and course information.

## Main Functions

- **Add Student**: Allows users to input student details (name and email) and save them to the database.
- **View Students**: Displays a list of all students currently stored in the database.
- **Add Course**: Enables users to input course details (name and level) and save them to the database.
- **View Courses**: Displays a list of all courses currently stored in the database.

## Quick Install

To run the Student Management application, you need to install the required dependencies. Follow these steps:

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
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   pydantic
   requests
   tkinter
   alembic
   ```

4. **Run Database Migrations**:
   To create the necessary database tables, run the following command:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Start the Application**:
   Run the main application file:
   ```bash
   python main.py
   ```

2. **Using the GUI**:
   - The application will open a graphical user interface (GUI) window.
   - **Adding a Student**:
     - Enter the student's name and email in the respective fields.
     - Click the "Add Student" button to save the information.
   - **Viewing Students**:
     - Click the "View Students" button to display a list of all students.
   - **Adding a Course**:
     - Enter the course name and level in the respective fields.
     - Click the "Add Course" button to save the information.
   - **Viewing Courses**:
     - Click the "View Courses" button to display a list of all courses.

## Database Structure

The application uses a SQLite database to store student and course information. The following tables are created:

- **students**:
  - `id`: Integer, primary key
  - `name`: String, required
  - `email`: String, required

- **courses**:
  - `id`: Integer, primary key
  - `name`: String, required
  - `level`: String, required

## Additional Information

For any issues or feature requests, please contact the development team at [support@chatdev.com](mailto:support@chatdev.com).

Thank you for using the Student Management Application!
```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, and usage guidelines.