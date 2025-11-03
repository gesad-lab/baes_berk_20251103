Here's a detailed user manual for the Student Management application, formatted in Markdown as requested:

```markdown
# Student Management Application

A simple application for managing student records, including adding and retrieving student information.

## Main Functions

- **Create Student**: Allows users to add a new student with a name and email address.
- **Retrieve Students**: Fetches a list of students from the database.

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
   ```bash
   pip install fastapi[all] sqlalchemy alembic pydantic requests
   ```

4. **Run Database Migration**:
   Ensure that the database schema is updated to include the new email field:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

1. **Open the GUI**:
   After starting the application, a GUI window will appear.

2. **Add a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Submit" button to create the student record.

3. **View Output**:
   - The application will display a confirmation message with the student's details or an error message if the submission fails.

## Database Schema

The application uses SQLite as the database, and the `students` table includes the following fields:

- `id`: Integer, primary key
- `name`: String, required
- `email`: String, required

## Migration Details

The application uses Alembic for database migrations. The migration script adds the `email` field to the `students` table while preserving existing data.

## Additional Information

For more detailed documentation on FastAPI, SQLAlchemy, and Alembic, please refer to their respective official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

If you encounter any issues or have questions, feel free to reach out for support.
```

This manual provides a comprehensive overview of the application, installation instructions, usage guidelines, and links to additional resources for further assistance.