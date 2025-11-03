```markdown
# Student Management API

A simple API for managing student records, including the ability to create and retrieve student information with an email field.

## Main Functions

- **Create Student**: Allows users to add a new student with a name and email address.
- **Retrieve Student**: Fetches the details of a student by their unique ID.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository** (if applicable):
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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Initialization

Before running the application, ensure that the database is initialized. This can be done by running the application, which will automatically create the necessary tables.

## How to Use the API

### Running the Application

1. Start the FastAPI application:
   ```bash
   python main.py
   ```
   The API will be available at `http://127.0.0.1:8000`.

### Using the API

#### Create a Student

To create a new student, send a POST request to the `/students/` endpoint with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

You can use tools like Postman or cURL, or the provided GUI.

#### Retrieve a Student

To retrieve a student's details, send a GET request to the `/students/{student_id}` endpoint, replacing `{student_id}` with the actual ID of the student.

### Using the GUI

1. Run the GUI application:
   ```bash
   python gui.py
   ```

2. Enter the student's name and email in the respective fields.

3. Click the "Create Student" button to submit the information. The result will be displayed below the button.

## Database Migration

If you need to apply database migrations (for example, if you change the schema), you can use Alembic. The migration script is included in `migration.py`. To apply the migration, run:

```bash
alembic upgrade head
```

## Conclusion

This Student Management API provides a straightforward way to manage student records, including the ability to add and retrieve students with their email addresses. For further customization or enhancements, feel free to modify the code as needed.

For more detailed documentation, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).
```