# README.md

---
# Student Management System

## Overview

The Student Management System facilitates educational management by allowing administrators to manage students, teachers, and courses effectively.

## Functionalities

### Assigning a Teacher to a Course

- The application allows administrators to assign a specific Teacher to a Course through an API endpoint.
- The `assign_teacher(course_id, teacher_id)` function checks if the provided `teacher_id` exists in the database before assignment.

### Retrieving Course Details with Teacher Information

- Users can view all details of a specific Course, including associated Teacher data.

## API Endpoints

### Assign Teacher to Course

- **Endpoint**: `POST /courses/{course_id}/assign-teacher`
- **Parameters**:
  - `course_id`: The ID of the course to which the teacher is to be assigned.
  - `teacher_id`: The ID of the teacher to be assigned.
- **Response**:
  - Confirmation message indicating successful assignment.
  - Error message if the `teacher_id` does not exist.

### Example Payload
```json
{
  "teacher_id": 1
}
```

### Error Response
```json
{
  "error": {
    "code": "E001",
    "message": "Teacher with ID 1 does not exist.",
    "details": {}
  }
}
```

## Database Schema Update

- The `Course` entity has been updated to include a new field `teacher_id`, which references the `Teacher` entity.
- Migrations ensure that existing data remains intact during the schema updates.

## Usage

Follow the instructions provided in the API documentation to utilize the functionalities of the Student Management System effectively.

---

## Technical Details

### Project Structure

```plaintext
student_management/
│
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py         # Add routes for assigning Teacher to Course and retrieving Course info
│   ├── models/
│   │   ├── __init__.py
│   │   ├── student.py        # Existing, no change
│   │   ├── course.py         # Update to include teacher_id
│   │   └── teacher.py        # Existing, no change
│   ├── services/
│   │   ├── __init__.py
│   │   └── course_service.py  # New service logic for Course-Teacher relationship handling
│   ├── dal/
│   │   ├── __init__.py
│   │   └── course_dal.py     # New file for Course CRUD operations including Teacher assignments
│   ├── app.py
│   └── config.py
│
├── migrations/
│   └── 002_add_teacher_relationship_to_courses.py # New migration for Course-Teacher relationship
│
├── tests/
│   ├── __init__.py
│   ├── test_student_routes.py  # Existing, no change
│   ├── test_student_service.py  # Existing, no change
│   ├── test_course_service.py   # Update to include tests for Teacher assignments
│   └── test_teacher_service.py   # Existing, no change
│
├── .env.example
├── requirements.txt
└── README.md
```

---