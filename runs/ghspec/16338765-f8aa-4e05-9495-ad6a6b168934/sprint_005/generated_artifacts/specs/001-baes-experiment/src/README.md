# README.md

# Project Documentation

## Overview

This project is designed to handle the management of teacher records in an educational system, providing API endpoints for creating, retrieving, and updating teacher information. We utilize Pydantic models for data validation to ensure that input data is well-formed and adheres to required formats.

## API Endpoints

### Teacher Management

#### Create a Teacher
- `POST /teachers`
- **Request Body**: 
```json
{
  "name": "string",
  "email": "string@example.com"
}
```
- **Response**:
  - **Success**: Returns the created teacher's ID, name, and email.
  - **Error**: Returns appropriate error messages for invalid inputs.

#### Retrieve a Teacher
- `GET /teachers/{teacher_id}`
- **Response**:
  - **Success**: Returns the teacher's details.
  - **Error**: Returns an appropriate error message if the teacher does not exist.

#### Update a Teacher
- `PUT /teachers/{teacher_id}`
- **Request Body**: 
```json
{
  "name": "string",
  "email": "string@example.com"
}
```
- **Response**:
  - **Success**: Returns the updated teacher's details.
  - **Error**: Returns appropriate error messages for invalid inputs or if the teacher does not exist.

## Input Validation with Pydantic

We are using Pydantic models to validate the input for the teacher management API. Below are the models used:

### Teacher Models

```python
from pydantic import BaseModel, EmailStr

class TeacherCreate(BaseModel):
    name: str  # Required field for teacher's name
    email: EmailStr  # Required field for teacher's email

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
```

### Error Handling

When invalid input is detected (e.g., incorrect email format), clear error messages will be returned to guide the user on how to correct their submissions. The error response will follow this structure:

```json
{
  "error": {
    "code": "E001", 
    "message": "Invalid email format. Please provide a valid email address.",
    "details": {}
  }
}
```

## Future Development

Further enhancements will include additional validations, connection to a database for persistent storage, and comprehensive testing of all API endpoints to ensure reliability and correctness.