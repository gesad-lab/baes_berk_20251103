Here's the `manual.md` file that provides a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Student Management System

A simple application for managing students and courses using FastAPI and SQLite.

## Main Functions

The Student Management System allows users to perform the following operations:

- **Manage Students**: Create and retrieve student records, including their names and email addresses.
- **Manage Courses**: Create and retrieve course records, including course names and levels.
- **Database Management**: The application uses SQLite as the database, and it supports migrations to update the database schema without losing existing data.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migrations**:
   Ensure you have an `alembic.ini` file in your project directory, then run:
   ```bash
   alembic upgrade head
   ```

## Usage Instructions

1. **Start the Application**:
   To run the application, execute the following command:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the FastAPI server at `http://127.0.0.1:8000`.

2. **Access the GUI**:
   The application provides a simple GUI built with Tkinter. Run the following command to launch the GUI:
   ```bash
   python main.py
   ```

3. **Adding Students**:
   - Enter the student's name and email in the respective fields.
   - Click on the "Add Student" button to save the student record.

4. **Adding Courses**:
   - Enter the course name and level in the respective fields.
   - Click on the "Add Course" button to save the course record.

5. **Viewing Students**:
   - Click on the "Show Students" button to retrieve and display the list of all students in the output area.

## API Endpoints

The application exposes the following API endpoints:

- **Create Student**: `POST /students/`
  - Request Body: `{ "name": "string", "email": "string" }`
  
- **Get Students**: `GET /students/`
  - Response: List of students with their IDs, names, and emails.

- **Create Course**: `POST /courses/`
  - Request Body: `{ "name": "string", "level": "string" }`
  
- **Get Courses**: `GET /courses/`
  - Response: List of courses with their IDs, names, and levels.

## Additional Information

- Ensure that the SQLite database file (`students.db`) is created in the project directory after running the migrations.
- The application is designed to preserve existing student data during database migrations.

For further assistance or to report issues, please contact the development team.
```

This manual provides a comprehensive overview of the application, guiding users through installation, usage, and understanding the core functionalities.