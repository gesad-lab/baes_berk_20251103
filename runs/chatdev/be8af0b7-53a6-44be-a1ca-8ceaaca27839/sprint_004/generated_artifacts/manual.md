Here's a detailed user manual for the software, formatted in Markdown:

```markdown
# Student Course Management Application

A FastAPI application for managing students and their associated courses.

## Overview

This application allows users to create and manage students and courses, establishing a many-to-many relationship between them. Students can enroll in multiple courses, and each course can have multiple students.

## Main Functions

- **Create Student**: Add a new student with a name, email, and optional list of course IDs.
- **Create Course**: Add a new course with a name and level.
- **Retrieve Students**: Get a list of all students along with their associated courses.
- **Retrieve Courses**: Get a list of all courses available in the system.

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

## Running the Application

To start the FastAPI application, run the following command:

```bash
python main.py
```

The application will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

### Create Student

**Endpoint**: `POST /students/`

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "courses": [1, 2]  // List of course IDs (optional)
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

### Create Course

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

### Retrieve Students

**Endpoint**: `GET /students/`

**Query Parameters**:
- `skip`: Number of records to skip (default: 0)
- `limit`: Number of records to return (default: 10)

**Response**:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "courses": [1, 2]
  }
]
```

### Retrieve Courses

**Endpoint**: `GET /courses/`

**Query Parameters**:
- `skip`: Number of records to skip (default: 0)
- `limit`: Number of records to return (default: 10)

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

## Conclusion

This application provides a robust framework for managing students and courses, allowing for easy enrollment and retrieval of information. For further customization or feature requests, please contact the development team.
```

This manual provides a comprehensive guide for users to understand the application, its functionalities, installation process, and how to interact with the API.