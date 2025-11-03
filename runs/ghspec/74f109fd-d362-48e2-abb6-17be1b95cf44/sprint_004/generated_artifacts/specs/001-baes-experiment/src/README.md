# README.md

## API Documentation

### Enroll Student in Course

**Endpoint**: `POST /api/v1/enrollments`  
**Description**: Enrolls a student in a specified course.  
**Request Body**:
```json
{
    "student_id": "integer",
    "course_id": "integer"
}
```
**Response**:  
- **201 Created**: Successfully enrolled the student in the course.
```json
{
    "message": "Student enrolled successfully."
}
```
- **400 Bad Request**: Invalid input, such as missing or incorrect student_id or course_id.
```json
{
    "error": {
        "code": "E001",
        "message": "Invalid student or course ID."
    }
}
```

### Get Courses by Student

**Endpoint**: `GET /api/v1/students/{student_id}/courses`  
**Description**: Retrieves the list of courses a student is enrolled in.  
**Response**:  
- **200 OK**: Returns a list of courses the student is enrolled in.
```json
{
    "courses": [
        {
            "course_id": "integer",
            "course_name": "string"
        },
        ...
    ]
}
```
- **404 Not Found**: Student with the given ID does not exist.
```json
{
    "error": {
        "code": "E002",
        "message": "Student not found."
    }
}
```

### Database Updates

- **Table: `student_courses`**  
  This join table connects students and courses for many-to-many relationships:
```sql
CREATE TABLE student_courses (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

### Next Steps

- Ensure the API endpoints are tested thoroughly, covering both successful enrollments and various error scenarios.
- Review and validate requests and responses for compliance with the specified formats. 

---

This update documents the new API endpoints related to student enrollment in courses and outlines necessary details including request and response formats, as well as database schema changes. Further modifications may include additional functionalities as the project evolves.