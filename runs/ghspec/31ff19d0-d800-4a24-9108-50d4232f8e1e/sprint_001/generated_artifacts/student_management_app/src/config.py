# README.md

# Student Management Application

This Student Management Application allows users to create and retrieve student records through a RESTful API. The application uses a SQLite database for data storage and is built using Flask.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [API Usage Examples](#api-usage-examples)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student_management_app.git
   cd student_management_app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python src/app.py
   ```

4. The application will create the SQLite database schema on startup.

## API Usage Examples

### 1. Create Student API Endpoint

- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "John Doe"
  }
  ```

- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```

**Example using cURL**:
```bash
curl -X POST http://localhost:5000/students \
-H "Content-Type: application/json" \
-d '{"name": "John Doe"}'
```

### 2. Retrieve All Students API Endpoint

- **Endpoint**: `GET /students`

- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe"
    },
    {
      "id": 2,
      "name": "Jane Smith"
    }
  ]
  ```

**Example using cURL**:
```bash
curl -X GET http://localhost:5000/students
```

## License

This project is licensed under the MIT License.

## Acknowledgments

- Flask for the web framework
- SQLite for database management


---