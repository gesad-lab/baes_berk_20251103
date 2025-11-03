# README.md

# Student Entity Web Application

## Overview
This application provides a simple API for managing student records, allowing users to create, read, update, and delete student entities from a SQLite database.

## API Endpoints

### 1. Create a Student
- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "string"  // Required
  }
  ```
- **Response**: Returns the created student object in JSON format.

### 2. Retrieve a Student
- **Endpoint**: `GET /students/{id}`
- **Response**: Returns the student object with the specified ID in JSON format.

### 3. Update a Student
- **Endpoint**: `PUT /students/{id}`
- **Request Body**:
  ```json
  {
    "name": "string"  // Required
  }
  ```
- **Response**: Returns the updated student object in JSON format.

### 4. Delete a Student
- **Endpoint**: `DELETE /students/{id}`
- **Response**: Returns a success message in JSON format.

## Database Interaction
The application automatically creates the following schema for the `Student` entity at startup:
- `id`: Primary Key
- `name`: String (required)

## Input Validation
The API enforces validation on the `name` field to ensure it is provided and in valid format. If validation fails, an appropriate error message will be returned in JSON format.

## Error Handling
Ensure that all API responses provide clear and actionable error messages for any invalid operations.

## Testing
All API endpoints have automated tests to ensure functionality:
- **CRUD Operations Tests** using `pytest`:
  - Test creating a new student
  - Test retrieving a student by ID
  - Test updating a student's name
  - Test deleting a student by ID

### Example Tests
```python
# Example of tests for CRUD operations in 'tests/test_students.py'

def test_create_student(client):
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert response.json['name'] == 'John Doe'

def test_get_student(client):
    response = client.get('/students/1')  # Assuming student ID 1 exists
    assert response.status_code == 200
    assert response.json['id'] == 1

def test_update_student(client):
    response = client.put('/students/1', json={'name': 'Jane Doe'})
    assert response.status_code == 200
    assert response.json['name'] == 'Jane Doe'

def test_delete_student(client):
    response = client.delete('/students/1')  # Assuming student ID 1 exists
    assert response.status_code == 204
```

## Conclusion
This README outlines the structure and functionality of the Student Entity Web Application, including detailed specifications for each API endpoint, database interactions, error handling requirements, and testing guidelines for robust application performance.