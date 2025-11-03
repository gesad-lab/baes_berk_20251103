Here's a detailed user manual for the Student Management web application, structured in Markdown format:

```markdown
# Student Management Web Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite. This application allows users to add and list students through a graphical user interface (GUI).

## Main Functions

- **Add Student**: Enter a student's name and add it to the database.
- **List Students**: Retrieve and display a list of all students stored in the database.

## Installation Instructions

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
   Create a `requirements.txt` file with the following content:
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

## Running the Application

1. **Start the FastAPI Server**:
   Open a terminal and navigate to the `student_app` directory. Run the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Launch the GUI**:
   In another terminal, run the following command to start the GUI application:
   ```bash
   python gui.py
   ```

## How to Use the Application

1. **Add a Student**:
   - In the GUI, enter the student's name in the input field.
   - Click the "Add Student" button.
   - If successful, the application will display a confirmation message with the added student's details.

2. **List Students**:
   - Click the "List Students" button in the GUI.
   - The application will display a list of all students currently stored in the database.

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

## Conclusion

This Student Management Web Application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and run the application. If you encounter any issues or have questions, please reach out for support.
```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, usage guidelines, and API endpoints. It is structured to be user-friendly and informative for anyone looking to use the software.