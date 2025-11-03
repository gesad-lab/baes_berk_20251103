# README.md

# Student Management App

This application is designed to manage student data efficiently. It provides RESTful API endpoints to create and retrieve student records. 

## Functional Requirements

1. **Update Student API Endpoint**
   - **Endpoint**: `POST /students`
   - **Request Body**: 
     - `name`: string (required)
     - `email`: string (required, must be a valid email format and unique)
   - **Response**:
     - Returns a JSON object with the created student's details, including a unique identifier and email.

   **Example Request**:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

   **Example Response**:
   ```json
   {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

2. **Retrieve All Students API Endpoint**
   - **Endpoint**: `GET /students`
   - **Response**:
     - Returns a JSON array containing all students with their names, emails, and identifiers.

   **Example Response**:
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

## Database Schema Update

- Modify the existing `Student` table in the database to include a new field:
  - `email`: string (required)

- Implement a migration script that preserves existing student data while adding the `email` field to accommodate new entries.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_management_app
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**:
   To apply database migrations and update the schema, run:
   ```bash
   python migrations.py
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

## API Documentation

- This API can be documented using Swagger/OpenAPI or Postman. For automatic generation of API docs, reference the routes defined in `routes.py` and include the necessary specifications.

## Technology Stack

- **Programming Language**: Python 3.x
- **Web Framework**: Flask
- **Database**: SQLite (for simplicity in development and deployment)
- **Dependency Management**: pip and requirements.txt
- **Testing Framework**: pytest
- **API Documentation**: Swagger/OpenAPI or Postman

## Contributing

Please feel free to submit issues, fork the repository, and create pull requests for enhancements!