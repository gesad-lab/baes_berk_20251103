# README.md

# Student Management API

The Student Management API provides a simple web application for managing student records. This application enables users to create, read, update, and delete (CRUD) student entities, where each student has a required name field. This system can be easily integrated into larger educational systems or applications.

## Overview & Purpose

The purpose of this feature is to facilitate the management of student data effectively. It allows users to maintain student records, ensuring that all operations return accurate data while initializing the database schema without manual intervention upon startup.

## API Endpoints

### Create Student
- **Endpoint**: `POST /students`
- **Request Body**: 
  ```json
  {
    "name": "string"
  }
  ```
  _(Name is a required field)_
  
- **Response**: 
  ```json
  {
    "id": "integer",
    "name": "string"
  }
  ```

### Retrieve All Students
- **Endpoint**: `GET /students`
- **Response**: 
  ```json
  [
    {
      "id": "integer",
      "name": "string"
    }
  ]
  ```

### Update Student
- **Endpoint**: `PUT /students/{id}`
- **Request Body**: 
  ```json
  {
    "name": "string"
  }
  ```
  _(Name is a required field)_

- **Response**: 
  ```json
  {
    "id": "integer",
    "name": "string"
  }
  ```

### Delete Student
- **Endpoint**: `DELETE /students/{id}`
- **Response**: `204 No Content` (on success)

## Database Initialization

The database schema will be automatically created on startup, including a Students table with `id` and `name` fields.

## Development Setup

To run this project, ensure you have [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed. Follow the steps below to set up the project:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd student_management
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Environment Variables**
   Create a `.env` file following the structure provided in `.env.example` to store configuration settings.

5. **Run the Application**
   Start the application using:
   ```bash
   python src/app.py
   ```

## Testing

To run tests for this application, use the following command:
```bash
pytest
```

Ensure all tests are passing to verify the functionality of the API.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or enhancements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.