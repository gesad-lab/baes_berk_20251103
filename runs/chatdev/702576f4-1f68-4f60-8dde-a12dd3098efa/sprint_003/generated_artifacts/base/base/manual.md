Here's a detailed user manual for the Student Management application, structured in Markdown format:

```markdown
# Student Management Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite.

## Main Functions

The Student Management application allows users to:

- **Add a Student**: Input a student's name to add them to the database.
- **View Students**: Retrieve and display a list of all students stored in the database.

## Quick Install

To run the application, you need to install the required dependencies. Follow the steps below:

1. **Install Python 3.11+**: Ensure you have Python 3.11 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Packages**: Open your terminal or command prompt and run the following command to install FastAPI, SQLAlchemy, and Uvicorn:

   ```bash
   pip install fastapi[all] sqlalchemy uvicorn requests
   ```

## How to Use the Application

### Step 1: Start the FastAPI Server

1. Navigate to the directory where your application files are located (e.g., `main.py`, `models.py`, `database.py`, `api.py`, `gui.py`).
2. Run the FastAPI application using Uvicorn:

   ```bash
   python main.py
   ```

3. The server will start and listen on `http://127.0.0.1:8000`.

### Step 2: Launch the GUI

1. Open another terminal window or command prompt.
2. Run the GUI application:

   ```bash
   python gui.py
   ```

3. A window will appear, allowing you to interact with the application.

### Step 3: Adding a Student

1. In the GUI, enter the student's name in the input field.
2. Click the "Add Student" button.
3. A success message will appear if the student was added successfully. If there is an error, an error message will be displayed.

### Step 4: Viewing Students

1. Click the "Show Students" button in the GUI.
2. A message box will display a list of all students currently in the database.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Add a new student.
  - Request Body: 
    ```json
    {
      "name": "Student Name"
    }
    ```
  - Response: 
    ```json
    {
      "id": 1,
      "name": "Student Name"
    }
    ```

- **GET /students/**: Retrieve a list of students.
  - Query Parameters: 
    - `skip`: Number of records to skip (default is 0).
    - `limit`: Maximum number of records to return (default is 10).
  - Response: 
    ```json
    [
      {
        "id": 1,
        "name": "Student Name"
      },
      ...
    ]
    ```

## Conclusion

This Student Management application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and run the application on your local machine. For any issues or questions, please refer to the documentation or contact support.
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and API details, ensuring users can effectively utilize the software.