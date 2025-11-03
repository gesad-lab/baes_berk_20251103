# student_management/README.md

# Student Management API

## Overview
The Student Management API is a web application designed to manage student entities with capabilities to create and retrieve student records. 

## Directory Structure
```
student_management/
├── src/
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   ├── database.py
│   ├── validation.py
│   └── serialization.py
├── tests/
│   └── test_routes.py
├── requirements.txt
└── README.md
```

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_management
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed and use pip to install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Navigate to the `src` directory, and execute the following command:
   ```bash
   python app.py
   ```
   The application will start on `http://127.0.0.1:5000`.

## API Endpoints

### Create a New Student
- **Endpoint**: `POST /students`
- **Request Body**:
    ```json
    {
      "name": "John Doe"
    }
    ```
- **Success Response** (201):
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```
- **Error Response** (400):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name is required."
      }
    }
    ```

### Retrieve Student Details
- **Endpoint**: `GET /students/<id>`
- **Success Response** (200):
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```
- **Error Response** (404):
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

## Database Initialization
Upon starting the application, the database schema for the Student entities is automatically created if it does not already exist.

## Testing
- Automated tests are included in the `tests` directory. Run the tests using:
  ```bash
  pytest
  ```

## License
This project is licensed under the MIT License - see the LICENSE file for details.