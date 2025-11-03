```markdown
# Student Management Application

A simple web application for managing student records using FastAPI and SQLite.

## Overview

This application allows users to add and view students by their names. It provides a graphical user interface (GUI) built with Tkinter that interacts with a FastAPI backend. The backend handles data persistence using an SQLite database.

## Main Functions

- **Add Student**: Users can input a student's name and add it to the database.
- **View Students**: Users can view a list of all students stored in the database.
- **API Endpoints**:
  - `POST /students/`: Add a new student.
  - `GET /students/`: Retrieve a list of all students.
  - `GET /`: Welcome message.

## Installation Instructions

### Prerequisites

Ensure you have Python 3.11+ installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```plaintext
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
   Open a terminal and run:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the FastAPI server at `http://127.0.0.1:8000`.

2. **Run the GUI**:
   In another terminal, run:
   ```bash
   python gui.py
   ```
   This will open the Student Management GUI.

## How to Use the Application

1. **Adding a Student**:
   - Enter the student's name in the input field.
   - Click the "Add Student" button.
   - A success message will appear if the student is added successfully.

2. **Viewing Students**:
   - Click the "View Students" button.
   - The list of students will be displayed in the list box.

## API Documentation

You can access the automatically generated API documentation at `http://127.0.0.1:8000/docs`.

## Troubleshooting

- **CORS Issues**: If you encounter CORS issues, ensure that the FastAPI server is running and accessible.
- **Database Issues**: If the database does not seem to be updating, check the console for any error messages.

## Conclusion

This Student Management Application provides a simple yet effective way to manage student records. Feel free to expand its functionality as needed!
```