```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers effectively. You can create, retrieve, and manage relationships between these entities seamlessly.

## Main Functions

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve courses, including assigning teachers to courses.
- **Teacher Management**: Create and retrieve teacher records.
- **Relationships**: Associate students with courses and courses with teachers.

## Quick Install

To get started, you need to install the required dependencies for the project. You can do this using `pip` or `conda`.

### Using pip

```bash
pip install -r requirements.txt
```

### Using conda

```bash
conda install --file requirements.txt
```

## Environment Setup

1. **Clone the Repository**: 
   Clone the repository to your local machine using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: 
   Use one of the methods mentioned above to install the required dependencies.

3. **Database Initialization**: 
   The database will be initialized automatically when you run the application for the first time. Ensure that you have SQLite installed and accessible.

## How to Use the Application

1. **Run the Application**: 
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**: 
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Creating Entities**:
   - **Create a Student**:
     - Endpoint: `POST /students/`
     - Body: `{ "name": "John Doe", "email": "john@example.com" }`
   - **Create a Teacher**:
     - Endpoint: `POST /teachers/`
     - Body: `{ "name": "Jane Smith", "email": "jane@example.com" }`
   - **Create a Course**:
     - Endpoint: `POST /courses/`
     - Body: `{ "name": "Mathematics", "level": "Beginner", "teacher_id": 1 }` (Ensure the teacher exists)

4. **Retrieving Entities**:
   - **Get All Students**: `GET /students/`
   - **Get All Teachers**: `GET /teachers/`
   - **Get All Courses**: `GET /courses/`

5. **Associating Students with Courses**:
   - Endpoint: `POST /students/{student_id}/courses/{course_id}`
   - This will associate a student with a course.

## Database Migration

The application uses Alembic for database migrations. To create and apply migrations:

1. **Create Migration**:
   ```bash
   alembic revision --autogenerate -m "Your migration message"
   ```

2. **Apply Migration**:
   ```bash
   alembic upgrade head
   ```

## Conclusion

This Course Management System is designed to simplify the management of educational entities. With its easy-to-use API and robust backend, you can efficiently manage students, teachers, and courses. For further assistance, please refer to the API documentation or contact support.

Happy coding!
```