```markdown
# Student Management Application

A simple web application for managing student records using FastAPI and SQLite.

## Overview

This application allows users to create and retrieve student records. Each student has a name, which is a required field. The application provides a graphical user interface (GUI) built with Tkinter for easy interaction.

## Main Functions

- **Add Student**: Users can enter a student's name and submit it to the database.
- **Get Students**: Users can retrieve a list of all students stored in the database.

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
   This will start the FastAPI server at `http://127.0.0.1:8000`.

2. **Launch the GUI**:
   In another terminal, run the following command to start the GUI:
   ```bash
   python gui.py
   ```

## Usage

### Adding a Student

1. Open the GUI application.
2. Enter the student's name in the input field.
3. Click the "Submit" button to add the student. A success message will appear if the student is added successfully.

### Retrieving Students

1. Click the "Get Students" button in the GUI.
2. The application will display a list of all students with their IDs and names.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Create a new student.
  - Request Body: `{ "name": "Student Name" }`
  - Response: Returns the created student object.

- **GET /students/**: Retrieve a list of students.
  - Response: Returns a list of student objects.

## Conclusion

This Student Management Application provides a simple interface for managing student records. It leverages FastAPI for the backend and Tkinter for the GUI, making it easy to add and retrieve student information.

For any issues or feature requests, please contact the development team.
```