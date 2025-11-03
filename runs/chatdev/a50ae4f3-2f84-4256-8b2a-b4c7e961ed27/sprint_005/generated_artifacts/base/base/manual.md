```markdown
# Course and Student Management System

A simple application for managing students and courses using a graphical user interface (GUI) built with Tkinter and a FastAPI backend.

## Main Functions

The application allows users to:

- **Manage Students**: Create new students and view existing students.
- **Manage Courses**: Create new courses and view existing courses.

## Installation

To run the application, you need to install the required dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests alembic
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the Alembic migration:
   ```bash
   alembic upgrade head
   ```

5. **Start the FastAPI Server**:
   Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

6. **Run the GUI Application**:
   In a separate terminal, run the GUI:
   ```bash
   python gui.py
   ```

## How to Use the Application

### Student Management

1. **Create a Student**:
   - Enter the student's name and email in the respective fields.
   - Click on the "Create Student" button.
   - A success message will appear if the student is created successfully.

2. **View Students**:
   - Click on the "Get Students" button to fetch and display the list of existing students.

### Course Management

1. **Create a Course**:
   - Enter the course name and level in the respective fields.
   - Click on the "Create Course" button.
   - A success message will appear if the course is created successfully.

2. **View Courses**:
   - Click on the "Get Courses" button to fetch and display the list of existing courses.

## Database Schema

The application uses SQLite as the database and includes two main tables:

- **students**: Stores student information (id, name, email).
- **courses**: Stores course information (id, name, level).

## Additional Information

- The application is built using FastAPI for the backend and Tkinter for the GUI.
- The database schema is managed using SQLAlchemy and Alembic for migrations.
- The application is designed to preserve existing student data during database migrations.

For further documentation and examples, please refer to the source code and comments within the files.
```