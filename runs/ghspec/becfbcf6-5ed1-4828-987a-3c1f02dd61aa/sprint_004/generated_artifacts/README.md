# README.md

# Student Management Web Application

This is a simple API for managing students and courses in a student management system. It allows users to assign courses to students, retrieve courses for a student, and manage errors gracefully.

## API Endpoints

### Assign a Course to a Student

**Method**: `POST`  
**Endpoint**: `/students/{student_id}/courses`  
**Request Body**:
```json
{
    "course_id": 1
}
```

**Description**: This endpoint allows a user to assign a specific course to a student. The `student_id` should be replaced with the ID of the student, and the request body should contain the `course_id` of the course to assign.

**Success Response**:
- **Code**: `201 Created`
- **Content**:
```json
{
    "message": "Course assigned successfully.",
    "student_id": 1,
    "course_id": 1
}
```

**Error Response**:
- **Code**: `400 Bad Request`
- **Content**:
```json
{
    "error": {
        "code": "E001",
        "message": "Invalid course ID provided.",
        "details": {}
    }
}
```

### Retrieve Courses for a Student

**Method**: `GET`  
**Endpoint**: `/students/{student_id}/courses`  

**Description**: This endpoint retrieves a list of all courses associated with a specific student.

**Success Response**:
- **Code**: `200 OK`
- **Content**:
```json
{
    "courses": [
        {
            "id": 1,
            "name": "Introduction to Python",
            "level": "Beginner"
        },
        {
            "id": 2,
            "name": "Advanced Python",
            "level": "Advanced"
        }
    ]
}
```

## User Scenarios & Testing

1. **Assigning a Course to a Student**:
   - **Scenario**: A user assigns a specific course to a student.
   - **Test**: Verify that the student record is updated correctly to reflect the course assignment.

2. **Retrieving Courses for a Student**:
   - **Scenario**: A user requests to view all courses associated with a specific student.
   - **Test**: Verify that the response includes a list of courses that the student is enrolled in.

3. **Error on Assigning Invalid Course**:
   - **Scenario**: A user attempts to assign a course to a student using a course ID that does not exist.
   - **Test**: Verify that the API returns an error response indicating the course ID is invalid.

4. **Database Schema Update**:
   - **Scenario**: The application starts up with an updated schema reflecting the new relationship between Student and Course.
   - **Test**: Verify that the database allows for the association without affecting existing Student or Course data.

## Setup

To get started with the API, follow the steps below:

1. **Clone the repository**: 
   ```bash
   git clone [repository-url]
   cd [repository-directory]
   ```

2. **Install dependencies**: 
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations** to update your database schema:
   ```bash
   flask db upgrade
   ```

4. **Start the application**:
   ```bash
   flask run
   ```

Now your API should be set up and ready to use! You can test the endpoints with tools like Postman or curl.