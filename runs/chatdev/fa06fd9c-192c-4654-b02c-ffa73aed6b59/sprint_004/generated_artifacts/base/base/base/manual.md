Here's a detailed user manual for the Student Management web application, structured in Markdown format as requested:

```markdown
# Student Management Web Application

A simple web application to manage student records, allowing users to add and view students by their names.

## Main Functions

- **Add Student**: Users can input a student's name and add it to the database.
- **Show Students**: Users can view a list of all students currently stored in the database.

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
   Create a `requirements.txt` file in the root of the project with the following content:
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

## How to Run the Application

1. **Start the FastAPI Server**:
   Open a terminal and navigate to the `student_app` directory. Run the following command:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the FastAPI server at `http://127.0.0.1:8000`.

2. **Run the GUI**:
   In another terminal, ensure you are in the `student_app` directory and run:
   ```bash
   python gui.py
   ```
   This will open a Tkinter GUI for the Student Management application.

## How to Use the Application

1. **Adding a Student**:
   - In the GUI, enter the student's name in the input field labeled "Student Name".
   - Click the "Add Student" button. If successful, the student will be added to the database.

2. **Viewing Students**:
   - Click the "Show Students" button to display a list of all students currently in the database. The names will appear in the list box.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Add a new student.
  - **Request Body**: 
    ```json
    {
      "name": "Student Name"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Student Name"
    }
    ```

- **GET /students/**: Retrieve a list of all students.
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Student Name"
      },
      ...
    ]
    ```

## Troubleshooting

- Ensure that the FastAPI server is running before you attempt to use the GUI.
- If you encounter any issues, check the terminal for error messages and ensure all dependencies are installed correctly.

## Conclusion

This Student Management web application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and run the application.
```

This manual provides a comprehensive guide for users to understand the application, install it, and use its features effectively.