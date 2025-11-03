```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses in an educational environment.

## Main Functions

The Teacher Management System provides the following functionalities:

- **Create and manage teachers**: Add new teachers with their names and email addresses.
- **Create and manage students**: Add new students with their names, email addresses, and enrolled courses.
- **Create and manage courses**: Add new courses with their names and levels.
- **Retrieve data**: Fetch lists of teachers, students, and courses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   Start the FastAPI application by executing:
   ```bash
   python main.py
   ```
   The API will be available at `http://127.0.0.1:8000`.

2. **Access the API documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **API Endpoints**:
   - **Teachers**:
     - `POST /teachers/`: Create a new teacher.
     - `GET /teachers/`: Retrieve a list of all teachers.
   - **Students**:
     - `POST /students/`: Create a new student.
     - `GET /students/`: Retrieve a list of all students.
   - **Courses**:
     - `POST /courses/`: Create a new course.
     - `GET /courses/`: Retrieve a list of all courses.

## Example Requests

### Create a Teacher
```bash
curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

### Get All Teachers
```bash
curl -X GET "http://127.0.0.1:8000/teachers/"
```

### Create a Student
```bash
curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "Jane Smith", "email": "jane.smith@example.com", "course_ids": []}'
```

### Get All Students
```bash
curl -X GET "http://127.0.0.1:8000/students/"
```

### Create a Course
```bash
curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner"}'
```

### Get All Courses
```bash
curl -X GET "http://127.0.0.1:8000/courses/"
```

## Database Migration

To add the Teacher table to the existing database schema while preserving the existing Student and Course data, run the migration script using Alembic. Ensure you have set up Alembic correctly in your project.

1. **Run the migration**:
   ```bash
   alembic upgrade head
   ```

This will create the `teachers` table in your database without affecting existing data.

## Conclusion

The Teacher Management System is a straightforward API designed for educational institutions to manage teachers, students, and courses efficiently. For further details and advanced usage, please refer to the API documentation available at `/docs`.
```