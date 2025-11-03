Here's a detailed user manual for the software, including installation instructions, main functions, and usage guidelines.

```markdown
# Student Management Application

A simple application for managing student records, including the ability to add, update, and retrieve student information.

## Main Functions

- **Add Student**: Allows users to create a new student record with a name and email address.
- **Update Student**: Enables users to modify existing student records.
- **Retrieve Student**: Fetches student information based on the provided criteria.
- **Database Migration**: Automatically updates the database schema to include new fields without losing existing data.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student-management-app.git
   cd student-management-app
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

   Ensure that you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   pydantic
   ```

4. **Run Database Migration**:
   To apply the latest database schema changes, run:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be running at `http://127.0.0.1:8000`.

## How to Use the Application

### Adding a Student

To add a new student, send a POST request to the `/students` endpoint with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Updating a Student

To update an existing student, send a PUT request to the `/students/{id}` endpoint with the updated information:

```json
{
  "name": "John Doe",
  "email": "john.doe@newdomain.com"
}
```

### Retrieving a Student

To retrieve a student's information, send a GET request to the `/students/{id}` endpoint.

### Database Migration

The application uses Alembic for database migrations. When you add new fields or make changes to the database schema, ensure to run the migration commands to keep the database in sync with your models.

## Additional Information

For more detailed documentation, including API reference and examples, please refer to the [FastAPI Documentation](https://fastapi.tiangolo.com/).

If you encounter any issues or have questions, feel free to reach out for support.

```

This manual provides a comprehensive overview of the software, installation steps, and usage instructions, ensuring that users can effectively utilize the Student Management Application.