# README.md

# Student Management Web Application

This application manages student enrollments and course registrations effectively. It provides APIs for enrolling students, retrieving their information, and managing course data.

## Functional Requirements

### 1. Enroll Student in Course Endpoint
- **Endpoint**: `POST /students/{student_id}/enroll`
- **Request Body**: 
  ```json
  {
    "course_ids": [1, 2, 3]
  }
  ```
  This body contains an array of course IDs that the student wishes to enroll in.
- **Response**: 
  - Returns a JSON representation of the updated Student, including an array of course objects that the student is now enrolled in.

### 2. Retrieve Student Details Endpoint
- **Endpoint**: `GET /students/{student_id}`
- **Response**: 
  - Returns a JSON representation of the specified Student entity, including their ID, name, and a list of enrolled courses.

### 3. Database Schema Update
- A new relationship between Student and Course entities must be established by implementing the following:
  - **Join Table**: `student_courses`
    - `student_id`: Integer (reference to Student entity)
    - `course_id`: Integer (reference to Course entity)
  - This table manages the many-to-many relationship between students and courses.

### 4. Data Validation
- Ensure that both the `student_id` and the provided `course_ids` in the enrollment request are valid. 
- If either the student or the course does not exist, the system will return a validation error.

## Database Migrations
- Ensure that the migration scripts are included in the deployment package.
- New API features must be verified through integration tests post-deployment.

## Documentation
- Update function docstrings and API documentation to encapsulate new functionalities, particularly concerning the enrollment feature.

## Setup Instructions
1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the environment variables as described in the `.env.example` file.
5. Run database migrations if applicable.
6. Start the application:
   ```bash
   python src/app.py
   ```

## Testing
- To run the tests, execute the following command:
  ```bash
  pytest
  ```

This documentation provides a clear and organized overview of the new features and updates for the Student Management Web Application. Make sure to review the API usage guidelines for effective integration.