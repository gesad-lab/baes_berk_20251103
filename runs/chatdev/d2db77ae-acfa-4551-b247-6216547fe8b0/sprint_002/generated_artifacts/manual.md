```markdown
# Student Management System

A simple application for managing student records, including their names and email addresses.

## Main Functions

- **Create Student**: Add a new student with a name and email address.
- **Get Students**: Retrieve a list of all students with their names and email addresses.
- **Database Management**: Automatically handles database creation and migration to include new fields.

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI server by running:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Creating a Student**:
   - Use the `/students/` POST endpoint to create a new student.
   - Provide a JSON body with the required fields:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

4. **Retrieving Students**:
   - Use the `/students/` GET endpoint to retrieve a list of all students.
   - You can specify query parameters `skip` and `limit` to paginate the results.

5. **Database Migration**:
   - The application automatically runs database migrations to ensure that the email field is added to the Student entity without losing existing data. This is handled in the `run_migrations()` function in `database.py`.

## GUI Interaction

The application also includes a graphical user interface (GUI) built with Tkinter. To use the GUI:

1. **Run the Application**:
   Ensure the FastAPI server is running as described above.

2. **Launch the GUI**:
   The GUI is initialized in `main.py`. Simply run:
   ```bash
   python main.py
   ```

3. **Using the GUI**:
   - The GUI allows you to input student names and email addresses.
   - You can view the list of students directly from the interface.

## Conclusion

This Student Management System provides a simple yet effective way to manage student records. With the ability to create and retrieve student information, along with a user-friendly GUI, it serves as a foundational tool for educational institutions or personal projects.

For further assistance or feature requests, please contact the development team.
```