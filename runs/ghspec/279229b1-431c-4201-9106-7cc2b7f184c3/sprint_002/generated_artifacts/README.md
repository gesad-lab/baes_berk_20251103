# README.md

# Project Title

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/projectname.git
   cd projectname
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

## API Usage

### 1. Create Student
- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "string",
    "email": "string"
  }
  ```
- **Response**:
  - On success:
    ```json
    {
      "status": "success",
      "student": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    }
    ```
  - On error (e.g., missing email):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Email field is required."
      }
    }
    ```

### 2. Retrieve Students
- **Endpoint**: `GET /students`
- **Response**:
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

### 3. Update Student
- **Endpoint**: `PUT /students/{id}`
- **Request Body**:
  ```json
  {
    "email": "new.email@example.com"
  }
  ```
- **Response**:
  - On success:
    ```json
    {
      "status": "success",
      "student": {
        "id": 1,
        "name": "John Doe",
        "email": "new.email@example.com"
      }
    }
    ```
  - On error (e.g., invalid email format):
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Invalid email format."
      }
    }
    ```

## Testing

To run the integration tests, use the following command:
```bash
pytest tests/test_integration.py
```

To run the unit tests for student functionality, use:
```bash
pytest tests/test_student.py
``` 

Ensure all tests pass to confirm functionality is as expected.