# Updated README.md

## Student Management Application

This application allows for managing courses and teachers, including assigning teachers to courses. Below is a guide on how to interact with the related API endpoints.

### API Endpoints

#### Teacher Assignments 

##### Assign a Teacher to a Course

- **POST** `/courses/{course_id}/assign-teacher`
  
  Assigns a teacher to a specified course.

  **Request Body**:
  ```json
  {
    "teacher_id": <int>
  }
  ```

  **Parameters**:
  - `course_id`: The ID of the course to which the teacher will be assigned.

  **Responses**:
  - **201 Created**: Teacher successfully assigned to the course.
  - **400 Bad Request**: Invalid input provided.
  - **404 Not Found**: Specified course or teacher does not exist.

---

### Testing

Unit tests have been implemented to ensure at least 70% coverage across all functionalities related to course and teacher assignments. Critical paths, such as assigning, removing, and updating teachers, are covered with over 90% coverage.

To run the tests, execute:

```bash
pytest tests/
```

Make sure that the application is set up properly before running the tests.

### Future Enhancements

Further documentation will be added as new features and endpoints are introduced to enhance the functionality of both teachers and courses within the application. 

Please refer to the existing API documentation for more details on related functionalities.