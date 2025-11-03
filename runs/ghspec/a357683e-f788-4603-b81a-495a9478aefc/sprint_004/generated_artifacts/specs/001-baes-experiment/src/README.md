# README.md

# Project Title

A brief description of what this project does and who it's for.

## API Documentation

### Endpoints

#### Enroll a Student in a Course
- **Method**: `POST`
- **Endpoint**: `/students/{student_id}/courses`
- **Request Body**: 
  - `course_id`: integer (required)
- **Response**: 
  - `201 Created` with JSON confirmation of the enrollment, including student and course details.
  
##### Example Request:
```json
POST /students/1/courses
{
  "course_id": 2
}
```
##### Example Response:
```json
{
  "student_id": 1,
  "course_id": 2,
  "message": "Enrollment created successfully."
}
```

---

#### List a Student's Courses
- **Method**: `GET`
- **Endpoint**: `/students/{student_id}/courses`
- **Response**: 
  - `200 OK` with a JSON array of course records associated with the student, including course name and level.

##### Example Response:
```json
GET /students/1/courses
```
```json
[
  {
    "course_id": 2,
    "name": "Sample Course",
    "level": "Beginner"
  }
]
```

---

#### Unenroll a Student from a Course
- **Method**: `DELETE`
- **Endpoint**: `/students/{student_id}/courses/{course_id}`
- **Response**: 
  - `204 No Content` confirming the course has been successfully removed from the student's record.

##### Example Request:
```json
DELETE /students/1/courses/2
```

---

### Error Handling
- **Validation Error**:
  - If an admin attempts to enroll a student in a course that does not exist, the application will return an appropriate error message.

##### Example Response for Invalid Course:
```json
{
  "error": {
    "code": "E001",
    "message": "Course not found.",
    "details": {}
  }
}
```

---

## Testing User Scenarios

1. **Associating a Course with a Student**
2. **Retrieving a Student's Courses**
3. **Removing a Course from a Student**
4. **Validating Course Enrollment**

Ensure that each of these scenarios is covered by appropriate test cases in the testing suite, validating both successful and error cases.

---

## Configuration

### Environment Variables
- Make sure to set the necessary environment variables as outlined in the `.env.example` file. 

```plaintext
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.