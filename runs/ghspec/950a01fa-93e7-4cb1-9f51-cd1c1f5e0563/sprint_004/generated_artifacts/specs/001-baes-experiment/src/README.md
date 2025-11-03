# Updated README.md

# Project Title

## Overview

This project provides an API for managing students and their course enrollments. It includes endpoints to enroll students in courses and to retrieve a list of courses each student is enrolled in.

---

## Functional Requirements

### 1. Enroll Student in Course

- **Endpoint**: `POST /students/{student_id}/enroll`
- **Request**: 
  - Accepts a JSON body with the required field: 
    ```json
    {
      "course_id": "string"
    }
    ```
- **Response**: 
  - A success message and the updated Student object, including the list of enrolled courses.

### 2. Retrieve Student Courses

- **Endpoint**: `GET /students/{student_id}/courses`
- **Response**: 
  - A JSON array of Course objects the Student is enrolled in, including their names and levels.

### 3. Update the Database Schema

- The database schema must be updated to include a new association:
  - A Student can have multiple Course entries.
  - This is achieved through a junction table that maintains `student_id` and `course_id`.
- Migrations must ensure that existing data in both the Student and Course tables is preserved and compatible.

### 4. Data Format

- All API responses must be in JSON format.

---

## Setup

Make sure to install the required dependencies:

```bash
pip install -r requirements.txt
```

Initialize the database before running the application:

```bash
python src/db/migrate.py  # Add migration script if it doesn't exist
```

---

## Running the Application

To start the FastAPI application:

```bash
uvicorn src.main:app --reload
```

The API documentation will be available at `http://127.0.0.1:8000/docs`.

---

## Testing

To run the tests, use:

```bash
pytest
```

The test suite includes tests for API endpoints, ensuring that the enrollment feature works as intended. 

--- 

## Contributing

Please refer to the contribution guidelines for details on how to submit changes.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.