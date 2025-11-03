```markdown
# Student Management System

A simple application for managing student records, including their names and email addresses.

## Main Functions

- **Create Student**: Allows you to add a new student with their name and email address.
- **Read Students**: Fetches a list of students stored in the database.

## Quick Install

To set up the environment and install the required dependencies, follow these steps:

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
   pip install fastapi sqlalchemy pydantic alembic
   ```

4. **Install an ASGI server** (e.g., uvicorn):
   ```bash
   pip install uvicorn
   ```

## Database Setup

1. **Initialize the database**:
   The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

2. **Run migrations**:
   To add the email field to the existing Student entity, run the migration script:
   ```bash
   alembic upgrade head
   ```

## How to Use

1. **Run the application**:
   Start the FastAPI application using uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your browser and go to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Create a new student**:
   Use the `/students/` endpoint to create a new student. You will need to provide a JSON body with the student's name and email:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

4. **Read existing students**:
   Use the same `/students/` endpoint with a GET request to retrieve a list of all students.

## Example Usage

### Creating a Student

```bash
curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "Jane Doe", "email": "jane.doe@example.com"}'
```

### Retrieving Students

```bash
curl -X GET "http://127.0.0.1:8000/students/"
```

## Additional Information

For more detailed documentation, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).

This application is designed to be simple and extensible. You can easily add more features such as updating or deleting student records as needed.
```