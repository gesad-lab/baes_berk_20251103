# README.md

# Project Title

## Overview

This project integrates course relationships into the existing Student entity, enabling enrollment functionality and retrieval processes for students.

## API Documentation

### Enrollment Functionality

The API allows for enrolling students in courses. Below are the key endpoints related to student enrollment:

#### Enroll a Student in a Course

- **Endpoint**: `POST /enroll`
- **Request Body**:
    ```json
    {
        "student_id": "string",
        "course_id": "string"
    }
    ```
- **Response**:
    - Status Code: `201 Created`
    - Body:
    ```json
    {
        "message": "Student enrolled successfully",
        "data": {
            "student_id": "string",
            "course_id": "string"
        }
    }
    ```
- **Error Responses**:
    - Status Code: `400 Bad Request` - Invalid input
    - Status Code: `404 Not Found` - Student or Course not found

#### Retrieve Student Details with Courses

- **Endpoint**: `GET /students/{student_id}`
- **Response**:
    - Status Code: `200 OK`
    - Body:
    ```json
    {
        "student_id": "string",
        "courses": [
            {
                "course_id": "string",
                "course_name": "string"
            }
        ]
    }
    ```
- **Error Responses**:
    - Status Code: `404 Not Found` - Student not found

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo.git
   cd your-repo
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.8+ installed, then install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the project root directory using the provided `.env.example` as a template. Ensure that the following variables are set:
   - `DATABASE_URL`: Your database connection string
   - `SECRET_KEY`: A secret key for encryption

4. **Run Database Migrations**:
   Make sure Alembic is set up, then run:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Launch the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

### Student-Course Relationship

The system leverages a relational model where each student can enroll in multiple courses. This enhancement has been designed to maintain data integrity while providing a straightforward API for users to enroll students and retrieve their course details.

---

## Next Steps

1. **Setup Migration Infrastructure**: Configure Alembic for schema management and run migrations.
2. **Implement Student Model Updates**: Extend the model to include the new relationship.
3. **Develop API Endpoints**: Introduce new endpoints for enrolling students and retrieving their details.
4. **Create Tests**: Develop comprehensive test cases covering the new functionalities.
5. **Update Documentation**: Ensure that all relevant documentation is current and complete.
6. **Deploy Changes**: Schedule deployment to the production environment following thorough testing.