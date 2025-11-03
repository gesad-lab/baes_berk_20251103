```markdown
# Student Management System

A FastAPI application for managing student records, including the ability to add and retrieve student information.

## Main Functions

The Student Management System provides the following functionalities:

- **Add Student**: Allows users to add a new student record, including their name and email address.
- **Retrieve Students**: Enables users to retrieve a list of all students in the database.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
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

4. **Initialize the Database**:
   Run the following command to create the database tables:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

## Usage

To run the application, execute the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the API documentation at `http://127.0.0.1:8000/docs`.

### Adding a Student

To add a new student, send a POST request to `/students/` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Retrieving Students

To retrieve the list of all students, send a GET request to `/students/`. The response will be a JSON array of student records, each containing the student's ID, name, and email.

## Database Migration

The application uses Alembic for database migrations. To add the email field to the Student table, run the following command:

```bash
alembic upgrade head
```

This will apply the migration that adds the email field while preserving existing student data.

## Conclusion

The Student Management System is a simple yet powerful application for managing student records. With its easy-to-use API and robust database management, it provides a solid foundation for further development and enhancements.
```
