# README.md

# Student Entity Management System

## Overview
The objective of this web application is to manage a Student entity, focusing primarily on storing and managing student information by their names. The application enables the addition, retrieval, and management of student records, improving organizational efficiency in tracking student data.

## User Scenarios
1. **As an admin, I want to create a new student entry with a name:** Upon providing a valid name, the system will successfully create a new student record.
2. **As an admin, I want to retrieve the student data:** The admin should be able to request all stored student records and receive them in JSON format.
3. **As an admin, I want to receive an error message when creating a student with an empty name:** If the name field is empty, the system will provide a clear error message indicating that it is required.

## Functional Requirements
- **Create Student**
  - **Endpoint**: `POST /students`
  - **Request Body**: JSON object containing `{ "name": "string" }` (name is required)
  - **Response**: 
    - `201 Created` with the created student details or 
    - `400 Bad Request` if the name is missing.

- **Get All Students**
  - **Endpoint**: `GET /students`
  - **Response**: 
    - `200 OK` with a JSON array of student records.

- **Error Handling**
  - Requests with missing required fields will return an error in the format:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name is required."
      }
    }
    ```
 
## Database Initialization
The application automatically creates the SQLite database schema on startup. It initializes a `students` table containing:
- `id` (integer, primary key)
- `name` (text, not null)

## Setup Instructions

To set up the project, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/student-management.git
   cd student-management
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**
   Install the necessary packages with pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   Start the application:
   ```bash
   python app.py
   ```
   The application should now be running on `http://localhost:5000`.

5. **Testing the API Endpoints**
   - Use a tool like Postman or curl to interact with the API:
     - **Create a student**:
       ```bash
       curl -X POST http://localhost:5000/students -H "Content-Type: application/json" -d '{"name": "John Doe"}'
       ```
     - **Get all students**:
       ```bash
       curl http://localhost:5000/students
       ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 

## Contributing
Contributions are welcome! Please submit a pull request for any major changes or enhancements.