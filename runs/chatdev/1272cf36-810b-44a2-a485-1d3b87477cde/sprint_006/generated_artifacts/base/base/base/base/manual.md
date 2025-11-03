Here's the `manual.md` file for the Student Registration application:

```markdown
# Student Registration Application

A simple application for registering students with their names and email addresses.

## Main Functions

The Student Registration Application allows users to:

- Register new students by entering their names and email addresses.
- View a list of registered students.
- Ensure that all student data is stored securely in a database.

## Quick Install

To run the Student Registration Application, you need to install the required environment dependencies. You can do this using `pip`. Open your terminal and run the following command:

```bash
pip install fastapi[all] sqlalchemy pydantic requests tkinter
```

Make sure you have Python installed on your machine (Python 3.6 or higher is recommended).

## How to Use the Application

1. **Run the FastAPI Backend:**
   - Navigate to the directory where your application files are located.
   - Run the FastAPI application by executing the following command in your terminal:
   ```bash
   uvicorn app:app --reload
   ```
   This will start the FastAPI server on `http://127.0.0.1:8000`.

2. **Run the GUI:**
   - Open another terminal window.
   - Navigate to the directory where your `gui.py` or `main.py` file is located.
   - Run the GUI application by executing:
   ```bash
   python gui.py
   ```
   or
   ```bash
   python main.py
   ```

3. **Register a Student:**
   - In the GUI, enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Email" field.
   - Click the "Add Student" button to submit the information.
   - A success message will appear if the student is added successfully; otherwise, an error message will be displayed.

4. **View Registered Students:**
   - You can retrieve the list of registered students by sending a GET request to the FastAPI endpoint:
   ```http
   GET http://127.0.0.1:8000/students/
   ```
   This will return a JSON response containing the list of students.

## Additional Information

- The application uses SQLite as the database to store student information.
- The database schema is automatically initialized when the FastAPI application starts.
- The application is built using Python with FastAPI for the backend and Tkinter for the graphical user interface.

## Support

If you encounter any issues or have questions about the application, please reach out to the support team.

Happy registering!
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and support information.