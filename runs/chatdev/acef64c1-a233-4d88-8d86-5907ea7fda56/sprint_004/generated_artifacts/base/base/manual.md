Here's the user manual for the software, formatted in Markdown as requested:

```markdown
# Student Management System

A FastAPI application for managing student records, including the ability to create and retrieve student information.

## Main Functions

- **Create Student**: Add a new student record with a name and email address.
- **Retrieve Students**: Get a list of all students along with their details.

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
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Set up the database**:
   The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

## How to Use

1. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```
   This command starts the FastAPI application with live reloading enabled.

2. **Create a new student**:
   You can create a new student by sending a POST request to the `/students/` endpoint with a JSON body containing the student's name and email. For example:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

   You can use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to send the request.

3. **Retrieve all students**:
   To get a list of all students, send a GET request to the `/students/` endpoint. You will receive a JSON response with the details of all students.

## Database Migration

The application includes a migration script to add the email field to the existing Student entity. To apply the migration, run the following command:
```bash
alembic upgrade head
```

This command will update the database schema to include the email field while preserving existing student data.

## Additional Information

For more details on FastAPI, SQLAlchemy, and Alembic, please refer to their respective documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)

If you encounter any issues or have questions, please reach out for support.
```

This manual provides a comprehensive overview of the Student Management System, including installation instructions, usage guidelines, and links to further documentation. Let me know if you need any modifications or additional sections!