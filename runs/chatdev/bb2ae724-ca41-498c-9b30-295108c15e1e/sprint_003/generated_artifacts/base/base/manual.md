Here's a detailed user manual for the Student API web application, structured in Markdown format:

```markdown
# Student API Web Application

A simple web application for managing Student entities using FastAPI and SQLite.

## Overview

This application allows users to create and retrieve student records. Each student has a name, which is a required field. The application provides a RESTful API that returns JSON responses.

## Main Functions

- **Create a Student**: Allows the user to create a new student by providing a name.
- **Retrieve a Student**: Allows the user to retrieve a student's details using their unique ID.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the FastAPI Server**:
   Run the following command to start the server:
   ```bash
   python main.py
   ```
   The server will start at `http://127.0.0.1:8000`.

2. **Access the API Documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

## Using the Application

### Creating a Student

1. **Using the GUI**:
   - Run the GUI application:
     ```bash
     python gui.py
     ```
   - Enter the student's name in the input field and click the "Create Student" button. If successful, the application will display the created student's name.

2. **Using API Endpoints**:
   You can also create a student using a tool like Postman or cURL:
   - **POST Request**:
     ```bash
     curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe"}'
     ```

### Retrieving a Student

- **GET Request**:
  To retrieve a student by their ID, use the following endpoint:
  ```bash
  curl -X GET "http://127.0.0.1:8000/students/{student_id}"
  ```
  Replace `{student_id}` with the actual ID of the student you want to retrieve.

## Conclusion

This Student API web application provides a simple interface for managing student records. It utilizes FastAPI for the backend and SQLite for data persistence, making it lightweight and easy to use. For further enhancements, consider adding more fields to the Student entity or implementing additional features such as updating and deleting student records.

For any issues or feature requests, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand and utilize the Student API web application effectively.