Here's the user manual for the software, formatted in Markdown as requested:

```markdown
# Student Management System

A simple application for managing student records, including adding student information with email addresses.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address, which will be stored in the database.
- **View Student**: Retrieve and display information about a specific student by their ID.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

4. **Install Alembic for database migrations**:
   ```bash
   pip install alembic
   ```

5. **Run database migrations**:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Start the FastAPI server**:
   Run the following command in your terminal:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Open the GUI**:
   In a separate terminal, run the following command to launch the Tkinter GUI:
   ```bash
   python gui.py
   ```

3. **Adding a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to submit the information.
   - A success message will be displayed if the student is added successfully.

4. **Viewing a Student**:
   (Note: The current implementation does not include a GUI for viewing students. You can use the API directly to fetch student details by their ID.)

## API Endpoints

- **POST /students**: Create a new student record.
  - Request Body:
    ```json
    {
      "name": "Student Name",
      "email": "student@example.com"
    }
    ```

- **GET /students/{student_id}**: Retrieve a student record by ID.

## Additional Information

For more detailed documentation on FastAPI, SQLAlchemy, and Pydantic, please refer to their respective official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

Feel free to reach out for support or if you have any questions regarding the application.
```

This manual provides a comprehensive overview of the Student Management System, including installation instructions, usage guidelines, and links to further documentation. Let me know if you need any modifications or additional information!