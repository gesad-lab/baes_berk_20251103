# README.md

# Student Management API

This repository contains a simple Student Management API that allows for the creation and retrieval of student records. Below are setup instructions and details on how to use the API.

## Table of Contents

- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
  - [Create Student](#create-student)
  - [Retrieve Student](#retrieve-student)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with this API, you need to clone the repository and install the required dependencies.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-management-api.git
   cd student-management-api
   ```

2. Install dependencies (replace with your package manager if necessary):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

The API should now be running on `http://localhost:5000`.

## API Endpoints

### Create Student

- **Endpoint**: `POST /students`
  
- **Request Body**:
  ```json
  {
    "name": "John Doe"
  }
  ```

- **Responses**:
  - **Success (201 Created)**:
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```
  - **Error (400 Bad Request)**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name field is required."
      }
    }
    ```

### Retrieve Student

- **Endpoint**: `GET /students/<id>`

- **Responses**:
  - **Success (200 OK)**:
    ```json
    {
      "name": "John Doe"
    }
    ```
  - **Error (404 Not Found)**:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

## Error Handling

All error responses follow a consistent format, providing an error code and message to aid in diagnosing issues.

## Contributing

Contributions are welcome! Please submit a pull request or create an issue for any feature requests or bug reports.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.