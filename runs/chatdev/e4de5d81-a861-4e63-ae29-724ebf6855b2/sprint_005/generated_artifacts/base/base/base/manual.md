Here's the detailed user manual for the software, including the introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Student Management System

A simple application for managing student records, including the ability to create and retrieve student information.

## Main Functions

- **Create Student**: Allows users to add a new student by providing their name and email address.
- **Get Students**: Fetches and displays a list of all students, showing their ID, name, and email.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-management-system.git
   cd student-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

1. **Launch the GUI**:
   - After running the application, a GUI will open using Tkinter.

2. **Adding a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to create a new student record.
   - A success message will appear if the student is created successfully.

3. **Retrieving Students**:
   - Click the "Get Students" button to fetch and display a list of all students.
   - The list will show each student's ID, name, and email.

## Additional Information

- **Database**: The application uses SQLite for storing student records. The database file is named `students.db` and will be created in the project directory upon the first run.
- **Data Persistence**: The application ensures that existing student data is preserved during updates to the database schema.

## Troubleshooting

- If you encounter issues while running the application, ensure that all dependencies are correctly installed and that the FastAPI server is running.
- Check the console for any error messages that may indicate what went wrong.

## Conclusion

This Student Management System provides a straightforward way to manage student records through a simple GUI. Feel free to customize and extend the application as needed to fit your requirements.
```

This manual provides a comprehensive overview of the software, guiding users through installation and usage while highlighting its main features.