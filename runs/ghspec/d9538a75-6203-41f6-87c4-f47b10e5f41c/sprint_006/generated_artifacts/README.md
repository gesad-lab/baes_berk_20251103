# README.md

# Course Management Application

This application is designed to manage courses, teachers, and students effectively. It provides functionalities to assign teachers to courses, retrieve course details including teacher information, and handle database migrations.

## User Scenarios & Testing

### Scenario 1: Assign Teacher to Course
- **Given** an admin user is logged in,
- **When** the admin assigns a teacher to a course via the course management interface,
- **Then** the specified teacher should be successfully associated with the course, and a confirmation message should be displayed.

### Scenario 2: Validate Teacher Assignment
- **Given** a course exists and an admin user attempts to assign a teacher,
- **When** the admin does not select a teacher,
- **Then** the system should return an error message indicating that a teacher assignment is required.

### Scenario 3: Retrieve Course with Teacher Information
- **Given** a course has an assigned teacher,
- **When** a request is made to retrieve the course's details,
- **Then** the API should return the course information including the assigned teacher’s name and email.

### Scenario 4: Successful Database Migration
- **Given** the existing database contains students, courses, and teachers,
- **When** the database migration is executed to establish the relationship,
- **Then** all existing student and course data should remain intact and accessible, and the new teacher relationship should be intact.

## Functional Requirements
1. Extend the existing `Course` entity to include:
   - A field `teacher_id`: A foreign key referencing the `Teacher` entity, which establishes the relationship between a course and its assigned teacher.

2. Update the database schema to reflect this relationship:
   - Modify the `Course` table to include the `teacher_id` field.
   - Ensure that `teacher_id` is nullable to allow existing courses without an assigned teacher.

3. Ensure data integrity and validation:
   - Validate that the `teacher_id`, if provided, corresponds to a valid `Teacher` entry.
   - If a course is being updated to assign or change a teacher, the system must ensure the corresponding teacher exists.

4. Create or update API endpoints for:
   - Assigning a teacher to a course.
   - Retrieving course details including teacher information.

## Development Steps
1. **Setup Environment**:
   - Confirm the virtual environment is properly working, and all necessary libraries are included in `requirements.txt`.

2. **Modify Course Model**:
   - Update `Course` model to include `teacher_id` as a foreign key referencing the `Teacher` entity.

3. **Database Migration**:
   - Create a migration script (`add_teacher_relationship_to_courses.py`) to include the `teacher_id` column in the `courses` table without impacting existing data.

4. **Implement API Endpoints**:
   - Update `routes.py` to add functionalities for assigning teachers to courses and retrieving course details with teacher information.

5. **Update Validation Logic**:
   - Modify the validation functionalities in `validations.py` to validate the `teacher_id` when assigning a teacher to a course.

6. **Testing**:
   - Write unit tests in `test_routes.py` for assigning teachers to courses and retrieving course details with teacher information, ensuring robust error handling for assignment failures.
   - Achieve a target of at least 70% coverage for business logic associated with the new relationship.

7. **Documentation**:
   - Update this `README.md` with details about new endpoints, including examples of request and response structures.

8. **Validation**:
   - Perform manual tests using Postman or curl to verify the complete functionality for assigning teachers to courses.

## API Endpoints
### Assign Teacher to Course
- **Endpoint**: `POST /api/v1/courses/<int:course_id>/assign_teacher`
- **Request Body**:
    ```json
    {
        "teacher_id": <int>
    }
    ```
- **Response**:
    - **200 OK**: Teacher assigned successfully.
    - **400 Bad Request**: Validation error - teacher assignment required.

### Retrieve Course with Teacher Information
- **Endpoint**: `GET /api/v1/courses/<int:course_id>`
- **Response**:
    ```json
    {
        "course_id": <int>,
        "course_name": "Example Course",
        "teacher": {
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    }
    ```

## Conclusion
This README covers the validation scenarios, functional requirements, development steps, and API endpoints for the Course Management Application. Ensure to follow the guidelines for a robust environment setup and code quality.