# README.md

## Overview & Purpose
The purpose of this feature is to create a web application that allows users to manage student entities. Each student will have a mandatory name field, and the application will provide standard API functionality to create, retrieve, update, and delete student records. This will facilitate easy management and accessibility of student data within a simple web interface.

## API Endpoints

### **POST /students**
- **Description**: Create a student with a required name field.
- **Request Body**:
  ```json
  {
    "name": "string"  // Required: The name of the student.
  }
  ```
- **Responses**:
  - **201 Created**: Student was successfully created.
  - **400 Bad Request**: Invalid input (e.g., missing name field).

### **GET /students/{id}**
- **Description**: Retrieve details of a student by their ID.
- **URL Parameters**:
  - `id` (integer): The unique identifier for the student.
- **Responses**:
  - **200 OK**: Returns student details.
    ```json
    {
      "id": 1,
      "name": "string"  // The name of the student.
    }
    ```
  - **404 Not Found**: Student with given ID does not exist.

### **PUT /students/{id}**
- **Description**: Update the name of an existing student.
- **Request Body**:
  ```json
  {
    "name": "string" // Required: The new name of the student.
  }
  ```
- **URL Parameters**:
  - `id` (integer): The unique identifier for the student to be updated.
- **Responses**:
  - **200 OK**: Student name was successfully updated.
  - **400 Bad Request**: Invalid input or missing name field.
  - **404 Not Found**: Student with given ID does not exist.

### **DELETE /students/{id}**
- **Description**: Remove a student from the database.
- **URL Parameters**:
  - `id` (integer): The unique identifier for the student to be deleted.
- **Responses**:
  - **204 No Content**: Student was successfully deleted.
  - **404 Not Found**: Student with given ID does not exist.

## User Scenarios & Testing
1. **Create a Student**: 
   - As a user, I want to be able to create a new student by providing a name.
   - **Test**: Send a POST request with a valid name and verify that a student is created successfully.

2. **Get a Student**:
   - As a user, I want to retrieve the details of a specific student by their ID.
   - **Test**: Send a GET request for an existing student ID and verify that the correct student details are returned.

3. **Update a Student**:
   - As a user, I want to update an existing student's name.
   - **Test**: Send a PUT request with a valid student ID and a new name, then verify that the student's name is updated.

4. **Delete a Student**:
   - As a user, I want to delete a specific student from the database.
   - **Test**: Send a DELETE request for an existing student ID and verify that the student is removed from the records.

5. **Error Handling**:
   - If I send a request to create a student without a name, I should receive a `400 Bad Request` response indicating the error.

## Database
- Automatically create a SQLite database schema on application startup.
- Define a `Student` entity with a required `name` field.

## Response Format
- All API responses should be in JSON format.
- Error responses should include a standard error structure with a message and status code.

## 2. Pydantic Model for Validation
```python
from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1)

class StudentUpdate(BaseModel):
    name: str = Field(..., min_length=1)

class StudentResponse(BaseModel):
    id: int
    name: str
```