```python
# docs/api_documentation.py

"""
API Documentation
=================
This document provides details about the API endpoints available in the application.

Endpoints
---------
1. **Courses**
   - **POST /courses**
     - Create a new course.
     - Request Body:
       ```json
       {
         "name": "string",  // Course name, required
         "level": "string"  // Course level, required
       }
       ```
     - Responses:
       - `201 Created`: Return course object if successful.
       - `400 Bad Request`: If course name or level is invalid.

   - **GET /courses**
     - Retrieve all courses.
     - Responses:
       - `200 OK`: Returns a list of all courses.

2. **Students**
   - **POST /students**
     - Create a new student.
     - Request Body:
       ```json
       {
         "name": "string",   // Student name, required
         "email": "string"   // Student email, required
       }
       ```
     - Responses:
       - `201 Created`: Return student object if successful.
       - `400 Bad Request`: If student name or email is invalid.

   - **GET /students**
     - Retrieve all students.
     - Responses:
       - `200 OK`: Returns a list of all students.

   - **POST /students/{student_id}/courses**
     - Enroll a student in a course.
     - Request Body:
       ```json
       {
         "course_id": "integer"  // ID of the course to enroll, required
       }
       ```
     - Responses:
       - `200 OK`: Enrolls the student successfully.
       - `400 Bad Request`: Invalid course ID or student ID.
       - `404 Not Found`: If student or course does not exist.

   - **GET /students/{student_id}/courses**
     - Retrieve courses for a specific student.
     - Responses:
       - `200 OK`: Returns a list of courses for the given student.
       - `404 Not Found`: If student does not exist.

Versioning
----------
This API is versioned. Future changes may introduce breaking changes without prior notice.

Contact
-------
For inquiries, please contact the API support team at support@example.com.
"""
```