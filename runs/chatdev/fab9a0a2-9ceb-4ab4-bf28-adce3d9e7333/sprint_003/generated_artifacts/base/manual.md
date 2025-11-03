```markdown
# Student Management System

A simple FastAPI application for managing student records, including the ability to create and retrieve student information with an email field.

## Main Functions

- **Create Student**: Allows you to add a new student with a name and email address.
- **Read Student**: Retrieve the details of a student by their unique ID.

## Quick Install

To get started with the Student Management System, you need to install the required dependencies. You can do this using pip:

```bash
pip install fastapi sqlalchemy pydantic alembic uvicorn
```

## Setting Up the Environment

1. **Clone the Repository**: If you haven't already, clone the repository containing the code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use the command provided above to install all necessary packages.

3. **Database Migration**: Before running the application, you need to apply the database migration to add the email field to the Student entity.

   Run the following command:

   ```bash
   alembic upgrade head
   ```

   This command will update the database schema while preserving existing student data.

## How to Use the Application

1. **Run the Application**: Start the FastAPI application using Uvicorn.

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server at `http://127.0.0.1:8000`.

2. **Create a New Student**: You can create a new student by sending a POST request to `/students/` with the following JSON body:

   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

   You can use tools like Postman or cURL to make this request.

3. **Retrieve Student Information**: To get the details of a student, send a GET request to `/students/{student_id}`, replacing `{student_id}` with the actual ID of the student you want to retrieve.

   Example:

   ```bash
   curl -X GET http://127.0.0.1:8000/students/1
   ```

   This will return the student's details, including their name and email.

## Additional Information

For more detailed documentation on FastAPI, SQLAlchemy, and Pydantic, please refer to their respective official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

Feel free to reach out if you have any questions or need further assistance!
```