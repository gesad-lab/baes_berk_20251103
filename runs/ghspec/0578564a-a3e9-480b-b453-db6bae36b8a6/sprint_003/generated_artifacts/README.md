# README.md

# Student Management System

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [User Scenarios & Testing](#user-scenarios--testing)
- [Success Criteria](#success-criteria)

## Overview
This web application allows for managing students and courses in an educational institution. The application provides RESTful API endpoints for creating and retrieving students and courses.

## Getting Started
1. Ensure that you have Python and PostgreSQL installed.
2. Clone the repository and navigate to the project directory.
3. Set up a virtual environment and install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure the database connection settings in `config.py`.
5. Run database migrations to set up the initial schema:
    ```bash
    alembic upgrade head
    ```

## API Endpoints

### Course Management
- **Create Course**
  - **Endpoint**: `POST /courses`
  - **Input**: `{ "name": "Course Name", "level": "Course Level" }`
  - **Response**: `{ "message": "Course created successfully", "course": { "id": 1, "name": "Course Name", "level": "Course Level" } }`

- **Retrieve Courses**
  - **Endpoint**: `GET /courses`
  - **Response**: `[{ "id": 1, "name": "Course Name", "level": "Course Level" }, ...]`

### Database Schema
- **Courses Table**
  - **Table Name**: `courses`
    - `id`: Integer, auto-incremented primary key (system-managed)
    - `name`: String, required field for the course name
    - `level`: String, required field for the course level

## User Scenarios & Testing
1. **Creating a Course**
   - **Scenario**: An administrator wants to add a new course with a specific name and level.
   - **Test**: The administrator submits a request to create a course with valid name and level, and the endpoint returns a success message along with the course details including a unique identifier (ID).

2. **Retrieving Courses**
   - **Scenario**: An administrator wants to view all available courses in the database.
   - **Test**: The endpoint returns a JSON array of course objects, each containing an ID, name, and level.

## Success Criteria
- The application can successfully create a new course and return the correct details.
- The application can successfully retrieve a list of all courses.
- The database schema is modified to include the Course entity without data loss for existing records.
- API responses must continue to be in JSON format and adhere to a consistent structure.

## Verifying Table Existence
To verify that the `Courses` table exists in the database, you can execute the following SQL command:

```sql
SELECT to_regclass('public.courses');
```

If the command returns `courses`, it confirms that the table exists. If it returns `NULL`, the table has not been created successfully.

## Next Steps
- Implement the Course management API endpoints in `routes.py`.
- Create a migration script to establish the `Courses` table.
- Ensure that all functionalities work as expected and are covered by tests.