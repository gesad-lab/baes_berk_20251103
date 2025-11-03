```markdown
# Course Management System

A simple application for managing students and courses using FastAPI and SQLite.

## Main Functions

The Course Management System allows users to:

- **Manage Students**: Add new students and view existing students.
- **Manage Courses**: Add new courses and view existing courses.

## Installation

To set up the environment and run the application, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Initialize the database**:
   Run the following command to create the initial database schema:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

5. **Run the application**:
   Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

## How to Use the Application

### Using the API

You can interact with the application through the API endpoints:

- **Add a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Student Name",
      "email": "student@example.com"
    }
    ```

- **Get Students**:
  - **Endpoint**: `GET /students/`
  - **Response**: Returns a list of students.

- **Add a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Course Name",
      "level": "Course Level"
    }
    ```

- **Get Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**: Returns a list of courses.

### Using the GUI

1. **Launch the GUI**:
   The GUI is implemented using Tkinter. You can run it by executing the `gui.py` file:
   ```bash
   python gui.py
   ```

2. **Add a Student**:
   - Enter the student's name and email in the respective fields and click "Add Student".

3. **Show Students**:
   - Click the "Show Students" button to view the list of added students.

4. **Add a Course**:
   - Enter the course name and level in the respective fields and click "Add Course".

5. **Show Courses**:
   - Click the "Show Courses" button to view the list of added courses.

## Database Migration

To add new fields or tables to the database without losing existing data, you can use Alembic for migrations. For example, to add the Course table, run:
```bash
alembic revision --autogenerate -m "Add Course table"
```

This will create a migration script that you can apply to update the database schema.

## Conclusion

This Course Management System provides a simple interface for managing students and courses. You can extend its functionality by adding more features as needed. For any issues or feature requests, please contact the development team.
```