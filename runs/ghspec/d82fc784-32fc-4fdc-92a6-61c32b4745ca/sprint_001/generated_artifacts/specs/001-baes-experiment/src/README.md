# Student Management API

This project provides a RESTful API for managing student records. It allows creating, retrieving, updating, and deleting student information.

## Table of Contents

- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## API Endpoints

### Create Student
- **Method**: POST
- **Endpoint**: `/students`
- **Request Body**: 
  ```json
  {
    "name": "Student Name"
  }
  ```
- **Success Response**:
  - **Status**: 201 Created
  - **Body**: JSON representation of the created student record.
  
### Retrieve Students
- **Method**: GET
- **Endpoint**: `/students`
- **Success Response**:
  - **Status**: 200 OK
  - **Body**: JSON array of student records.

### Update Student
- **Method**: PUT
- **Endpoint**: `/students/{id}`
- **Request Body**: 
  ```json
  {
    "name": "Updated Student Name"
  }
  ```
- **Success Response**:
  - **Status**: 200 OK
  - **Body**: JSON representation of the updated student record.

### Delete Student
- **Method**: DELETE
- **Endpoint**: `/students/{id}`
- **Success Response**:
  - **Status**: 204 No Content (indicating successful deletion).

## Database Schema

The application will automatically create the `students` table with the expected schema upon startup. Ensure that the database settings are correctly configured to allow table creation.

## Technology Stack

- Python
- Flask (or FastAPI, depending on implementation)
- SQLAlchemy or similar for ORM
- SQLite or PostgreSQL for the database

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-management-api.git
   ```
2. Navigate into the project directory:
   ```bash
   cd student-management-api
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```bash
   python app.py
   ```
2. Use a tool like Postman or curl to interact with the API.

### Example Requests:

- **Create Student**:
   ```bash
   curl -X POST http://localhost:5000/students -H "Content-Type: application/json" -d '{"name": "John Doe"}'
   ```

- **Retrieve Students**:
   ```bash
   curl -X GET http://localhost:5000/students
   ```

- **Update Student**:
   ```bash
   curl -X PUT http://localhost:5000/students/1 -H "Content-Type: application/json" -d '{"name": "John Smith"}'
   ```

- **Delete Student**:
   ```bash
   curl -X DELETE http://localhost:5000/students/1
   ```

## Contributing

Contributions are welcome! Please create a pull request for any features or fixes that you implement.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.