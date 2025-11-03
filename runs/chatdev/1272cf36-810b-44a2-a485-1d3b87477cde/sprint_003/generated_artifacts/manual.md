```markdown
# Student and Course Management Application

A simple application for managing student registrations and course information.

## Main Functions

This application allows users to:
- Register new students with their names and email addresses.
- Add new courses with a name and level.
- View the list of registered students and courses.

## Quick Install

To run this application, you need to install the required dependencies. You can do this using pip:

```bash
pip install fastapi[all] sqlalchemy pydantic requests tkinter
```

## Environment Setup

1. **Install Python**: Ensure you have Python 3.7 or higher installed on your machine.
2. **Install Dependencies**: Use the command provided above to install the necessary packages.
3. **Database Setup**: The application uses SQLite for database management, which is included with Python. No additional setup is required for the database.

## How to Use the Application

### Running the Application

1. **Start the FastAPI Server**:
   - Open a terminal and navigate to the directory containing your application files.
   - Run the following command to start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```
   - The server will start at `http://127.0.0.1:8000`.

2. **Open the GUI**:
   - In a separate terminal, run the GUI application:
   ```bash
   python main.py
   ```
   - This will open a graphical user interface for the application.

### Adding Students

1. **Enter Student Information**:
   - In the GUI, enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Email" field.

2. **Add Student**:
   - Click the "Add Student" button to register the student.
   - A success message will appear if the student is added successfully.

### Adding Courses

1. **Enter Course Information**:
   - Use the same fields as for student information: enter the course name in the "Student Name" field and the course level in the "Email" field.

2. **Add Course**:
   - Click the "Add Course" button to register the course.
   - A success message will appear if the course is added successfully.

### Viewing Students and Courses

- The application currently does not have a direct feature to view the list of students and courses through the GUI. However, you can access the following endpoints via a web browser or API client (like Postman):
  - **View Students**: `GET http://127.0.0.1:8000/students/`
  - **View Courses**: `GET http://127.0.0.1:8000/courses/`

## Troubleshooting

- If you encounter any issues while running the application, ensure that all dependencies are installed correctly.
- Check the terminal for any error messages that may indicate what went wrong.

## Conclusion

This application provides a straightforward way to manage student registrations and courses. Feel free to extend its functionality as needed!
```