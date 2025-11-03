Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Management API

A FastAPI application for managing student records, including the ability to create and retrieve student information.

## Main Functions

- **Create Student**: Allows the addition of a new student with a name and email address.
- **Retrieve Students**: Fetches a list of all students stored in the database.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Create a New Student**:
   To create a new student, send a POST request to `/students/` with the following JSON body:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```
   You can use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to test the API.

   Example using curl:
   ```bash
   curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
   ```

3. **Retrieve All Students**:
   To get a list of all students, send a GET request to `/students/`:
   ```bash
   curl -X GET "http://127.0.0.1:8000/students/"
   ```

## Database Migration

The application includes a migration function that automatically adds the email field to the existing Student entity without losing any existing data. This is handled in the `migrate_database` function within `database.py`.

## API Documentation

You can access the automatically generated API documentation by visiting `http://127.0.0.1:8000/docs` in your web browser. This provides an interactive interface to test the API endpoints.

## Conclusion

This Student Management API provides a simple yet effective way to manage student records. By following the installation and usage instructions, you can quickly set up and start using the application.
```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, usage guidelines, and information about the database migration process.