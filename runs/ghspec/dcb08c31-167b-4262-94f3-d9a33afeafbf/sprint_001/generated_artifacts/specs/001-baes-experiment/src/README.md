# README.md

# Student Management Web Application

This project is a simple Student Management Web Application that allows users to add, retrieve student records. The application uses Flask for the web framework and SQLite as the database for storing student information.

## Table of Contents
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Testing the Application](#testing-the-application)
- [Error Handling](#error-handling)

## Requirements
- Python 3.7 or higher
- Flask
- SQLite

## Setup Instructions

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd student-management-app
   ```

2. **Create a virtual environment**:
   This step is essential to manage dependencies effectively.
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required packages**:
   Use pip to install the necessary dependencies.
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   Start the Flask server.
   ```bash
   flask run
   ```

   The application will be accessible at `http://127.0.0.1:5000`.

## API Endpoints

### POST /students
- **Description**: Adds a new student record.
- **Request**:
   - Body: `{"name": "<student_name>"}`
- **Response**:
   - Success: Returns the created student object with a unique identifier.
   - Error: Returns an error message if the name field is missing.

### GET /students
- **Description**: Retrieves a list of all students.
- **Response**:
   - Returns a JSON array of all student records in the database.

## Testing the Application
Unit tests are included to verify the functionality of adding, retrieving student records and ensuring proper error handling. To run the tests, execute:
```bash
pytest
```

## Error Handling
The application provides informative error messages for various scenarios:
- **Empty Name Submission**: Returns an error response if the name field is left blank when adding a student.
- Appropriate status codes are included in error responses for invalid requests.

By following this guide, you should be able to set up and run the Student Management Web Application smoothly. For any further questions, please feel free to reach out!