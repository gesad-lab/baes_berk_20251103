# README.md

# Project Title

This project is an educational management system designed to handle course and student data.

## User Scenarios & Testing

1. **Creating a Course**: 
   - A user provides a name and level for the Course and submits a form. 
   - The system should save the new Course in the database and return a confirmation response.

2. **Retrieving Course Details**: 
   - A user requests to view details of a specific Course. 
   - The application should provide the Course's name and level in a JSON response.

3. **Updating Course Information**: 
   - A user provides a Course ID and updates the name or level in a form. 
   - The system should update the Course in the database and return a confirmation response.

4. **Creating a Course Without Required Fields**: 
   - A user attempts to create a Course without providing either name or level. 
   - The system should return an error indicating that both fields are required.

5. **Retrieving a Non-existent Course**: 
   - A user tries to retrieve details of a Course that does not exist. 
   - The system should return an error indicating that the Course was not found.

## Functional Requirements

1. **Course Creation**:
   - Endpoint: POST `/courses`
   - Input: JSON containing `name` (string, required) and `level` (string, required)
   - Output: JSON response confirming creation (200 OK) or error (400 Bad Request for missing required fields).

2. **Course Retrieval**:
   - Endpoint: GET `/courses/{id}`
   - Input: Course ID (integer, required)
   - Output: JSON containing `id`, `name`, and `level`, or error (404 Not Found if Course does not exist).

3. **Course Update**:
   - Endpoint: PUT `/courses/{id}`
   - Input: Course ID (integer, required) and JSON containing `name` (string, required) and `level` (string, required)
   - Output: JSON response confirming update (200 OK), or error (400 Bad Request for invalid input or missing fields, 404 Not Found).
   - **Note**: If name or level is not provided, return 400 Bad Request.

4. **Database Management**:
   - Update the database schema to include a new `Course` table with the fields required for storing course information.

## 1.2 Technology Stack
- **Programming Language**: Python
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest

## API Endpoints

### Courses

1. **POST /courses**: Create a new Course
2. **GET /courses/{id}**: Retrieve a Course by ID
3. **PUT /courses/{id}**: Update an existing Course

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## Running Tests

To run the tests for this project, use:
```bash
pytest
```

Ensure that the test database is set up correctly before running the tests.