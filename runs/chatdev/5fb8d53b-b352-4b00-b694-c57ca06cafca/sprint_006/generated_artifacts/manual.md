```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers effectively. You can create, read, update, and delete records for each entity, as well as establish relationships between courses and teachers.

## Main Functions

- **Student Management**: Create and manage student records, including their names and emails.
- **Course Management**: Create and manage courses, including associating them with teachers.
- **Teacher Management**: Create and manage teacher records, including their names and emails.
- **Relationships**: Establish a relationship between courses and teachers, allowing each course to have a designated teacher.

## Quick Install

To get started, you need to install the required dependencies. You can do this using `pip`:

```bash
pip install -r requirements.txt
```

Alternatively, if you are using `conda`, you can install the dependencies as follows:

```bash
conda install fastapi uvicorn sqlalchemy alembic -c conda-forge
```

## How to Use the Software

1. **Run the Application**:
   To start the FastAPI application, run the following command in your terminal:

   ```bash
   python run.py
   ```

   This will start the server, and you can access the API at `http://127.0.0.1:8000`.

2. **API Endpoints**:
   The application exposes several API endpoints for managing students, courses, and teachers. Here are the main endpoints:

   - **Students**:
     - `POST /students/`: Create a new student.
       - Request Body: `{"name": "Student Name", "email": "student@example.com"}`
     - `GET /students/`: Retrieve a list of all students.

   - **Courses**:
     - `POST /courses/`: Create a new course.
       - Request Body: `{"name": "Course Name", "level": "Course Level", "teacher_id": 1}`
     - `GET /courses/`: Retrieve a list of all courses.

   - **Teachers**:
     - `POST /teachers/`: Create a new teacher.
       - Request Body: `{"name": "Teacher Name", "email": "teacher@example.com"}`
     - `GET /teachers/`: Retrieve a list of all teachers.

3. **Database Migration**:
   The application uses Alembic for database migrations. When you run the application for the first time, it will automatically create the necessary tables in the SQLite database (`students.db`). The migration script ensures that existing data for students, courses, and teachers is preserved while adding new relationships.

4. **Testing the API**:
   You can test the API using tools like Postman or cURL. For example, to create a new student, you can use the following cURL command:

   ```bash
   curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}'
   ```

## Conclusion

This Course Management System provides a robust framework for managing educational entities and their relationships. Feel free to explore the API and integrate it into your applications. If you have any questions or need support, please reach out to our team.

Happy coding!
```