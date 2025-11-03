Here's a detailed user manual for the software, including the main functions, installation instructions, and usage guidelines.

```markdown
# Student Management Application

A FastAPI-based application for managing student records, including the ability to create and retrieve student information.

## Main Functions

The Student Management Application provides the following functionalities:

- **Create Student**: Allows users to add a new student with their name and email address.
- **Retrieve Students**: Fetches a list of students with their details, including name and email.

## Quick Install

To set up the environment and run the application, follow these steps:

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
   Ensure you have `pip` installed, then run:
   ```bash
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Initialize the Database**:
   Run the following command to create the initial database schema:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

5. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

## How to Use the Application

### Creating a Student

To create a new student, send a POST request to the `/students/` endpoint with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

You can use tools like Postman or curl to send the request. Here’s an example using curl:

```bash
curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

### Retrieving Students

To retrieve a list of students, send a GET request to the `/students/` endpoint:

```bash
curl -X GET "http://127.0.0.1:8000/students/"
```

This will return a JSON array of students, including their IDs, names, and email addresses.

## Database Migration

To add the email field to the existing Student entity, you need to create and run a migration script using Alembic. Follow these steps:

1. **Create a Migration Script**:
   Run the following command to create a new migration script:
   ```bash
   alembic revision -m "Add email field to students"
   ```

2. **Edit the Migration Script**:
   In the generated migration script, add the following code to the `upgrade()` function:

   ```python
   def upgrade():
       op.add_column('students', sa.Column('email', sa.String(), nullable=True))
       op.execute("UPDATE students SET email = '' WHERE email IS NULL")  # Set a default value
       op.alter_column('students', 'email', nullable=False)
   ```

3. **Run the Migration**:
   Execute the migration to update the database schema:
   ```bash
   alembic upgrade head
   ```

## Conclusion

The Student Management Application is a simple yet powerful tool for managing student records. With the ability to create and retrieve student information, it serves as a foundational application for educational institutions or any organization that needs to manage student data.

For further documentation and support, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).
```

This manual provides a comprehensive overview of the application, installation steps, and usage instructions, ensuring that users can effectively utilize the software.