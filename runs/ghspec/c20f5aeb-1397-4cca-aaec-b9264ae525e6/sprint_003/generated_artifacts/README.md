# README.md

# Student Management System

This project is a Student Management System designed for managing student data, course information, and associated functionalities.

## Deployment Steps

To deploy the Student Management System, follow these steps:

1. **Prepare the Environment**:
   - Ensure you have Python 3.8+ installed on your machine.
   - Install required packages from `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

2. **Database Migrations**:
   - Ensure that the migration scripts are included in the deployment package for database updates.
   - Run the database migrations:
     ```bash
     flask db upgrade
     ```

3. **Service Checks**:
   - Before going live, verify that the new Course endpoint functionality works as expected. You can test the endpoints using Postman or cURL.

4. **Run the Application**:
   - Start the application:
     ```bash
     flask run
     ```
   - The application should be running on `http://127.0.0.1:5000/`.

5. **Verify Application Functionality**:
   - Once the application is running, test the endpoints for both Student and Course resources to ensure they are functioning correctly.

6. **Monitor Application Logs**:
   - Check the application logs for any potential issues during startup or while handling requests.

## New Courses Functionality

With this deployment, the following new Course-related features have been added:

- **Course Model**: A new course model has been introduced to represent course details in the database.
- **API Endpoints**:
  - `POST /courses`: Create a new course
  - `GET /courses`: Retrieve a list of all courses
  - `GET /courses/<course_id>`: Retrieve details for a specific course
  - `PUT /courses/<course_id>`: Update an existing course
  - `DELETE /courses/<course_id>`: Delete a specific course

Documentation for these endpoints is available in the API section below.

## API Documentation

- **POST /students**: Create a new student
- **GET /students**: Retrieve a list of all students
- **GET /students/<student_id>**: Retrieve details for a specific student
- **PUT /students/<student_id>**: Update an existing student
- **DELETE /students/<student_id>**: Delete a specific student

- **New Course Endpoints**: 
  - `POST /courses`, `GET /courses`, `GET /courses/<course_id>`, `PUT /courses/<course_id>`, `DELETE /courses/<course_id>`

For detailed information on request and response formats, please refer to the API documentation in the project's codebase.