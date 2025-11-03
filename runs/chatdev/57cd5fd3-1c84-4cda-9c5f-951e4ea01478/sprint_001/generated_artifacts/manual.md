Here's a detailed user manual for the Student Management web application, structured in Markdown format as requested:

```markdown
# Student Management Web Application

A simple web application for managing student records, allowing users to add and view students by their names.

## Main Functions

- **Add Student**: Users can input a student's name and add it to the database.
- **View Students**: Users can retrieve and view a list of all students stored in the database.

## Quick Install

To run the Student Management application, you need to install the required dependencies. Follow the steps below:

1. **Install Python 3.11+**: Ensure you have Python 3.11 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:
   Use pip to install FastAPI, SQLAlchemy, and other dependencies:
   ```bash
   pip install fastapi[all] sqlalchemy
   ```

## How to Run the Application

1. **Start the FastAPI Server**:
   Navigate to the directory where your `main.py` file is located and run:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the FastAPI server at `http://127.0.0.1:8000`.

2. **Run the GUI Application**:
   In a separate terminal, run the GUI application:
   ```bash
   python gui.py
   ```

3. **Access the Application**:
   - Open the GUI application window.
   - Enter a student's name in the input field and click "Add Student" to add the student to the database.
   - Click "View Students" to see the list of all students.

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

- **GET /students/**: Retrieve a list of students.
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

- **Tkinter Not Installed**: If you encounter an error stating that Tkinter is not installed, please install it using your package manager or ensure you have the correct Python version that includes Tkinter.

- **Server Not Running**: Ensure that the FastAPI server is running before trying to add or view students through the GUI.

## Conclusion

This Student Management web application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and run the application on your local machine.
```

This manual provides a comprehensive overview of the application, including installation instructions, usage, and troubleshooting tips, ensuring that users can effectively utilize the software.