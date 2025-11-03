# Student Management System

This project is a simple Student Management System API built with Flask and SQLite. It allows you to create and retrieve student records. 

## Table of Contents

- [Functional Requirements](#functional-requirements)
- [Project Structure](#project-structure)
- [Installation Instructions](#installation-instructions)
- [Usage Examples](#usage-examples)
- [Testing](#testing)

## Functional Requirements

1. **Create Student API**: 
   - **Endpoint**: `POST /students`
     - **Request Body**: 
       ```json
       { "name": "string" }
       ```
     - **Response**: 
       - **Success**: 
         - HTTP Status: `201 Created`
         - Response Body: 
           ```json
           { "id": "int", "name": "string" }
           ```
       - **Error**: 
         - HTTP Status: `400 Bad Request`
         - Response Body: 
           ```json
           { "error": "Name is required." }
           ```
       
2. **Retrieve Student API**: 
   - **Endpoint**: `GET /students/{id}`
     - **Response**: 
       - **Success**: 
         - HTTP Status: `200 OK`
         - Response Body: 
           ```json
           { "id": "int", "name": "string" }
           ```
       - **Error**: 
         - HTTP Status: `404 Not Found`
         - Response Body: 
           ```json
           { "error": "Student not found." }
           ```

## Project Structure

```plaintext
student_management/
│
├── src/
│   ├── app.py                  # Main application
│   ├── models.py               # Data models
│   ├── routes.py               # API endpoints
│   ├── services.py             # Business logic
│   ├── database.py             # Database setup and initialization
│   ├── schemas.py              # Data validation schemas
│
├── tests/
│   ├── test_routes.py          # Tests for API endpoints
│   ├── test_services.py        # Tests for business logic
│
├── requirements.txt            # Required packages
├── .env.example                 # Sample environment variables
├── README.md                   # Project documentation
```

## Installation Instructions

To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/student_management.git
   cd student_management
   ```

2. **Install dependencies**:
   Ensure you have Python and pip installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file**:
   Create a file named `.env` in the root directory and include the necessary environment variables. Use `.env.example` as a reference.

## Usage Examples

1. **Create a Student**:
   ```bash
   curl -X POST http://localhost:5000/students -H "Content-Type: application/json" -d '{ "name": "John Doe" }'
   ```

2. **Retrieve a Student by ID**:
   ```bash
   curl -X GET http://localhost:5000/students/1
   ```

## Testing

To run the tests for the API and service functionalities, you can execute:

```bash
pytest tests/
``` 

This will run all the tests defined in the `tests` directory. Ensure your environment is properly set up before running the tests.