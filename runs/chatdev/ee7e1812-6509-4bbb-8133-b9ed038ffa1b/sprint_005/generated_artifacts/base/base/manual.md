```markdown
# Course Management System

A simple application for managing students and courses using FastAPI and SQLAlchemy.

## Main Functions

This software provides the following key functionalities:

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records.
- **Database Migration**: Automatically migrate the database schema to include new entities while preserving existing data.

## Quick Install

To set up the environment and install the required dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**:
   To start the FastAPI application, run:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Access the API Endpoints**:
   You can interact with the API using tools like Postman or directly through your browser. The available endpoints are:

   - **Students**:
     - `POST /students/`: Create a new student.
     - `GET /students/`: Retrieve a list of students.

   - **Courses**:
     - `POST /courses/`: Create a new course.
     - `GET /courses/`: Retrieve a list of courses.

3. **Database Migration**:
   The application includes a migration script that ensures the database schema is updated to include the new Course entity without losing existing Student data. This is handled automatically when you run the application.

## Example API Requests

### Create a Student
```http
POST /students/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Retrieve Students
```http
GET /students/
```

### Create a Course
```http
POST /courses/
Content-Type: application/json

{
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

### Retrieve Courses
```http
GET /courses/
```

## Additional Information

For more detailed documentation and examples, please refer to the FastAPI documentation at [FastAPI Docs](https://fastapi.tiangolo.com/).

If you encounter any issues or need further assistance, please reach out to our support team.

Happy coding!
```