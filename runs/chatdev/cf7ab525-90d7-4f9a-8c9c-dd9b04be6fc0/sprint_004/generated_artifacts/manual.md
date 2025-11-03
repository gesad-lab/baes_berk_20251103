```markdown
# Student Course Management System

A comprehensive application for managing student and course relationships, allowing students to enroll in multiple courses and manage their academic profiles.

## Main Functions

- **Student Management**: Create and manage student profiles, including their names and email addresses.
- **Course Management**: Create and manage courses, including course names and levels.
- **Enrollment**: Enroll students in multiple courses, establishing a many-to-many relationship between students and courses.
- **Data Persistence**: All data is stored in a SQLite database, ensuring data integrity and persistence.

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

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migration scripts:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### API Endpoints

The application exposes several API endpoints for managing students and courses.

#### Create a Student

- **Endpoint**: `POST /students/`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "course_ids": [1, 2]
  }
  ```
- **Description**: Creates a new student and enrolls them in the specified courses.

#### Create a Course

- **Endpoint**: `POST /courses/`
- **Request Body**:
  ```json
  {
    "name": "Mathematics",
    "level": "Intermediate"
  }
  ```
- **Description**: Creates a new course.

#### Get Students

- **Endpoint**: `GET /students/`
- **Query Parameters**: `skip` (optional), `limit` (optional)
- **Description**: Retrieves a list of students with pagination.

### Database Structure

The application uses a SQLite database with the following tables:

- **students**: Stores student information (id, name, email).
- **courses**: Stores course information (id, name, level).
- **student_courses**: An association table that links students to their enrolled courses.

### GUI Implementation

The GUI file (`gui.py`) is currently empty. You can implement a graphical user interface to interact with the API if needed.

## Additional Resources

For more detailed documentation on FastAPI and SQLAlchemy, please refer to the following links:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

## Conclusion

This Student Course Management System provides a robust solution for managing student and course relationships. With its RESTful API, you can easily integrate it into other applications or extend its functionality as needed.
```