# README.md

# Student Management Application

## API Documentation

### Associate Teacher with Course

- **Endpoint**: `POST /courses/{courseId}/assignTeacher`
- **Description**: This endpoint allows you to associate a teacher with an existing course.
- **Request Body**:
  ```json
  {
      "teacherId": <integer>  // Required. The ID of the teacher to associate with the course.
  }
  ```
  
- **Response**: Returns the updated Course object in JSON format.
  ```json
  {
      "id": <integer>,  // Course ID
      "name": "<string>",  // Course name
      "teacher_id": <integer>,  // ID of the associated teacher
      // additional course fields...
  }
  ```
  
- **Error Responses**:
  - `404 Not Found`: The teacher with the specified `teacherId` does not exist.
    - Example:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Teacher not found.",
            "details": {}
        }
    }
    ```

### Database Schema Update

The `Course` entity has been updated to include a new foreign key field:

- **Field**: `teacher_id` (Integer, nullable, referencing the Teacher entity)

### Testing Scenarios

1. **Scenario 1: Associate a Teacher with a Course**
   - Test that a valid teacher can be associated with a course successfully.
  
2. **Scenario 2: Associate a Course with a Non-Existent Teacher**
   - Verify that an error is returned when attempting to associate a course with a non-existent teacher.
  
3. **Scenario 3: Verify Course to Teacher Association**
   - Confirm that fetching course details includes the correct teacher information when a teacher has been associated.
  
4. **Scenario 4: Database Migration Verification**
   - Ensure the migration preserves existing data for Students and Courses while adding the teacher association.

---

## Getting Started

Follow these steps to get your development environment up and running:

1. Clone the repository: `git clone <repository-url>`
2. Navigate into the project directory: `cd student_management_app`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file based on the `.env.example` provided.
5. Run migrations to set up the database: `python src/database.py migrate`
6. Start the application: `uvicorn src.main:app --reload`

For further details on each endpoint, refer to the specific sections above.