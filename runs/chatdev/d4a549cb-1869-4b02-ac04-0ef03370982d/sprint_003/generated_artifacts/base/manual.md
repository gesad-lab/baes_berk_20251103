Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Management Application

A simple application for managing student records, including adding and retrieving student information.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address to create a new student record.
- **Retrieve Students**: Fetches and displays a list of all students stored in the database.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-management.git
   cd student-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   pydantic
   requests
   ```

4. **Run Database Migrations**:
   To update the database schema and add the email field to the Student entity, run:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Start the FastAPI Server**:
   Run the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. **Open the GUI**:
   The application provides a simple GUI using Tkinter. Run the following command to launch the GUI:
   ```bash
   python main.py
   ```

3. **Add a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Submit" button to add the student. A success message will be displayed if the student is added successfully.

4. **Retrieve Students**:
   Currently, the application does not display the list of students in the GUI. However, you can retrieve students using the FastAPI endpoint:
   - Send a GET request to `http://127.0.0.1:8000/students/` to fetch all student records.

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file is created in the project directory as `students.db`.
- **Email Validation**: The email field is validated using Pydantic to ensure that only valid email addresses are accepted.

## Future Enhancements

- Implement a feature to display the list of students in the GUI.
- Add functionality to update and delete student records.
- Improve error handling and user feedback in the GUI.

For any issues or feature requests, please contact the development team.

```

This manual provides a comprehensive overview of the application, installation instructions, and usage guidelines, ensuring that users can effectively utilize the software.