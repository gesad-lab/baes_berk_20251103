```markdown
# Student Management Application

A simple web application for managing student records using FastAPI and SQLite.

## Overview

This application allows users to create and manage student records with a focus on the student's name. It features a graphical user interface (GUI) built with Tkinter, which interacts with a FastAPI backend to perform CRUD operations on student data stored in an SQLite database.

## Main Functions

- **Add Student**: Users can input a student's name and add it to the database.
- **Fetch Students**: Users can retrieve and display a list of all students stored in the database.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd chatdev_student_app
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

1. **Start the FastAPI Backend**:
   Open a terminal and navigate to the project directory. Run the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   The server will start at `http://127.0.0.1:8000`.

2. **Launch the GUI**:
   In another terminal, run the following command to start the Tkinter GUI:
   ```bash
   python gui.py
   ```

## How to Use the Application

1. **Adding a Student**:
   - Open the GUI application.
   - Enter the student's name in the input field.
   - Click the "Add Student" button. A success message will appear if the student is added successfully.

2. **Fetching Students**:
   - Click the "Fetch Students" button to retrieve the list of all students.
   - The names of the students will be displayed in the list box.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Create a new student.
  - Request Body: `{ "name": "Student Name" }`
  - Response: Returns the created student object.

- **GET /students/**: Retrieve a list of students.
  - Query Parameters: `skip` (optional), `limit` (optional)
  - Response: Returns a list of student objects.

## Conclusion

This Student Management Application provides a simple yet effective way to manage student records using modern web technologies. Feel free to explore and modify the code as needed to fit your requirements.
```