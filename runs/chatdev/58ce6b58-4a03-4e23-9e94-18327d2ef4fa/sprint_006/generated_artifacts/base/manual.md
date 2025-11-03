```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Main Functions

The Teacher Management System allows users to:

- Create, retrieve, and manage teacher records.
- Create, retrieve, and manage student records.
- Create, retrieve, and manage course records.
- Associate students with courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Environment Dependencies

Make sure you have the following dependencies installed:

- **fastapi**: The web framework used to build the API.
- **uvicorn**: An ASGI server for running FastAPI applications.
- **sqlalchemy**: The ORM used for database interactions.
- **alembic**: The migration tool for managing database schema changes.
- **pydantic**: Used for data validation and settings management.

You can install these dependencies using the following command:

```bash
pip install fastapi uvicorn sqlalchemy alembic pydantic
```

## How to Use the Application

1. **Run the Application:**
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

2. **API Endpoints:**
   The following API endpoints are available:

   - **Teachers:**
     - `POST /teachers/`: Create a new teacher.
     - `GET /teachers/`: Retrieve all teachers.

   - **Students:**
     - `POST /students/`: Create a new student.
     - `GET /students/`: Retrieve all students.

   - **Courses:**
     - `POST /courses/`: Create a new course.
     - `GET /courses/`: Retrieve all courses.

3. **Example Requests:**
   You can use tools like Postman or cURL to interact with the API. Here are some example requests:

   - **Create a Teacher:**
     ```bash
     curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
     ```

   - **Get All Teachers:**
     ```bash
     curl -X GET "http://127.0.0.1:8000/teachers/"
     ```

   - **Create a Student:**
     ```bash
     curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "Jane Smith", "email": "jane.smith@example.com"}'
     ```

   - **Get All Students:**
     ```bash
     curl -X GET "http://127.0.0.1:8000/students/"
     ```

   - **Create a Course:**
     ```bash
     curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner"}'
     ```

   - **Get All Courses:**
     ```bash
     curl -X GET "http://127.0.0.1:8000/courses/"
     ```

## Database Migration

The application uses Alembic for database migrations. To create the initial database schema, run:

```bash
alembic upgrade head
```

This command will create the necessary tables while preserving existing data for students and courses.

## Conclusion

This Teacher Management System provides a simple yet effective way to manage teachers, students, and courses. You can extend its functionality by adding more features as needed. For any issues or feature requests, please reach out to the development team.
```