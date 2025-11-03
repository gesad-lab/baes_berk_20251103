```markdown
# Student Course Management System

A FastAPI application for managing students and their course enrollments.

## Main Functions

This application allows users to:

- Create and manage student records.
- Create and manage course records.
- Enroll students in courses.
- Retrieve lists of students and their enrolled courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/student-course-management.git
   cd student-course-management
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

4. **Initialize the database**:
   The application will automatically create the database tables when you run it for the first time.

## How to Use

### Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

### API Endpoints

#### 1. Create a Student

- **Endpoint**: `POST /students/`
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

#### 2. Retrieve Students

- **Endpoint**: `GET /students/`
- **Query Parameters**: `skip`, `limit`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
  ]
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

### Database Migration

To apply database migrations, you can use Alembic. Ensure you have the migration scripts set up, and run:

```bash
alembic upgrade head
```

This will apply any pending migrations to your database schema.

## Conclusion

This application provides a simple yet powerful way to manage students and their course enrollments. You can extend its functionality by adding more features as needed. For any issues or feature requests, please reach out to the development team.
```