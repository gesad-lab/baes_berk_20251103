```markdown
# Student Management Application

A simple application for managing student records, including adding and listing students with their email addresses.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address, which are then stored in the database.
- **List Students**: Displays a list of all students in the database along with their email addresses.

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the API Server**:
   In the terminal, navigate to the project directory and run:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the FastAPI server at `http://127.0.0.1:8000`.

2. **Run the GUI**:
   Open another terminal window, navigate to the project directory, and run:
   ```bash
   python gui.py
   ```
   This will launch the Student Management GUI.

3. **Adding a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to save the student record.

4. **Listing Students**:
   - Click the "List Students" button to retrieve and display all students in the database along with their email addresses.

## Database Migration

The application includes a database migration that preserves existing student data while adding the new email field. The database schema has been updated to include the email field in the `Student` entity.

## Troubleshooting

- Ensure that the FastAPI server is running before trying to add or list students from the GUI.
- If you encounter any issues, check the terminal for error messages and ensure all dependencies are installed correctly.

## Conclusion

This Student Management Application provides a straightforward way to manage student records. By following the installation and usage instructions, you can easily set up and run the application.
```