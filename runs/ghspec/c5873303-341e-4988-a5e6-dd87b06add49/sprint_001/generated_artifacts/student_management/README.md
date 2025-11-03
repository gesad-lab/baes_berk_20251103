# student_management/README.md

# Student Management Web Application

## Overview
The purpose of this web application is to manage student information efficiently. The application allows users to create and retrieve student records with a single field dedicated to the student's name. This functionality aims to provide simplicity and compatibility with various front-end frameworks through JSON responses.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [License](#license)

## Installation
To set up the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd student_management
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```bash
uvicorn src.main:app --reload
```
The application will start at `http://127.0.0.1:8000`.

### API Endpoints

1. **Create a New Student**
   - **Endpoint:** `POST /students`
   - **Request Body:**
     ```json
     {
       "name": "John Doe"
     }
     ```
   - **Expected Response:**
     ```json
     {
       "message": "Student created successfully",
       "student_id": 1
     }
     ```

2. **Retrieve All Students**
   - **Endpoint:** `GET /students`
   - **Expected Response:**
     ```json
     [
       {
         "name": "John Doe"
       },
       {
         "name": "Jane Doe"
       }
     ]
     ```

### Handling Errors
If a request is made without the required `name` field, the response will include an appropriate error message:
```json
{
  "error": {
    "code": "E001",
    "message": "The 'name' field is required.",
    "details": {}
  }
}
```

## Testing
Automated tests are included to verify the application's functionality. You can run the tests using:
```bash
pytest tests/test_students.py
```
The tests cover:
- Successful student creation.
- Retrieval of all students.
- Response handling for missing required fields.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.