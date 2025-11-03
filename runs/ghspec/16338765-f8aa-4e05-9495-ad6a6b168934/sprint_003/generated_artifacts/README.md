# README.md

# Project Documentation

## User Scenarios

1. **Create a Course**:
   - As an admin, I want to create a new course by specifying its name and level to expand the curriculum offerings.
   - **Endpoint**: `POST /courses`
   - **Request Body**:
     ```json
     {
       "name": "Course Name",
       "level": "Beginner"
     }
     ```
   - **Response**:
     - **201 Created**: Returns the details of the newly created course, including its assigned ID.
     ```json
     {
       "id": "12345",
       "name": "Course Name",
       "level": "Beginner"
     }
     ```

2. **Retrieve Course Information**:
   - As a user, I want to access details of a specific course by its ID so that I can view the course name and level.
   - **Endpoint**: `GET /courses/{id}`
   - **Response**:
     - **200 OK**: Returns the details of the course.
     ```json
     {
       "id": "12345",
       "name": "Course Name",
       "level": "Beginner"
     }
     ```

3. **Update Course Information**:
   - As an admin, I want to update the existing details of a course, including its name and level, so that course information remains current.
   - **Endpoint**: `PUT /courses/{id}`
   - **Request Body**:
     ```json
     {
       "name": "Updated Course Name",
       "level": "Intermediate"
     }
     ```
   - **Response**:
     - **200 OK**: Returns the updated course details.
     ```json
     {
       "id": "12345",
       "name": "Updated Course Name",
       "level": "Intermediate"
     }
     ```

## Migration Instructions

To deploy the latest changes, ensure to run the following migration steps:

1. **Initial Migration**:
   - Run the migration command to create courses table:
   ```bash
   alembic upgrade head
   ```

2. **Schema Update**:
   - If additional fields or modifications were introduced, ensure to check the migration scripts in `migrations/` and run them as needed.

3. **Seeding Initial Data** (optional):
   - If you wish to seed the database with initial course data, execute:
   ```bash
   python src/scripts/seed_courses.py
   ```

Be sure to verify that your environment variables are set correctly and that the database connection is established before running migrations or seeds.