# Project Title: Student Management App

## Description
The Student Management App is a simple web application that allows users to manage student records. Users can add new students and retrieve a list of all students through a RESTful API. The app utilizes SQLite as the database backend for storing student information.

## Features
- **Create Student**: Add a new student by sending a POST request with the student's name.
- **Retrieve Students**: Fetch a list of all students with a GET request.
- Automatically creates the SQLite database schema on startup.

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student_management_app.git
   cd student_management_app
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python src/app.py
   ```

### API Usage Examples
1. **Add a New Student**
   - **Request**:
     ```bash
     curl -X POST http://localhost:5000/students -H "Content-Type: application/json" -d '{"name": "John Doe"}'
     ```
   - **Response**:
     ```json
     {
       "id": 1,
       "name": "John Doe"
     }
     ```

2. **Retrieve All Students**
   - **Request**:
     ```bash
     curl http://localhost:5000/students
     ```
   - **Response**:
     ```json
     [
       {
         "id": 1,
         "name": "John Doe"
       }
     ]
     ```

3. **Add Student Without Name**
   - **Request**:
     ```bash
     curl -X POST http://localhost:5000/students -H "Content-Type: application/json" -d '{}'
     ```
   - **Response**:
     ```json
     {
       "error": {
         "code": "E001",
         "message": "Name is required."
       }
     }
     ```

## Database Configuration
The application configures the SQLite database automatically upon startup, including the creation of the `Student` table.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.