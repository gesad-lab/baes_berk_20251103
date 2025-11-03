Here's a detailed user manual for the software, including installation instructions, main functions, and usage guidelines.

```markdown
# Student Management System

A FastAPI application for managing student records, including the ability to create and retrieve student information.

## Main Functions

- **Create Student**: Allows users to add a new student with a name and email address.
- **Retrieve Students**: Fetches a list of all students with their details, including name and email.

## Quick Install

To get started with the Student Management System, you need to install the required environment dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
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
   Run the following command to create the initial database schema:
   ```bash
   python main.py
   ```

5. **Run Migrations**:
   To add the email field to the Student table, run the Alembic migration:
   ```bash
   alembic upgrade head
   ```

## Usage

### Starting the Application

To start the FastAPI application, run:
```bash
uvicorn main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

1. **Create a Student**:
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Response**:
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

2. **Get Students**:
   - **Endpoint**: `GET /students/`
   - **Query Parameters**: 
     - `skip`: Number of records to skip (default is 0)
     - `limit`: Number of records to return (default is 10)
   - **Response**:
     ```json
     [
       {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
       },
       ...
     ]
     ```

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file will be created in the project directory as `students.db`.
- **Schema Migration**: The application uses Alembic for database migrations. Make sure to run migrations whenever you change the database schema.

## Documentation

For more detailed documentation on FastAPI and SQLAlchemy, please refer to the following links:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

## Support

If you encounter any issues or have questions, please reach out to our support team at [support@example.com].
```

This manual provides a comprehensive overview of the Student Management System, including installation steps, usage instructions, and links to further documentation.