```markdown
# Student and Course Management System

A simple application for managing students and courses using FastAPI and Tkinter.

## Main Functions

- **Student Management**: Create and retrieve student records, including their names and emails.
- **Course Management**: Create and retrieve course records, including their names and levels.
- **Database Management**: The application uses SQLite to store student and course data, with migrations to ensure data integrity.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

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
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date with the following command:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

6. **Open the GUI**:
   The GUI will launch automatically. If not, you can run:
   ```bash
   python main.py
   ```

## How to Use the Application

### Student Management

1. **Adding a Student**:
   - In the "Student Management" section, enter the student's name and email.
   - Click the "Submit" button to create a new student record.
   - The application will display a confirmation message with the student's details.

2. **Viewing Students**:
   - The application retrieves and displays a list of students in the database.

### Course Management

1. **Adding a Course**:
   - In the "Course Management" section, enter the course name and level.
   - Click the "Submit" button to create a new course record.
   - The application will display a confirmation message with the course details.

2. **Viewing Courses**:
   - The application retrieves and displays a list of courses in the database.

## Database Schema

- **Students Table**:
  - `id`: Integer, Primary Key
  - `name`: String, Required
  - `email`: String, Required

- **Courses Table**:
  - `id`: Integer, Primary Key
  - `name`: String, Required
  - `level`: String, Required

## Migration Scripts

The application uses Alembic for database migrations. Ensure to run migrations after making changes to the database schema.

## Troubleshooting

- If you encounter issues with Tkinter, ensure it is installed correctly. You can install it via your package manager or check the Python installation.
- For any errors related to FastAPI or database connections, check the console logs for detailed error messages.

## Support

For further assistance, please reach out via the support channel or check the documentation for more detailed guides and examples.

```
