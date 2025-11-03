Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student-Course Management System

A FastAPI application for managing students and their enrolled courses.

## Main Functions

This application provides the following main functionalities:

- **Create Students**: Add new students to the database along with their enrolled courses.
- **Retrieve Students**: Fetch a list of students with their associated courses.
- **Create Courses**: Add new courses to the database.
- **Retrieve Courses**: Fetch a list of available courses.

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

4. **Set Up the Database**:
   The application uses SQLite for the database. Ensure that the `students.db` file is created in the project directory. This will be handled automatically when you run the application for the first time.

## How to Use

### Running the Application

1. **Start the FastAPI Server**:
   Run the following command to start the server:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API Documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

### API Endpoints

#### 1. Create a Student

- **Endpoint**: `POST /students/`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "course_ids": [1, 2]  // Optional: List of course IDs to enroll the student in
  }
  ```

#### 2. Retrieve Students

- **Endpoint**: `GET /students/`
- **Query Parameters**:
  - `skip`: Number of records to skip (for pagination).
  - `limit`: Maximum number of records to return.

#### 3. Create a Course

- **Endpoint**: `POST /courses/`
- **Request Body**:
  ```json
  {
    "name": "Mathematics",
    "level": "Beginner"
  }
  ```

#### 4. Retrieve Courses

- **Endpoint**: `GET /courses/`
- **Query Parameters**:
  - `skip`: Number of records to skip (for pagination).
  - `limit`: Maximum number of records to return.

## Database Migration

To apply database migrations, use the following commands:

1. Create a new migration:
   ```bash
   alembic revision --autogenerate -m "Add course relationship to Student"
   ```

2. Apply the migration:
   ```bash
   alembic upgrade head
   ```

## Conclusion

This Student-Course Management System provides a simple yet effective way to manage students and their courses. For any issues or feature requests, please reach out to the development team.

```

This manual provides a comprehensive overview of the application, its installation, and usage instructions, ensuring that users can effectively interact with the software.