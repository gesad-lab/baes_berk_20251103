# Updated README.md

# Project Title

## Overview
This project serves as an API for managing students and courses. It utilizes FastAPI for the server and SQLite for the database.

## User Scenarios & Testing

1. **Scenario 1: Create a New Course**
   - User sends a request to add a new course with a valid name and level.
   - **Expected Outcome**: The system should successfully create the course and return a JSON response containing the course’s information, including an auto-generated ID.

2. **Scenario 2: Create Course with Missing Name**
   - User sends a request to add a new course without a name but with a valid level.
   - **Expected Outcome**: The system should return a JSON error response indicating that the name field is required.

3. **Scenario 3: Create Course with Missing Level**
   - User sends a request to add a new course with a valid name but without a level.
   - **Expected Outcome**: The system should return a JSON error response indicating that the level field is required.

4. **Scenario 4: Retrieve Course Information**
   - User sends a request to retrieve a list of all courses.
   - **Expected Outcome**: The system should return a JSON response with an array of all existing courses, showing their IDs, names, and levels.

5. **Scenario 5: Database Migration Verification**
   - On application startup or during migration, the database schema should be updated to include the Course table.
   - **Expected Outcome**: The system should successfully apply the migration while preserving existing Student data.

## Assumptions
- The user has access to the same environment and tech stack used in the previous sprint.
- The existing SQLite database can be updated to include the new Course table without losing existing Student data through a proper migration process.
- Users can interact with the updated RESTful API and understand JSON data formats.

## Architecture Overview
The architecture will remain consistent with previous plans while integrating the new Course entity:
- **Client**: The existing API will serve requests related to courses.
- **Server**: FastAPI will handle incoming requests and perform operations through the SQLite database.
- **Database**: SQLite will be updated to include the new Course table without impacting existing data.

## Component Diagram
```plaintext
+-----------------+
|    Client/API   |
|    (Frontend)   |
+-------+---------+
        |
        v
+-------+--------+
|  FastAPI Server|
| (RESTful API)  |
+-------+--------+
        |
        v
+-------+--------+
|  SQLite Database|
|    +-----------+|
|    | Courses   ||
|    | Students  ||
+-----------------+
```

## Setup & Usage
To start the project, ensure you have the required dependencies installed and the environment properly configured. Refer to the Documentation for detailed setup instructions.