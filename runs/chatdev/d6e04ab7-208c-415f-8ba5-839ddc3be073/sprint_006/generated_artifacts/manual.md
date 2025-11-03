```markdown
# Student Course Management System

A FastAPI application for managing students, courses, and teachers, allowing for the creation and retrieval of entities while maintaining relationships between them.

## Main Functions

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records, including the association of teachers.
- **Teacher Management**: Create and retrieve teacher records.
- **Relationships**: Establish relationships between students, courses, and teachers.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
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
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

1. **Create the Database**:
   The database will be created automatically when you run the application for the first time. Ensure that you have SQLite installed, as this application uses SQLite as the database.

2. **Run Migrations**:
   To apply the database migrations, run the following command:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

2. **API Endpoints**:
   You can interact with the application through the following API endpoints:

   - **Students**:
     - `POST /students/`: Create a new student.
     - `GET /students/`: Retrieve a list of students.

   - **Courses**:
     - `POST /courses/`: Create a new course (including teacher association).
     - `GET /courses/`: Retrieve a list of courses.

   - **Teachers**:
     - `POST /teachers/`: Create a new teacher.
     - `GET /teachers/`: Retrieve a list of teachers.

3. **Testing the API**:
   You can use tools like Postman or curl to test the API endpoints. Here are some example requests:

   - **Create a Student**:
     ```bash
     curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}'
     ```

   - **Create a Teacher**:
     ```bash
     curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "Jane Smith", "email": "jane@example.com"}'
     ```

   - **Create a Course**:
     ```bash
     curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Math 101", "level": "Beginner", "teacher_id": 1}'
     ```

## Documentation

For more detailed documentation on FastAPI, SQLAlchemy, and Pydantic, please refer to the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

## Conclusion

This application provides a robust framework for managing students, courses, and teachers with a focus on relationships between entities. Feel free to extend the functionality as needed!
```