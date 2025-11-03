```markdown
# Student Management API

A simple application for managing student records, including the ability to create and retrieve student information through a user-friendly GUI.

## Main Functions

- **Create Student**: Allows users to add a new student by providing their name and email address.
- **Get Students**: Fetches and displays a list of all students in the database.

## Quick Install

To set up the environment and install the required dependencies, follow these steps:

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
   You can install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Dependencies

The following dependencies are required for the application to run:

- **fastapi**: The web framework used for building the API.
- **uvicorn**: An ASGI server for running FastAPI applications.
- **sqlalchemy**: The ORM used for database interactions.
- **pydantic**: Used for data validation and settings management.
- **alembic**: A database migration tool for SQLAlchemy.
- **requests**: A library for making HTTP requests, used in the GUI for API calls.
- **tkinter**: The standard GUI toolkit for Python, typically included with Python installations.

Make sure to adjust the versions as necessary based on your project's requirements and compatibility.

## How to Use the Application

1. **Run the FastAPI application**:
   Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

2. **Launch the GUI**:
   Run the GUI application by executing:
   ```bash
   python gui.py
   ```

3. **Creating a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Create Student" button to add the student to the database. A success message will be displayed if the student is created successfully.

4. **Retrieving Students**:
   - Click the "Get Students" button to fetch and display a list of all students currently stored in the database.

## Database Migration

The application uses Alembic for database migrations. To add the email field to the Student entity, run the following command after creating the migration script:

```bash
alembic upgrade head
```

This command will apply the migration, adding the email column to the existing Student table while preserving existing data.

## Additional Information

For more detailed documentation and examples, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).

If you encounter any issues or have questions, feel free to reach out for support.
```