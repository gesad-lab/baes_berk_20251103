Here's the `manual.md` file tailored for the software that includes the new email field for the Student entity:

```markdown
# Student Management System

A FastAPI application for managing student records, including functionalities for creating and retrieving student information.

## Main Functions

- **Create Student**: Allows users to add a new student with a name and email address.
- **Retrieve Students**: Fetches a list of all students stored in the database.
- **Email Validation**: Ensures that the email provided for each student is valid.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd student_app
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

## Database Migration

To add the new email field to the Student entity and preserve existing data, run the following Alembic migration command:

```bash
alembic upgrade head
```

This command will apply the migration script located in the `xxxx_add_email_field_to_student.py` file, adding the email column to the existing Student table.

## How to Use the Application

1. **Run the FastAPI application**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs`. This will provide you with an interactive API documentation interface where you can test the endpoints.

3. **Create a new student**:
   Use the `/students/` POST endpoint to create a new student. You will need to provide a JSON body with the following structure:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

4. **Retrieve all students**:
   Use the `/students/` GET endpoint to fetch a list of all students. This will return a JSON array of student objects, each containing the id, name, and email.

## Additional Information

- **Dependencies**:
  - **fastapi**: The web framework used to build the API.
  - **uvicorn**: The ASGI server for running the FastAPI application.
  - **sqlalchemy**: The SQL toolkit and Object-Relational Mapping (ORM) system used for database interactions.
  - **pydantic**: Used for data validation and settings management using Python type annotations.
  - **alembic**: A lightweight database migration tool for use with SQLAlchemy.

For more detailed documentation, please refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).

## Support

If you encounter any issues or have questions, please reach out to our support team via the designated support channel.
```

This manual provides a comprehensive overview of the application, installation instructions, usage guidelines, and additional resources for users.