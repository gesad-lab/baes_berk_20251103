```python
"""
Teacher API Documentation

## Overview & Purpose
This section describes the Teacher API, which allows the creation and retrieval of Teacher entities. This functionality is essential for the educational institution to maintain records of teachers, including contact information.

## API Endpoints

### 1. Create a Teacher
- **Endpoint**: `/teachers`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Success Response**:
    - **Code**: 201 CREATED
    - **Content**:
    ```json
    {
        "message": "Teacher successfully created.",
        "teacher": {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    }
    ```

- **Error Responses**:
    - **Code**: 400 BAD REQUEST
      - Content:
      ```json
      {
          "error": {
              "code": "E001",
              "message": "Invalid input: name and email are required."
          }
      }
      ```
    - **Code**: 409 CONFLICT
      - Content:
      ```json
      {
          "error": {
              "code": "E002",
              "message": "A teacher with this email already exists."
          }
      }
      ```

### 2. Retrieve a Teacher
- **Endpoint**: `/teachers/<id>`
- **Method**: `GET`
- **Success Response**:
    - **Code**: 200 OK
    - **Content**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```

- **Error Responses**:
    - **Code**: 404 NOT FOUND
      - Content:
      ```json
      {
          "error": {
              "code": "E003",
              "message": "Teacher not found."
          }
      }
      ```

## Usage Example

### Create a Teacher
To create a new teacher, send a POST request to `/teachers` with the `name` and `email` fields in the request body.

Example:
```bash
curl -X POST http://localhost:5000/teachers \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

### Retrieve a Teacher
To retrieve an existing teacher by their identifier, send a GET request to `/teachers/<id>`.

Example:
```bash
curl -X GET http://localhost:5000/teachers/1
```

This request will return the details of the teacher with ID `1`.

"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

def initialize_database():
    engine = create_engine('sqlite:///database.db')  # Database connection
    Base.metadata.create_all(engine)  # Create tables if they do not exist
```