```markdown
# Student Management System

A simple application for managing student records, including the ability to create and list students with their associated email addresses.

## Main Functions

- **Create Student**: Allows users to add a new student with a name and email address.
- **List Students**: Displays a list of all students along with their IDs, names, and email addresses.

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

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Dependencies

The following dependencies are required for the application:

- **fastapi**: The web framework used for building the API.
- **uvicorn**: ASGI server for running the FastAPI application.
- **sqlalchemy**: ORM used for database interactions.
- **pydantic**: Data validation and settings management using Python type annotations.
- **requests**: Library for making HTTP requests, used in the GUI for interacting with the FastAPI backend.
- **alembic**: Database migration tool for SQLAlchemy, used for managing database schema changes.

Make sure to adjust the versions as necessary based on your project's requirements or the latest stable releases.

## How to Use the Application

1. **Run the FastAPI Application**:
   Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Launch the GUI**:
   Open a new terminal window and run the GUI application:
   ```bash
   python gui.py
   ```

3. **Creating a Student**:
   - In the GUI, enter the student's name and email address in the respective fields.
   - Click the "Create Student" button to add the student to the database.
   - A success message will appear if the student is created successfully.

4. **Listing Students**:
   - Click the "List Students" button to retrieve and display all students in the list box.
   - Each entry will show the student's ID, name, and email address.

## Database Migration

To ensure that the existing student data is preserved while adding the new email field, run the migration script:

1. **Run the migration script**:
   ```bash
   alembic upgrade head
   ```

This will add the `email` column to the `students` table in the database without losing any existing data.

## Conclusion

This Student Management System provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and interact with the application. For further customization or features, feel free to modify the code as needed.
```