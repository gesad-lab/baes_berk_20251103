Here's a detailed user manual for the software that incorporates the new email field in the Student entity. This manual will guide users on how to install the necessary dependencies, use the software, and understand its main functions.

```markdown
# Student Registration System

A simple application for registering students with their names and email addresses.

## Main Functions

The Student Registration System allows users to:

- Register new students by entering their name and email address.
- Validate email format during registration.
- Store student information in a SQLite database.
- Retrieve and display registered students through a graphical user interface (GUI).

## Quick Install

To set up the environment for the Student Registration System, follow these steps:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Ensure you have Python installed (version 3.7 or higher). Then, install the required packages using pip:
   ```bash
   pip install fastapi[all] sqlalchemy tkinter requests
   ```

3. **Run the Application**:
   Start the FastAPI application and the GUI by executing:
   ```bash
   python main.py
   ```

## How to Use the Application

1. **Launching the Application**:
   After running `main.py`, a GUI window will appear for student registration.

2. **Registering a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Submit" button to register the student.

3. **Email Validation**:
   - The application checks if the email format is valid. If the format is incorrect, a warning message will be displayed.
   - Both name and email fields are required. If either field is empty, a warning message will be shown.

4. **Success and Error Messages**:
   - Upon successful registration, a success message will be displayed.
   - If registration fails (e.g., due to server issues), an error message will appear.

## Database Schema

The application uses a SQLite database to store student information. The `students` table includes the following fields:

- `id`: Unique identifier for each student (automatically generated).
- `name`: Name of the student (required).
- `email`: Email address of the student (required).

## Additional Information

- The application is built using FastAPI for the backend and Tkinter for the GUI.
- The database is initialized automatically when the application starts, and existing student data is preserved during migrations.

## Troubleshooting

- If you encounter issues with Tkinter, ensure it is installed and available in your Python environment.
- For any errors related to database connections, check the database URL in `database.py`.

## Conclusion

The Student Registration System is a straightforward application designed to facilitate student registration with essential validation checks. Feel free to explore the code and customize it further to meet your needs!

```

This manual provides a comprehensive overview of the software, installation instructions, and usage guidelines, ensuring that users can effectively utilize the Student Registration System.