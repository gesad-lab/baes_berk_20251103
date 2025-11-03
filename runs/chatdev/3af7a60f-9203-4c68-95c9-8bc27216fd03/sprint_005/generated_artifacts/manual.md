```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Main Functions

The Teacher Management System provides the following functionalities:

- **Create and Manage Teachers**: Add new teachers with their names and email addresses.
- **Create and Manage Students**: Add new students, including their names, email addresses, and enrolled courses.
- **Create and Manage Courses**: Add new courses with their names and levels.
- **Retrieve Data**: Fetch lists of teachers, students, and courses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/teacher_management_system.git
   cd teacher_management_system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   alembic
   email-validator
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Migration

Before running the application, you need to set up the database and apply migrations:

1. **Run the Migration Script**:
   Make sure you have Alembic installed and run the migration to create the necessary tables:
   ```bash
   alembic upgrade head
   ```

## Running the Application

To start the application, use the following command:
```bash
uvicorn main:app --reload
```
This will start the FastAPI server, and you can access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Teachers

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created teacher object.

- **Get All Teachers**:
  - **Endpoint**: `GET /teachers/`
  - **Response**: Returns a list of all teachers.

### Students

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com",
      "courses": [1, 2]  // List of course IDs
    }
    ```
  - **Response**: Returns the created student object.

- **Get All Students**:
  - **Endpoint**: `GET /students/`
  - **Response**: Returns a list of all students.

### Courses

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Advanced"
    }
    ```
  - **Response**: Returns the created course object.

- **Get All Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**: Returns a list of all courses.

## Conclusion

This Teacher Management System is a straightforward application for managing educational entities. You can extend its functionality by adding more features as needed. For any issues or feature requests, please reach out to the development team.

Happy coding!
```