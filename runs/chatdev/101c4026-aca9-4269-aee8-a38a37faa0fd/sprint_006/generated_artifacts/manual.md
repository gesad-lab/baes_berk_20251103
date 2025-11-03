```markdown
# ChatDev Course Management System

A comprehensive API for managing students, courses, and teachers in an educational environment.

## Main Functions

The ChatDev Course Management System provides the following functionalities:

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create, read, update, and delete course records, including associating courses with teachers.
- **Teacher Management**: Create, read, update, and delete teacher records.
- **Relationships**: Establish relationships between students, courses, and teachers.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy alembic
   ```

4. **Install SQLite** (if not already installed):
   - SQLite comes pre-installed with Python, but you can also download it from [SQLite Download Page](https://www.sqlite.org/download.html).

## Database Migration

Before running the application, ensure that the database schema is up to date. Run the migration script to create the necessary tables:

```bash
alembic upgrade head
```

## How to Use the API

### Starting the Application

To start the FastAPI application, run:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

The following endpoints are available for managing students, courses, and teachers:

#### Teacher Endpoints

- **Create a Teacher**:
  - `POST /teachers/`
  - Request Body: `{ "name": "Teacher Name", "email": "teacher@example.com" }`

- **Get All Teachers**:
  - `GET /teachers/`

- **Get a Teacher by ID**:
  - `GET /teachers/{teacher_id}`

- **Update a Teacher**:
  - `PUT /teachers/{teacher_id}`
  - Request Body: `{ "name": "Updated Name", "email": "updated@example.com" }`

- **Delete a Teacher**:
  - `DELETE /teachers/{teacher_id}`

#### Course Endpoints

- **Create a Course**:
  - `POST /courses/`
  - Request Body: `{ "name": "Course Name", "level": "Beginner", "teacher_id": 1 }`

- **Get All Courses**:
  - `GET /courses/`

- **Get a Course by ID**:
  - `GET /courses/{course_id}`

### Example Usage

1. **Create a Teacher**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}'
   ```

2. **Create a Course**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Math 101", "level": "Beginner", "teacher_id": 1}'
   ```

3. **Get All Courses**:
   ```bash
   curl -X GET "http://127.0.0.1:8000/courses/"
   ```

## Conclusion

The ChatDev Course Management System is designed to streamline the management of educational entities. With its robust API, you can easily manage students, courses, and teachers while maintaining relationships between them. For more detailed documentation, please refer to the code comments and the FastAPI documentation.
```