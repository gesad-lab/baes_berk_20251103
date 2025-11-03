Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Management Application

A simple application for managing student records, including the ability to add and retrieve student information.

## Main Functions

- **Create Student**: Add a new student record with a name and email address.
- **Get Students**: Retrieve a list of all students in the database.

## Quick Install

To set up the environment and install the required dependencies, follow these steps:

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
   Ensure that the database is set up correctly by running the migration script:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

### Starting the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### Creating a Student

To create a new student, send a POST request to the `/students/` endpoint with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

You can use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to make this request. Here's an example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

### Retrieving Students

To retrieve a list of all students, send a GET request to the `/students/` endpoint:

```bash
curl -X GET "http://127.0.0.1:8000/students/"
```

This will return a JSON array of student records.

## Additional Information

- **Database**: The application uses SQLite as the database. The database file will be created in the project directory.
- **Email Validation**: The email field is validated to ensure it is in the correct format.
- **Data Preservation**: The database migration process ensures that existing student data is preserved when adding the new email field.

## Documentation

For more detailed documentation, including API references and advanced usage, please refer to the [FastAPI documentation](https://fastapi.tiangolo.com/) and [SQLAlchemy documentation](https://docs.sqlalchemy.org/).

## Support

If you encounter any issues or have questions, please reach out to our support team via the contact form on our website.
```

This manual provides a comprehensive overview of the application, installation instructions, usage guidelines, and links to additional resources. Let me know if you need any modifications or additional sections!