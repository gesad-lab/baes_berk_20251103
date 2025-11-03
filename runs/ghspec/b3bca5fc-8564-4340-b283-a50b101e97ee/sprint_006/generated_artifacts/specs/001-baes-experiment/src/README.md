# Updated README.md Content

# Course-Teacher API Documentation

## API Endpoints for Course-Teacher Relationships

### 1. Assign Teacher to Course
- **Endpoint**: `POST /courses/{course_id}/assign-teacher`
- **Description**: Assign a specific Teacher to a Course by providing the Course ID and the Teacher ID in the request body.
- **Request Body**:
  ```json
  {
    "teacher_id": "string"  // Required: ID of the Teacher to be assigned
  }
  ```
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**: 
  ```json
  {
    "message": "Teacher assigned successfully to the course."
  }
  ```

### 2. Retrieve Course Information with Teacher Details
- **Endpoint**: `GET /courses/{course_id}`
- **Description**: Retrieve detailed information about a specific Course, including details of the assigned Teacher.
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**: 
  ```json
  {
    "id": "course_id",
    "title": "Course Title",
    "teacher": {
      "id": "teacher_id",
      "name": "Teacher Name",
      "email": "teacher@example.com"
    }
  }
  ```

### 3. Database Schema Update
- **Update the Courses Table**:
  - A new foreign key column `teacher_id` has been added to the Courses table, referencing the Teachers table.
  - The migration process ensures that existing Course and Student data remain intact and no data is removed.

## Success Criteria
- The application must respond with a 200 status code along with a confirmation message upon successful assignment of a Teacher to a Course.
- The application must return the correct Course data and the assigned Teacher details with a 200 status code upon successful retrieval of the Course's information.
- The application should validate input for the assignment process and respond with a 404 status code if the specified Course does not exist.
- The database schema update must include the new `teacher_id` foreign key in the `Courses` table without affecting existing Student or Course data.

## Key Entities
- **Course**:
  - Updated entity to include:
    - `teacher_id`: Foreign key referencing the Teacher assigned to the Course.

- **Teacher**:
  - Existing entity, referenced in the Course entity without changes made.

- **Student**:
  - No changes made to this existing entity.

---

This update provides comprehensive documentation for the new API endpoints for managing the relationships between Courses and Teachers, ensuring that users can effectively interact with these features in the application.