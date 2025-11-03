# README.md

# Student Entity App

## Overview
The purpose of this application is to manage student data, ensuring efficient handling and storage of important information. This includes functionality to add students, retrieve student details, and manage email addresses associated with each student.

## New Feature: Email Field in Student Entity
As of the latest update, the Student entity now includes a required email field. This enhancement allows the application to capture and store students' email addresses, facilitating future communication. The implementation guarantees that existing student data remains intact during this schema update.

### User Scenarios
1. **Add Student with Email**
   - **Given:** The user submits a new student with a name and an email address.
   - **When:** The API receives the valid inputs.
   - **Then:** The student is added to the database with both the name and email, returning a success JSON response.

   **Example Request:**
   ```json
   POST /students
   {
     "name": "John Doe",
     "email": "john.doe@example.com"
   }
   ```

   **Example Response:**
   ```json
   {
     "message": "Student added successfully",
     "data": {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
   }
   ```

2. **Retrieve All Students with Email**
   - **Given:** There are students in the database with email addresses.
   - **When:** The user requests the list of students.
   - **Then:** The API returns a JSON array of all students with their names and email addresses.

   **Example Request:**
   ```json
   GET /students
   ```

   **Example Response:**
   ```json
   [
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
     },
     {
       "id": 2,
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
     }
   ]
   ```

3. **Handle Missing Email Input**
   - **Given:** The user submits a new student with a name but without an email.
   - **When:** The API receives the request.
   - **Then:** The API returns a JSON error response indicating that the email is required.

   **Example Request:**
   ```json
   POST /students
   {
     "name": "John Doe"
   }
   ```

   **Example Response:**
   ```json
   {
     "error": {
       "code": "E001",
       "message": "Email is required."
     }
   }
   ```

4. **Database Migration Validation**
   - After the database migration, verify that existing student data is preserved and returned correctly with the required schema.

## Directory Structure
```plaintext
student_entity_app/
│
├── src/
│   ├── __init__.py
│   ├── main.py                     # Entry point for the application
│   ├── models.py                   # Database models (SQLAlchemy)
│   ├── schemas.py                  # Data validation schemas (Pydantic)
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── student_routes.py        # API routes for student endpoints
│   └── database.py                  # Database connection and initialization
│
├── tests/
│   ├── __init__.py
│   └── test_student.py              # Test cases for student routes
│
├── config/
│   └── .env                         # Environment variables
│
├── requirements.txt                 # Dependencies file
└── README.md                        # Project documentation
```

## Installation Instructions
1. Clone the repository to your local machine.
2. Change into the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
4. Set up the environment variables in the `.env` file.

## Usage
To run the application, execute:
```
python src/main.py
```

You can interact with the application through the provided API endpoints using tools like Postman or curl.