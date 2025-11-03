# Student Course Management System

A FastAPI application for managing students and their course enrollments.

## Main Functions

The Student Course Management System allows users to perform the following operations:

- **Create Students**: Add new students to the database.
- **Retrieve Students**: Get a list of all students along with their enrolled courses.
- **Create Courses**: Add new courses to the database.
- **Retrieve Courses**: Get a list of all available courses.
- **Enroll Students in Courses**: Enroll a student in a specific course.

## Installation

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

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Database Migration

Before running the application, you need to apply the database migrations to set up the necessary tables and relationships.

1. **Run the Migration Script**:
   ```bash
   alembic upgrade head
   ```

This will create the `students`, `courses`, and `student_courses` tables in your SQLite database, preserving any existing data.

## Running the Application

To start the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## Using the API

### Create a Student

**Endpoint**: `POST /students/`

**Request Body**:
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

### Retrieve All Students

**Endpoint**: `GET /students/`

**Response**:
```json
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "courses": []
    }
]
```

### Create a Course

**Endpoint**: `POST /courses/`

**Request Body**:
```json
{
    "name": "Mathematics",
    "level": "Beginner"
}
```

### Retrieve All Courses

**Endpoint**: `GET /courses/`

**Response**:
```json
[
    {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
    }
]
```

### Enroll a Student in a Course

**Endpoint**: `POST /students/{student_id}/courses/{course_id}`

**Example**: To enroll student with ID 1 in course with ID 1, make a request to:
```
POST /students/1/courses/1
```

**Response**: `204 No Content` (indicates successful enrollment)

## Conclusion

This application provides a simple yet effective way to manage students and their course enrollments. You can extend its functionality by adding more features as needed. For further customization or support, feel free to reach out to the development team.