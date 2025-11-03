Here's the user manual for the software, formatted in Markdown as requested:

```markdown
# Student Management System

A simple application for managing student records, including the ability to create and retrieve student information.

## Main Functions

- **Create Student**: Allows users to add a new student by providing their name and email address.
- **Get Students**: Fetches and displays a list of all students, including their names and email addresses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

4. **Install Alembic for Database Migrations**:
   ```bash
   pip install alembic
   ```

5. **Run Database Migrations**:
   ```bash
   alembic upgrade head
   ```

## How to Use

1. **Run the Application**:
   Start the FastAPI application by running:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the GUI**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation, or use the GUI provided by the `gui.py` script.

3. **Create a Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Create Student" button to add the student to the database.

4. **Get Students**:
   - Click the "Get Students" button to retrieve and display the list of all students along with their email addresses.

## Additional Information

- **Database**: The application uses SQLite for data storage, and the database file is created automatically in the project directory.
- **Email Validation**: The email field is validated to ensure that it contains a properly formatted email address.

## Troubleshooting

- If you encounter any issues while running the application, ensure that all dependencies are installed correctly and that the database migrations have been applied.
- Check the console for any error messages that may provide insight into the issue.

## Support

For further assistance, please reach out to our support team or consult the documentation available in the repository.

```

This manual provides a comprehensive overview of the Student Management System, including installation instructions, usage guidelines, and troubleshooting tips. Let me know if you need any modifications or additional information!