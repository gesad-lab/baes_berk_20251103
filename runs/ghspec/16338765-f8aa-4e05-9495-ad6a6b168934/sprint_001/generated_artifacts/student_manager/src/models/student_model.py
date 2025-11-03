# README.md

# Student Manager

## Overview & Purpose
The Student Manager is a web application designed to manage student records efficiently. It focuses on adding and retrieving information about students, accommodating functionalities that allow administrators and users to interact seamlessly with the student data.

## Prerequisites
- Python 3.11 or higher
- FastAPI framework
- SQLite database

Ensure that you have these installed and available in your environment.

## Getting Started

### 1. Set Up Environment
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd student_manager
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Database Setup
- The application uses SQLite as a lightweight persistence layer. The database setup is outlined in `src/database/db_setup.py`, which takes care of creating the necessary tables on startup.

### 3. Run the Application
To start the application, use the following command:
```bash
uvicorn src.main:app --reload
```
This will start the FastAPI server locally at `http://127.0.0.1:8000`.

## User Scenarios
### Create a Student
As an admin, you can add a new student with a name using the POST request to `/students`.

### Retrieve All Students
Any user can view a list of all registered students by making a GET request to `/students`.

### Retrieve a Single Student
Users can access details of a specific student by their ID by sending a GET request to `/students/{id}`.

## API Endpoints
- **POST /students**: Create a new student
  - Request Body: `{"name": "Student Name"}`

- **GET /students**: Retrieve a list of all students
  - Response: A list of students with their IDs and names.

- **GET /students/{id}**: Retrieve a specific student by ID
  - Response: Student details including ID and name.

## Testing
Unit tests for each user scenario are written using pytest and are located in the `/tests` directory. To run the tests, execute:
```bash
pytest
```

## Contributions
Feel free to contribute by submitting issues or pull requests. For larger changes, please discuss first by opening an issue.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.