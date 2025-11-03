# README.md

# Student Management System

## Overview & Purpose
The purpose of this student management system is to facilitate the organization and management of student data effectively. As part of its enhancement, we have introduced a new Course entity which will store essential information regarding courses including their names and levels. This feature aims to improve the educational capabilities of the system, allowing for better management of courses associated with students.

## Course Feature

### User Scenarios & Testing
1. **Create Course**: A user can input a course's name and level, which will be stored in the database as a new Course entity.
   - **Expected Result**: The course is successfully added, and the server returns a 201 Created status with the course details in JSON format, including name and level.

2. **Retrieve All Courses**: A user can request a list of all courses, and receives a response detailing each course's name and level.
   - **Expected Result**: The server responds with a 200 OK status that includes an array of course objects in JSON format.

3. **Error Handling for Missing Fields**: A user attempts to create a course without providing either a name or a level.
   - **Expected Result**: The server returns a 400 Bad Request status with an appropriate error message, indicating the required fields.

4. **Database Migration**: The migration process should seamlessly introduce the Course table without disrupting existing Student data.
   - **Expected Result**: The database schema is updated to include the Course table while preserving existing student records.

### Functional Requirements
1. The application must allow users to create a new course by providing a name and a level.
   - **Input**: 
     - Name (string, required)
     - Level (string, required)
   - **Output**: JSON response with course details (including name and level) and status code 201 Created.

2. The application must allow users to retrieve a list of all courses, displaying their name and level.
   - **Output**: JSON response with an array of course objects (each containing name and level).

### Running Migrations
To run the migrations and ensure the new Course entity is set up, use the following command:
```bash
flask db upgrade
```

### API Endpoints
- **Create Course**
  - **Endpoint**: POST `/api/courses`
  - **Request Body**:
    ```json
    {
      "name": "Course Name",
      "level": "Intermediate"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Course Name",
      "level": "Intermediate"
    }
    ```
    
- **Retrieve All Courses**
  - **Endpoint**: GET `/api/courses`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Course Name",
        "level": "Intermediate"
      }
    ]
    ```

### Testing
To run tests associated with the Course entity, ensure you have set up your testing environment and then execute:
```bash
pytest tests/test_course.py
```

## Conclusion
This README outlines the introduction of the Course feature within the student management system, detailing the associated API endpoints, user scenarios, and testing instructions. With this new functionality, users will be able to manage courses efficiently alongside student data.