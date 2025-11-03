# README.md

# Course Management API

This API allows for the management of courses in an educational context, including the ability to create new courses and retrieve existing course information.

## Project Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database connection in the `.env` file or directly in the application settings.

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## Database Schema

### Course Table

The application includes a new `Course` table with the following fields:

- `id`: Integer (auto-incrementing primary key).
- `name`: String (required).
- `level`: String (required).

The database schema is automatically updated upon application startup, ensuring that existing Student data remains intact.

## API Endpoints

### Create a New Course

- **Endpoint**: `POST /courses`
- **Description**: Creates a new course with the provided `name` and `level`.
- **Request Body**:
  ```json
  {
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```
- **Response**: 
  - **Status Code**: 201 Created
  - **Response Body**:
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```

### Retrieve a Course by ID

- **Endpoint**: `GET /courses/{id}`
- **Description**: Retrieves a course by its ID, including its name and level.
- **Response**: 
  - **Status Code**: 200 OK
  - **Response Body**:
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```
  
### Example Usage

You can test the API endpoints using `curl`:

1. **Create a Course**:
   ```bash
   curl -X POST "http://localhost:8000/courses" -H "Content-Type: application/json" -d '{"name": "Introduction to Programming", "level": "Beginner"}'
   ```

2. **Get Course by ID**:
   ```bash
   curl -X GET "http://localhost:8000/courses/1"
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.