# Student Management API

This project is a simple Student Management API built with Flask and SQLAlchemy. It allows for basic operations such as adding and retrieving student information and is designed to serve as a foundational example for building more complex applications.

## Project Structure

```
/student_management_api
│
├── models/                     # Database models
│   └── student.py              # Student model
│
├── controllers/                # API controllers
│   └── student_controller.py    # Endpoints for student operations
│
├── schemas/                    # Request/Response schemas
│   └── student_schema.py        # Validation schema for student data
│
├── database/                   # Database initialization and handling
│   └── __init__.py             # Script to create the SQLite database
│
├── tests/                      # Unit tests
│   └── test_student.py          # Tests for student functionality
│
├── config.py                   # Configuration settings
│
└── README.md                   # Project documentation
```

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your_username/student_management_api.git
   cd student_management_api
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Install the required dependencies using:
   ```bash
   pip install Flask SQLAlchemy pytest flask_sqlalchemy
   ```

4. **Initialize the Database**:
   Set up the database by running the initialization script:
   ```bash
   python -m database
   ```

## API Endpoints

### Add Student

- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
      "name": "John Doe"
  }
  ```
- **Response**: 
  - `201 Created` if successful
  - `400 Bad Request` if validation fails
  
### Retrieve Students

- **Endpoint**: `GET /students`
- **Response**:
  - `200 OK` with a list of students

## Running Tests

To run the unit tests, execute:
```bash
pytest tests/
```

## Dependencies

- **Flask**: A web framework for building the API.
- **SQLAlchemy**: An ORM library for database operations.
- **pytest**: A testing framework for Python, to ensure code quality and functionality.

This README provides the necessary steps and information to set up and use the Student Management API effectively. For further instructions, refer to the code comments and additional documentation in the project files.