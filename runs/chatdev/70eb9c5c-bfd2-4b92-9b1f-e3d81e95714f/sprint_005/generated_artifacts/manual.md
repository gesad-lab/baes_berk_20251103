```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses.

## Main Functions

The Teacher Management System allows users to perform the following operations:

- **Manage Teachers**: Create, retrieve, and manage teacher information, including their names and email addresses.
- **Manage Students**: Create, retrieve, and manage student information, including their names and email addresses.
- **Manage Courses**: Create, retrieve, and manage courses, including their names and levels.
- **Student-Course Relationship**: Associate students with courses they are enrolled in.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Install the required Python packages using pip:
   ```bash
   pip install fastapi sqlalchemy alembic pydantic
   ```

4. **Set Up the Database**:
   The application uses SQLite by default. You can change the database URL in `database.py` if needed. To create the database and tables, run:
   ```bash
   python main.py
   ```

## How to Use the Application

### Start the Application

Run the FastAPI application:
```bash
uvicorn main:app --reload
```

### Access the API

Once the application is running, you can access the API documentation at:
```
http://127.0.0.1:8000/docs
```

### API Endpoints

#### Teacher Endpoints

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get All Teachers**:
  - **Endpoint**: `GET /teachers/`

#### Student Endpoints

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```

- **Get All Students**:
  - **Endpoint**: `GET /students/`

#### Course Endpoints

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get All Courses**:
  - **Endpoint**: `GET /courses/`

#### Student-Course Relationship

- **Add Course to Student**:
  - **Endpoint**: `POST /students/{student_id}/courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

## Database Migration

To apply any database migrations, run the following command:
```bash
alembic upgrade head
```

This will ensure that your database schema is up to date with the latest changes, including the addition of the Teacher entity.

## Conclusion

The Teacher Management System provides a straightforward way to manage teachers, students, and courses. By following the installation and usage instructions, you can easily set up and interact with the application.
```
