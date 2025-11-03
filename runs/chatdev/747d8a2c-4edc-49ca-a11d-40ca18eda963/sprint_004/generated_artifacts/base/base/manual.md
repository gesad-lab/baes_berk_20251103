Here's the `manual.md` file that provides a detailed user manual for the Student Management application, including its main functions, installation instructions, and usage guidelines.

```markdown
# Student Management Application

A simple application for managing student records, including adding and fetching student information.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address, which will be stored in the database.
- **Fetch Students**: Retrieves and displays a list of all students currently stored in the database, showing their names and email addresses.

## Quick Install

To run the Student Management application, you need to set up the environment and install the necessary dependencies. Follow these steps:

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
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migration script:
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
   Once the application is running, open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the API documentation or use the GUI.

2. **Add a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Submit" button to add the student to the database. A confirmation message will appear if successful.

3. **Fetch Students**:
   - Click the "Fetch Students" button to retrieve and display the list of all students. The students will be shown in a list format, including their IDs, names, and email addresses.

## Additional Information

- **Database**: The application uses SQLite for data storage, and the database file is created in the project directory as `students.db`.
- **Error Handling**: If there is an error while adding a student, an error message will be displayed in the GUI.

## Conclusion

This Student Management application provides a straightforward way to manage student records. By following the installation and usage instructions, you can easily set up and run the application to add and view student information.

For further assistance or to report issues, please contact the development team.
```

This manual provides a comprehensive overview of the application, ensuring that users can easily install and utilize its features.