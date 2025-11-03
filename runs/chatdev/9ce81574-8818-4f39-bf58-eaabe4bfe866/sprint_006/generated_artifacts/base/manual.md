```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Main Functions

This application allows you to:

- **Create and manage teachers**: Add new teachers with their names and email addresses.
- **Create and manage students**: Add new students with their names and email addresses.
- **Create and manage courses**: Add new courses with their names and levels.
- **Enroll students in courses**: Enroll students in various courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use

### API Endpoints

The application exposes several API endpoints to interact with the data.

#### 1. Create a Teacher

- **Endpoint**: `POST /teachers/`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

#### 2. Create a Student

- **Endpoint**: `POST /students/`
- **Request Body**:
  ```json
  {
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
  }
  ```

#### 3. Create a Course

- **Endpoint**: `POST /courses/`
- **Request Body**:
  ```json
  {
    "name": "Mathematics",
    "level": "Beginner"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Mathematics",
    "level": "Beginner"
  }
  ```

#### 4. Enroll a Student in a Course

- **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
- **Response**:
  ```json
  {
    "message": "Student enrolled in course successfully"
  }
  ```

#### 5. Get All Students

- **Endpoint**: `GET /students/`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
  ]
  ```

### Database Migration

To update the database schema and include the new Teacher table while preserving existing Student and Course data, run the following command:

```bash
alembic upgrade head
```

This command will create the `teachers` table in the database.

## Conclusion

This Teacher Management System provides a simple yet effective way to manage teachers, students, and courses. You can extend its functionality by adding more features as needed. For any issues or questions, please refer to the documentation or contact support.
```