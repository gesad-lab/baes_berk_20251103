Here's a detailed user manual for the Student Management application, formatted in Markdown:

```markdown
# Student Management Application

A simple application for managing student records, including adding and viewing student information.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address to create a new student record.
- **Show Students**: Displays a list of all students currently stored in the database, showing their ID, name, and email address.

## Quick Install

To run the Student Management application, you need to install the required environment dependencies. Follow these steps:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Install Dependencies**:
   Make sure you have Python installed (version 3.7 or higher). Then, install the required packages using pip:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

3. **Run the Application**:
   Start the FastAPI server by running:
   ```bash
   uvicorn main:app --reload
   ```

   This will start the server at `http://127.0.0.1:8000`.

## How to Use the Application

1. **Launch the GUI**:
   After starting the FastAPI server, run the GUI application:
   ```bash
   python main.py
   ```

2. **Add a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to submit the information. A success message will appear if the student is added successfully.

3. **View Students**:
   - Click the "Show Students" button to retrieve and display the list of all students in the application. The list will show each student's ID, name, and email.

## Error Handling

- If you attempt to add a student without filling in both the name and email fields, a warning message will prompt you to enter the required information.
- If there is an issue with adding a student (e.g., server error), an error message will inform you of the failure.

## Additional Information

- The application uses SQLite as the database to store student records.
- The email field is validated to ensure it contains a properly formatted email address.
- The application is built using FastAPI for the backend and Tkinter for the graphical user interface.

For further assistance or support, please contact the development team.

```

This manual provides a comprehensive overview of the Student Management application, including installation instructions, usage guidelines, and error handling information. It is designed to help users quickly understand and effectively use the software.