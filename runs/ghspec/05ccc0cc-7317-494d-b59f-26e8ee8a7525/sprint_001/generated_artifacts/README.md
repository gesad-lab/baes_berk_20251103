# README.md

# Student Management System

## Overview
This application provides a REST API for managing student records. Users can create new student records and retrieve existing ones.

## Database Setup
This application uses an SQLite database to store student records. The required database schema will be created automatically upon startup.

### Important Files
- `app/models.py`: Contains SQLAlchemy models for the application.
- `app/main.py`: Defines the API endpoints and handles requests.
- `README.md`: Documentation for setting up and using the application.

## API Endpoints

### 1. Create Student
- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "John Doe"
  }
  ```
- **Response**: 
  - `200 OK` with created student details in JSON format or an error message if the name is missing.

### 2. Retrieve All Students
- **Endpoint**: `GET /students`
- **Response**: `200 OK` with an array of student objects in JSON format.

## Test Cases

### Database Initialization Test
To ensure that the necessary database schema is created at startup, validate the presence of the `students` table in the SQLite database.

```python
import unittest
from sqlalchemy import create_engine, inspect
from app.models import Base

class TestDatabaseInitialization(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Create in-memory SQLite database for testing
        cls.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(cls.engine)

    def test_students_table_exists(self):
        """Test to validate the presence of the students table after startup."""
        inspector = inspect(self.engine)
        self.assertIn('students', inspector.get_table_names(), "The 'students' table should exist.")

if __name__ == '__main__':
    unittest.main()
```

### Other Test Cases
1. **Create Student**: Test success and missing name error.
2. **Retrieve All Students**: Test retrieving the list, confirm JSON structure.

## Success Criteria
1. The API responds with a success message and the student data when a student is created successfully.
2. The API returns an array of existing students when requested.
3. The application automatically creates the required database schema without manual intervention during startup.
4. Error messages inform users adequately when they attempt to create a student record without a name.

## Usage
1. Install required Python packages:  
   `pip install -r requirements.txt`
2. Run the application:  
   `python app/main.py`
3. Access the API at `http://localhost:8000`.

## License
This project is licensed under the MIT License - see the LICENSE file for details.