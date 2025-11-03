# README.md

# Student Management API

This project is a simple RESTful API for managing student information. It allows users to create and retrieve student records.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
  - [Create Student](#create-student)
  - [Retrieve Student](#retrieve-student)
- [Database Schema](#database-schema)

## Setup Instructions

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/student-management-api.git
   cd student-management-api
   ```

2. **Create a virtual environment**:
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   Install the required Python packages using pip.
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the repository root based on the `.env.example` provided. This file should contain your configuration settings. Modify any values as necessary.

5. **Run the application**:
   Start the Flask application locally.
   ```bash
   flask run
   ```

The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### Create Student

- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "string"  // Required
  }
  ```
- **Response**:
  - **Success**: 
  ```json
  {
    "id": "integer",
    "name": "string"  // The name provided
  }
  ```
  - **Error**:
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Name field is required."
    }
  }
  ```

### Retrieve Student

- **Endpoint**: `GET /students/{id}`
- **Response**:
  - **Success**:
  ```json
  {
    "id": "integer",
    "name": "string"
  }
  ```
  - **Error**: If the student is not found.
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Student not found."
    }
  }
  ```

## Database Schema

Upon application startup, a SQLite database schema will be automatically created. The `Student` table will include:
- `id`: integer, primary key, auto-incremented
- `name`: string, required

This schema ensures data persistence across application restarts.

For detailed API documentation and usage guidelines, please refer to the [API Documentation](docs/api.md).