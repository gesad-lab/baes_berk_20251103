# README.md

# Project Title

## Description
This project is an API service for managing student records.

## Requirements
This project requires the following dependencies:

- **FastAPI**: A modern web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **SQLAlchemy**: The Python SQL toolkit and Object-Relational Mapping (ORM) system.
- **Pytest**: A testing framework that makes building simple and scalable test cases easy.

## Installation
To install the required dependencies, run the following command:

```bash
pip install fastapi[all] sqlalchemy pytest
```

## Usage
Run the FastAPI application with the command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

You can access the API documentation at `http://localhost:8000/docs`.

## API Endpoints
### Create Student (POST /students)
- **Request Body**:
  ```json
  {
    "name": "John Doe"
  }
  ```
- **Response**:
  - **201 Created**:
  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```
  - **400 Bad Request** (if name is missing):
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Name is required."
    }
  }
  ```

### Retrieve Students (GET /students)
- **Response**:
  - **200 OK**:
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

## Running Tests
To run the test suite, execute:

```bash
pytest
```

## License
This project is licensed under the MIT License.