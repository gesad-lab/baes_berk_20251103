# Student Management Web Application

## Overview
The Student Management Web Application provides a simple interface to manage Student entities, allowing operations such as creating, retrieving, updating, and deleting Student records. Each Student has a required name field.

## Features
- **Create a Student**: Submit a name to create a new Student record.
- **Retrieve All Students**: View a list of all Students.
- **Update a Student**: Change the name of an existing Student.
- **Delete a Student**: Remove a Student from the database.

## API Endpoints

### 1. Create a Student
- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "John Doe"
  }
  ```
- **Response**:
  - **Status**: 201 Created
  - **Body**:
  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```

### 2. Retrieve All Students
- **Endpoint**: `GET /students`
- **Response**:
  - **Status**: 200 OK
  - **Body**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe"
    },
    {
      "id": 2,
      "name": "Jane Doe"
    }
  ]
  ```

### 3. Update an Existing Student
- **Endpoint**: `PUT /students/{id}`
- **Request Body**:
  ```json
  {
    "name": "John Smith"
  }
  ```
- **Response**:
  - **Status**: 200 OK
  - **Body**:
  ```json
  {
    "id": 1,
    "name": "John Smith"
  }
  ```

### 4. Delete a Student
- **Endpoint**: `DELETE /students/{id}`
- **Response**:
  - **Status**: 204 No Content (on successful deletion)

## Database Setup
- Upon application startup, the SQLite database schema will be initialized automatically. This includes creating the `students` table with a required `name` field if it does not already exist.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student-management.git
   cd student-management
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then set up a virtual environment and install the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the application using the following command:
   ```bash
   python app.py
   ```

4. **Access the API**:
   The API will be accessible at `http://localhost:5000`.

## Testing
To test the API, you can use tools like Postman or curl to make HTTP requests to the provided endpoints. Ensure to follow the request formats as specified above to create, retrieve, update, or delete Student records.

## License
This project is licensed under the MIT License. See the LICENSE file for details.