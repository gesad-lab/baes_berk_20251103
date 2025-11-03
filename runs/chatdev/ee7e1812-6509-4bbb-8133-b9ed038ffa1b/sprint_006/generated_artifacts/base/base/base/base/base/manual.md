```markdown
# Student Management Web Application

A simple web application for managing student records using FastAPI, SQLite, and a Tkinter GUI.

## Overview

This application allows users to add and view student records. Each student has a name, which is required. The application uses FastAPI to create a RESTful API for managing student data, and SQLite for data persistence. The GUI is built using Tkinter, providing a user-friendly interface for interaction.

## Main Functions

- **Add Student**: Users can enter a student's name and add it to the database.
- **Show Students**: Users can retrieve and display a list of all students in the database.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository** (if applicable):
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
   The server will start at `http://127.0.0.1:8000`.

2. **Run the GUI**:
   In another terminal, run the following command to start the Tkinter GUI:
   ```bash
   python gui.py
   ```

## Using the Application

1. **Add a Student**:
   - Enter the student's name in the input field.
   - Click the "Add Student" button.
   - If successful, the application will display a confirmation message.

2. **Show Students**:
   - Click the "Show Students" button.
   - The application will retrieve and display a list of all students currently in the database.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Create a new student.
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

This Student Management Web Application provides a simple and effective way to manage student records. With a user-friendly GUI and a robust backend powered by FastAPI and SQLite, it serves as a great starting point for further enhancements and features.

For any issues or feature requests, please contact the development team.
```