# Updated README.md for Course-Teacher API Documentation

# Course-Teacher API Documentation

## Overview

This API provides endpoints for managing courses and their associations with teachers. It allows you to update courses with teacher assignment and fetch course details including teacher information.

## API Endpoints

### 1. Update a Course with Teacher Assignment

**PATCH** `/courses/{course_id}`

- Updates an existing course to include a teacher association.

**Request Body:**
```json
{
    "teacher_id": "integer"
}
```

**Parameters:**
- `course_id`: The ID of the course you want to update.

**Responses:**
- **200 OK**: Successfully updated the course.
    - Example:
    ```json
    {
        "id": 1,
        "title": "Math 101",
        "teacher_id": 3,
        "teacher": {
            "id": 3,
            "name": "Jane Smith",
            "email": "jane.smith@example.com"
        }
    }
    ```
- **404 Not Found**: The course could not be found or updated due to validation issues.

**Error Handling:**
- The API will prevent assigning a teacher to multiple overlapping courses and respond with appropriate error messages if the condition fails.

### 2. Get Course Details

**GET** `/courses/{course_id}`

- Retrieves details for a specific course including its assigned teacher.

**Parameters:**
- `course_id`: The ID of the course you wish to view.

**Responses:**
- **200 OK**: Returns the course details along with the associated teacher's information.
    - Example:
    ```json
    {
        "id": 1,
        "title": "Math 101",
        "teacher": {
            "id": 3,
            "name": "Jane Smith",
            "email": "jane.smith@example.com"
        }
    }
    ```
- **404 Not Found**: The course could not be found.

## Database Migration

Ensure that the existing Course table schema is updated to include the `teacher_id` foreign key without data loss. The migration script is as follows:

```python
async def migrate_course_teachers():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("ALTER TABLE course ADD COLUMN teacher_id INTEGER REFERENCES teacher(id);")
        await db.commit()
```

## Validation Rules

- The API enforces validation to prevent a teacher from being assigned to multiple overlapping courses.

## Usage Example

### 1. Associating a Teacher with a Course

To associate a teacher with a course, send a PATCH request to `/courses/{course_id}` with the relevant `teacher_id`.

### 2. Checking Course Details

To view the course details including the assigned teacher, send a GET request to `/courses/{course_id}`.

## Conclusion

This API provides essential functionality for managing the relationships between courses and teachers. Follow the endpoints described to utilize the features effectively.

--- 

This completes the update to the README.md, detailing the functional requirements and new API endpoints for the Course-Teacher API.