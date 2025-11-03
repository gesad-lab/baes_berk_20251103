Here's the user manual for the software, formatted in Markdown as requested:

```markdown
# Student Registration System

A simple application for registering students with their names and email addresses.

## Main Functions

The Student Registration System allows users to:

- **Register a new student**: Users can input a student's name and email address to create a new student record.
- **View registered students**: Users can retrieve a list of all registered students.

## Quick Install

To set up the environment and run the application, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install required dependencies**:
   Make sure you have Python installed. Then, run:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

3. **Run the application**:
   Start the FastAPI server by executing:
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the GUI**:
   Open a new terminal window and run:
   ```bash
   python gui.py
   ```
   This will launch a simple GUI for interacting with the FastAPI application.

## How to Use the Application

### Registering a Student

1. Open the GUI application.
2. Enter the student's name in the "Student Name" field.
3. Enter the student's email in the "Student Email" field.
4. Click the "Create Student" button.
5. A message will appear indicating whether the student was successfully created or if there was an error.

### Viewing Registered Students

To view the list of registered students, you can use an API client like Postman or simply access the following URL in your web browser:
```
http://127.0.0.1:8000/students/
```
This will return a JSON response containing a list of all registered students.

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file is named `students.db` and will be created in the project directory upon the first run.
- **Data Preservation**: The database migration process ensures that existing student data is preserved when adding new fields.

## Support

For any issues or questions, please reach out to our support team at [support@example.com](mailto:support@example.com).

```

This manual provides a comprehensive overview of the Student Registration System, including installation instructions, usage guidelines, and support information. Let me know if you need any modifications or additional sections!