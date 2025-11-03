```markdown
# README.md

## Querying Tests for Teacher-Course Relationships

This document outlines the querying tests that validate the relationships between teachers and courses within the application.

### User Scenarios & Testing

1. **Assigning a Teacher to a Course**
   - **Scenario**: An admin wants to assign a teacher to a specific course.
   - **Test**: Validate that the system allows the assignment of a teacher to a course and correctly updates the course record in the database.
     - **Endpoint**: `PATCH /courses/{course_id}/assign-teacher`
       - **Request Body**: 
         ```json
         {
             "teacher_id": 1
         }
         ```
       - **Expected Response**: 
         ```json
         {
             "message": "Teacher assigned successfully",
             "course": {
                 "id": 1,
                 "name": "History 101",
                 "teacher": {
                     "id": 1,
                     "name": "Jane Smith"
                 }
             }
         }
         ```
       
2. **Retrieving Courses with Their Assigned Teacher**
   - **Scenario**: A user wants to view the details of a course along with its assigned teacher.
   - **Test**: Confirm that the application retrieves the course’s information, including the teacher's name, in a structured JSON format when queried.
     - **Endpoint**: `GET /courses/{course_id}`
     - **Expected Response**:
       ```json
       {
           "id": 1,
           "name": "History 101",
           "teacher": {
               "id": 1,
               "name": "Jane Smith"
           }
       }
       ```

3. **Removing a Teacher from a Course**
   - **Scenario**: An admin decides to remove a teacher's assignment from a course.
   - **Test**: Ensure that the application correctly removes the teacher from the course record while preserving other course data.
     - **Endpoint**: `PATCH /courses/{course_id}/remove-teacher`
     - **Expected Response**:
       ```json
       {
           "message": "Teacher removed successfully",
           "course": {
               "id": 1,
               "name": "History 101",
               "teacher": null
           }
       }
       ```

4. **Querying Courses of a Specific Teacher**
   - **Scenario**: A user wants to list all courses taught by a specific teacher.
   - **Test**: Validate that the application returns all courses associated with that teacher in an appropriate format.
     - **Endpoint**: `GET /teachers/{teacher_id}/courses`
     - **Expected Response**:
       ```json
       [
           {
               "id": 1,
               "name": "History 101"
           },
           {
               "id": 2,
               "name": "Math 201"
           }
       ]
       ```

### Conclusion

These tests ensure that the relationship between teachers and courses functions correctly and meets the specified requirements. Implementing and validating these scenarios will help maintain the integrity and usability of the application.
```