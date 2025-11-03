```markdown
# Student Management Application

A simple web application for managing student records using Python, FastAPI, and SQLite.

## Overview

This application allows users to add and view students through a graphical user interface (GUI). Each student has a name, which is stored in an SQLite database. The application provides a RESTful API for managing student data, ensuring that all interactions return JSON responses.

## Main Functions

- **Add Student**: Users can input a student's name and submit it to be added to the database.
- **View Students**: Users can view a list of all students stored in the database.

## Installation

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
   Open a terminal and navigate to the `student_app` directory. Run the following command:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the FastAPI server on `http://127.0.0.1:8000`.

2. **Run the GUI Application**:
   In another terminal, run the GUI application:
   ```bash
   python gui.py
   ```

## How to Use the Application

1. **Adding a Student**:
   - Open the GUI application.
   - Enter the student's name in the input field.
   - Click the "Add Student" button.
   - A success message will appear if the student is added successfully.

2. **Viewing Students**:
   - Click the "View Students" button in the GUI.
   - A dialog will display a list of all students currently in the database.

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

This Student Management Application provides a simple yet effective way to manage student records using modern web technologies. By following the installation and usage instructions, you can easily set up and run the application on your local machine.

For further assistance or feature requests, please contact the development team.
```