```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This application allows you to manage students, courses, and teachers effectively. You can create, read, and manage relationships between these entities.

## Main Functions

- **Student Management**: Create and manage student records, including their courses.
- **Course Management**: Create and manage courses, including assigning teachers to courses.
- **Teacher Management**: Create and manage teacher records.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   pydantic
   uvicorn
   ```

4. **Run database migrations**:
   After installing the dependencies, run the migration scripts to set up the database schema:
   ```bash
   alembic upgrade head
   ```

5. **Start the application**:
   Run the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### API Endpoints

The application exposes several API endpoints for managing students, courses, and teachers.

#### Students

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get Students**:
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip`, `limit` (for pagination)

#### Courses

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner",
      "teacher_id": 1  // Optional, if you want to assign a teacher
    }
    ```

- **Get Courses**:
  - **Endpoint**: `GET /courses/`
  - **Query Parameters**: `skip`, `limit` (for pagination)

#### Teachers

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```

- **Get Teachers**:
  - **Endpoint**: `GET /teachers/`
  - **Query Parameters**: `skip`, `limit` (for pagination)

### Database Schema

The application uses SQLite as the database. The following tables are created:

- **students**: Stores student information.
- **courses**: Stores course information and relationships with teachers.
- **teachers**: Stores teacher information.
- **student_courses**: A many-to-many relationship table linking students and courses.

### Database Migration

To ensure that existing data is preserved during schema updates, Alembic is used for database migrations. The migration scripts handle the addition of new fields and tables without losing existing data.

## Conclusion

This application provides a robust framework for managing educational entities. You can extend its functionality by adding more features as needed. For further assistance, feel free to reach out to the support team.

Happy coding!
```