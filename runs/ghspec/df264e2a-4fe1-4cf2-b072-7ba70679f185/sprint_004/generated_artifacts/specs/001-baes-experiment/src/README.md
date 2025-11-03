# README.md

## Course Assignment and Student Retrieval Functionalities

This document outlines the newly implemented functionalities for associating students with courses and retrieving student information along with their enrolled courses in the student management system.

### API Endpoints

1. **Associate Student with Course**
   - **Endpoint**: `POST /students/{id}/courses`
   - **Description**: Assign a specific course to a student.
   - **Request Body**:
     ```json
     {
       "course_id": 1
     }
     ```
   - **Response**:
     - Success:
       ```json
       {
         "message": "Course assigned successfully."
       }
       ```
     - Error:
       ```json
       {
         "error": {
           "code": "E404",
           "message": "Invalid course ID provided."
         }
       }
       ```

2. **Retrieve Student with Courses**
   - **Endpoint**: `GET /students/{id}`
   - **Description**: Retrieve details of a student along with their enrolled courses.
   - **Response**:
     ```json
     {
       "student": {
         "id": 1,
         "name": "John Doe",
         "courses": [
           {
             "id": 1,
             "name": "Mathematics",
             "level": "Intermediate"
           },
           {
             "id": 2,
             "name": "Science",
             "level": "Advanced"
           }
         ]
       }
     }
     ```

### Testing Functionalities

Comprehensive tests have been added to ensure the proper functioning of course assignment and student retrieval functionalities. Below are the test scenarios implemented:

1. **Test: Associate Student with Course**
   - Validates that a student can be assigned to a course successfully.

2. **Test: Retrieve Student with Courses**
   - Ensures that student information is retrieved correctly along with their enrolled courses.

3. **Test: Error Handling for Invalid Course Assignment**
   - Confirms that an error is returned when trying to assign a non-existent course to a student.

4. **Test: Database Migration**
   - Validates that the application can initialize correctly and the database schema has been updated while retaining existing data integrity.

### Running the Tests

To execute the tests for the new functionalities, run the following command from the project root:

```bash
pytest tests/services/test_student.py
```

Ensure you have the necessary test dependencies installed before running the tests.

### Conclusion

These enhancements to the student management system improve the tracking of student enrollments and overall system functionality. Implementing these changes sets the stage for a more robust educational management experience for administrators and educators alike.