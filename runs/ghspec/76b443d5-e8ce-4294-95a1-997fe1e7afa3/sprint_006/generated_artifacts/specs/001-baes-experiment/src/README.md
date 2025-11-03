# Updated README.md

# Project Documentation

## Introduction

This project is an API built using FastAPI designed for managing courses and teachers.

## API Endpoints

### Teacher Endpoints

1. **Create a Teacher**
   - **URL**: `/teachers`
   - **Method**: `POST`
   - **Request Body**: 
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Response**: 
     - `201 Created` on success with the teacher details.
     - `400 Bad Request` if validation fails.

### Course Endpoints

1. **Assign a Teacher to a Course**
   - **URL**: `/courses/{course_id}/assign-teacher`
   - **Method**: `POST`
   - **Path Parameters**: 
     - `course_id`: ID of the course to assign the teacher to.
   - **Request Body**: 
     ```json
     {
       "teacher_id": 1
     }
     ```
   - **Response**: 
     - `200 OK` on success with the updated course details.
     - `404 Not Found` if the course or teacher does not exist.

2. **Remove a Teacher from a Course**
   - **URL**: `/courses/{course_id}/remove-teacher`
   - **Method**: `POST`
   - **Path Parameters**: 
     - `course_id`: ID of the course to remove the teacher from.
   - **Response**:
     - `200 OK` on success with the updated course details.
     - `404 Not Found` if the course does not exist.

3. **Get Course Details**
   - **URL**: `/courses/{course_id}`
   - **Method**: `GET`
   - **Path Parameters**: 
     - `course_id`: ID of the course to retrieve.
   - **Response**:
     - `200 OK` with the course details.
     - `404 Not Found` if the course does not exist.

## API Documentation

For a complete and interactive API documentation, please visit [FastAPI Docs](http://localhost:8000/docs) after running the application.

## Run the Application

To run this application, make sure you have FastAPI and the required dependencies installed. Then use the following command:

```bash
uvicorn src.main:app --reload
```

## Conclusion

This API provides various endpoints for managing teachers and courses efficiently. Be sure to refer to the API documentation for the latest updates and more detailed instructions.