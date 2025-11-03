Here's a detailed user manual for the Student Management software, formatted in Markdown as requested:

```markdown
# Student Management Software

A simple application for managing student records, including adding and viewing student information.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address, which will be stored in the database.
- **Show Students**: Displays a list of all students currently stored in the database, including their names and email addresses.

## Quick Install

To run the Student Management software, you need to install the required environment dependencies. Follow the steps below:

1. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Packages**: Open your terminal or command prompt and run the following command to install the necessary packages:

   ```bash
   pip install fastapi sqlalchemy pydantic requests uvicorn
   ```

3. **Install Tkinter**: Tkinter is included with most Python installations. If you encounter any issues, refer to the [Tkinter documentation](https://docs.python.org/3/library/tkinter.html) for installation instructions.

## How to Use the Software

1. **Run the Application**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the application files are located.
   - Start the FastAPI server by running:

     ```bash
     uvicorn api:app --reload
     ```

   - This will start the server at `http://127.0.0.1:8000`.

2. **Launch the GUI**:
   - In a new terminal window, run the following command to start the GUI:

     ```bash
     python gui.py
     ```

   - This will open the Student Management application window.

3. **Adding a Student**:
   - In the GUI, enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to save the information. A success message will appear if the student is added successfully.

4. **Viewing Students**:
   - Click the "Show Students" button to retrieve and display the list of all students in the application. The list will show each student's ID, name, and email.

## Additional Information

- The application uses SQLite as the database to store student records. The database file is named `students.db` and will be created in the same directory as the application files.
- The application is built using FastAPI for the backend and Tkinter for the GUI, providing a simple and user-friendly interface for managing student data.

## Support

For any issues or questions regarding the software, please contact our support team at support@chatdev.com.

```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and support information. Let me know if you need any modifications or additional details!