Here's a detailed user manual for the software, including the main functions, installation instructions, and usage guidelines.

```markdown
# Student Management Application

A simple application for managing student records, including the ability to add and retrieve student information.

## Main Functions

- **Create Student**: Add a new student record with a name and email address.
- **Retrieve Students**: Fetch a list of all students in the database.
- **Email Validation**: Ensure that the email provided is in a valid format.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-management.git
   cd student-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy pydantic alembic
   ```

4. **Run Database Migration**:
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

### Creating a Student

To create a new student, send a POST request to the `/students/` endpoint with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Example Using `curl`

You can use `curl` to create a student from the command line:

```bash
curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

### Retrieving Students

To retrieve all students, send a GET request to the `/students/` endpoint:

```bash
curl -X GET "http://127.0.0.1:8000/students/"
```

### Validating Email

The application uses Pydantic to validate the email format when creating a student. If the email is invalid, a 422 Unprocessable Entity error will be returned.

## Documentation

For more detailed documentation on the API and its usage, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).

## Support

If you encounter any issues or have questions, please reach out to our support team via the contact information provided in the repository.

```

This manual provides a comprehensive overview of the Student Management Application, including installation instructions, main functionalities, and usage examples. Let me know if you need any further modifications or additional sections!