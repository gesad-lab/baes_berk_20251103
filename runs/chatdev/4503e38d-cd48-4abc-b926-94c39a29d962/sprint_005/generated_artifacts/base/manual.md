Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Course Management System

A simple application to manage students and their associated courses.

## Main Functions

- **Student Registration**: Allows users to register new students with their names, emails, and associated courses.
- **Course Management**: Enables the creation of courses that students can enroll in.
- **Database Management**: Maintains a SQLite database to store student and course information, ensuring data integrity and persistence.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-course-management.git
   cd student-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic pydantic requests
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migration script:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### 1. Access the Dashboard

Once the application is running, you can access the dashboard by navigating to `http://127.0.0.1:8000/docs` in your web browser. This will provide you with an interactive API documentation interface.

### 2. Register a New Student

- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "courses": ["Mathematics", "Science"]
  }
  ```
- **Response**: Returns the registered student's details including their ID.

### 3. Create a New Course

- **Endpoint**: `POST /courses`
- **Request Body**:
  ```json
  {
    "name": "Mathematics",
    "level": "Beginner"
  }
  ```
- **Response**: Returns the created course details including its ID.

### 4. View All Students and Courses

You can view all registered students and courses by accessing the following endpoints:

- **Students**: `GET /students`
- **Courses**: `GET /courses`

### 5. Update Student Information

To update a student's information, you can use the `PUT` method on the `/students/{id}` endpoint (not implemented in the current version but can be added as a feature).

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file is located in the project directory as `students.db`.
- **Data Migration**: The migration scripts ensure that existing data is preserved while updating the database schema.

## Conclusion

This Student Course Management System provides a simple yet effective way to manage students and their courses. For further enhancements or feature requests, feel free to reach out to the development team.

```

This manual provides a comprehensive overview of the software, installation instructions, and usage guidelines, ensuring that users can effectively interact with the application.