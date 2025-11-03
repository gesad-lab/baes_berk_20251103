```markdown
# Student Management System

A simple application for managing student records, including adding and viewing students with their email addresses.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address, which will be stored in the database.
- **Show Students**: Displays a list of all students along with their IDs, names, and email addresses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Initialize the Database**:
   Run the following command to create the initial database schema:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI application by executing:
   ```bash
   python main.py
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

2. **Add a Student**:
   - Open the GUI application (Tkinter interface).
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to save the student record.

3. **Show Students**:
   - Click the "Show Students" button to retrieve and display a list of all students in the database.

## Database Migration

To add the email field to the existing Student entity, the following migration steps were implemented:

1. **Create Migration Script**:
   Run the command to create a new migration script:
   ```bash
   alembic revision --autogenerate -m "Add email field to Student"
   ```

2. **Migration Script**:
   The migration script includes:
   - Adding the email column as nullable.
   - Updating existing records with a default email value.
   - Altering the column to be non-nullable.

## Additional Information

For more detailed documentation on FastAPI, SQLAlchemy, and Alembic, please refer to their respective official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)

Feel free to reach out if you have any questions or need further assistance!
```