```markdown
# Student and Course Management System

A simple API for managing students and courses, allowing students to enroll in multiple courses.

## Main Functions

- **Create Students**: Add new students to the system.
- **Retrieve Students**: Get a list of all students.
- **Create Courses**: Add new courses to the system.
- **Retrieve Courses**: Get a list of all courses.
- **Enroll Students in Courses**: Allow students to enroll in specific courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Initialization

Before using the API, you need to initialize the database. Run the following command to create the necessary tables:

```bash
python main.py
```

This will create the `students`, `courses`, and `student_courses` tables in the SQLite database.

## API Usage

### Create a Student

**Endpoint**: `POST /students/`

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

**Response**:
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Retrieve Students

**Endpoint**: `GET /students/`

**Response**:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
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

**Response**:
```json
{
  "id": 1,
  "name": "Mathematics",
  "level": "Beginner"
}
```

### Retrieve Courses

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

**Endpoint**: `POST /students/{student_id}/courses/{course_id}/`

**Example Request**:
```bash
POST /students/1/courses/1/
```

**Response**:
```json
{
  "message": "Student enrolled in course successfully"
}
```

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn routes:router --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the API documentation at `http://127.0.0.1:8000/docs`.

## Conclusion

This Student and Course Management System provides a straightforward way to manage students and their course enrollments. Feel free to extend the functionality as needed!
```