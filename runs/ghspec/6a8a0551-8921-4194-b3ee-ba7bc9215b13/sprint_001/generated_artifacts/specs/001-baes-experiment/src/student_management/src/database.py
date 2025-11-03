# README.md

# Student Management API

## Overview
The Student Management API is a simple web application that provides functionality to manage student entities. Each student entity consists of a single required field: `name`. This application uses an SQLite database to persist data and responds to API requests in JSON format. The API allows for creating new students and retrieving existing student details.

## Features
- Create a new Student entity with a required `name`.
- Retrieve details of an existing Student entity by Student ID.
- Automatically initializes the SQLite database schema on application startup.

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student_management.git
   cd student_management
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment:
   - Create a `.env` file in the root directory and provide your configuration variables if needed.

## Usage

### Starting the Application
To run the application, execute:
```bash
python src/app.py
```

The application will start on `http://localhost:5000` by default.

### API Endpoints

1. **Create a New Student**
   - **URL**: `/students`
   - **Method**: `POST`
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

2. **Retrieve Student Details**
   - **URL**: `/students/<id>`
   - **Method**: `GET`
   - **Response**:
     ```json
     {
       "id": 1,
       "name": "John Doe"
     }
     ```

### Error Handling
- If the `name` field is missing in the request body when creating a student, the API will respond with an error message indicating the issue.

## Testing
Automated tests are provided in the `tests/` directory. To run the tests, use:
```bash
pytest tests/
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Your Name (you@example.com)  

---

This `README.md` provides a comprehensive introduction to the Student Management API, including setup instructions and usage examples.