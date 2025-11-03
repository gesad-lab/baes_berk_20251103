Here's a detailed user manual for the Student Management software, written in Markdown format:

```markdown
# Student Management Application

A simple application for managing student records, including adding and viewing student details with email support.

## Main Functions

- **Add Student**: Allows users to add a new student by entering their name and email address.
- **Show Students**: Displays a list of all students with their names and email addresses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student_management.git
   cd student_management
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
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to save the student record.
   - If successful, a confirmation message will appear in the output area.

3. **Show Students**:
   - Click the "Show Students" button to retrieve and display a list of all students.
   - The output area will show each student's ID, name, and email.

## Example Usage

1. **Adding a Student**:
   - Name: John Doe
   - Email: john.doe@example.com
   - Click "Add Student" to save.

2. **Viewing Students**:
   - Click "Show Students" to see:
     ```
     ID: 1, Name: John Doe, Email: john.doe@example.com
     ```

## Additional Information

- **Database**: The application uses SQLite for data storage, and the database file is created in the project directory.
- **Email Validation**: The application ensures that the email format is valid before adding a student.

## Troubleshooting

- If you encounter any issues, ensure that all dependencies are correctly installed and that the FastAPI server is running.
- Check the console for any error messages that may indicate what went wrong.

## Support

For further assistance, please reach out to the development team or refer to the documentation for FastAPI and SQLAlchemy.

```

This manual provides a comprehensive overview of the Student Management application, including installation instructions, usage guidelines, and troubleshooting tips.