Here's a user manual for the software, detailing the main functions, installation of environment dependencies, and usage instructions. 

```markdown
# Student Management Application

A simple application for managing student records, including the ability to create and retrieve student information.

## Main Functions

- **Create Student**: Add a new student record with a name and email address.
- **Retrieve Students**: Fetch a list of students with pagination support.

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
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   pydantic
   uvicorn
   ```

## Usage Instructions

### Running the Application

1. **Start the Application**:
   Run the following command to start the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

### Creating a Student

To create a new student, send a POST request to `/students` with the following JSON payload:
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

### Retrieving Students

To retrieve a list of students, send a GET request to `/students`. You can also use query parameters for pagination:
```
GET /students?skip=0&limit=10
```

## Database Migration

The application uses SQLite as the database. To add the new email field to the existing Student entity, run the migration script:
```bash
python main.py
```

This will update the database schema to include the email field while preserving existing student data.

## Conclusion

This application provides a straightforward interface for managing student records. You can extend its functionality by adding more features as needed. For any issues or feature requests, please reach out to the development team.
```

This manual provides a comprehensive overview of the application, its installation, and usage, ensuring that users can effectively utilize the software.