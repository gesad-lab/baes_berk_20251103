# README.md

# Student Management Application

## Overview & Purpose
The purpose of this feature is to create a simple web application that facilitates the management of a Student entity, with a focus on the name field. This application allows users to perform basic operations such as creating, retrieving, and managing student records, providing a robust framework for handling student information efficiently. By employing best practices in web application development, this feature aims to ensure maintainability, scalability, and clarity in the design.

## Technology Stack
- **Backend Framework**: FastAPI (for creating RESTful APIs with high performance)
- **Database**: SQLite (for lightweight and easy data storage)
- **ORM**: SQLAlchemy (for database interaction)
- **Testing Framework**: pytest (for running unit tests)
- **Documentation**: OpenAPI (auto-generated with FastAPI)

## Application Structure
```plaintext
project-root/
├── src/
│   ├── main.py               # Entry point for the FastAPI application
│   ├── models/                # Database models
│   │   └── student.py         # Student model definition
│   ├── schemas/               # Pydantic schemas for validation
│   │   └── student.py         # Schema for Student input/output
│   ├── services/              # Business logic layer
│   │   └── student_service.py  # Logic for managing students
│   ├── db/                   # Database setup
│   │   └── database.py        # Database connection and schema creation
│   └── api/                  # API routes
│       └── student_routes.py   # Routes for student-related endpoints
├── tests/                     # Test suite
│   ├── test_student.py        # Unit tests for student-related functionalities
├── requirements.txt           # Project dependencies
├── .env.example               # Example environment configuration
└── README.md                  # Project documentation
```

## Setup Instructions

To set up the Student Management Application, follow these steps:

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### Create a Virtual Environment
It is a good practice to use a virtual environment to manage dependencies.
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
Install the project dependencies specified in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Configure the Environment
Create a `.env` file based on the provided example to configure environment variables:
```bash
cp .env.example .env
```
Modify the `.env` file to include any necessary configuration settings.

### Running the Application
To run the application, execute the following command:
```bash
uvicorn src.main:app --reload
```
This will start the FastAPI application at `http://127.0.0.1:8000`.

### Accessing the API Documentation
Once the application is running, you can access the auto-generated API documentation at:
- OpenAPI (Swagger UI): `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### Running Tests
To run the tests in the project, execute:
```bash
pytest
```

## User Scenarios & Testing

1. **Scenario: Create a Student**
   - As a user, I want to create a new student by providing their name so that I can keep track of students in the system.
   - **Test Steps**:
     1. Send a POST request to `/students` with the student name in the request body.
     2. Assert that the response status is 201 Created.
     3. Validate that the response body contains the created student's ID and name.

2. **Scenario: Retrieve a Student**
   - As a user, I want to fetch the details of a student by their ID to view their information.
   - **Test Steps**:
     1. Send a GET request to `/students/{id}`.
     2. Assert that the response status is 200 OK.
     3. Validate that the response body contains the student's ID and name.

3. **Scenario: Retrieve All Students**
   - As a user, I want to see a list of all students to easily manage student records.
   - **Test Steps**:
     1. Send a GET request to `/students`.
     2. Assert that the response status is 200 OK.
     3. Validate that the response is an array of students, each containing an ID and name.

## Success Criteria
- The application must successfully create the database schema during startup without requiring manual intervention.
- The API must return JSON responses compliant with specified formats.
- The application should have unit tests ensuring at least 70% coverage of business logic.
- All specified API endpoints must function as intended and return appropriate status codes.