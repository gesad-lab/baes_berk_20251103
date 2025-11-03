```markdown
# Student Application

A simple web application for managing student records using Python, FastAPI, and SQLite.

## Overview

The Student Application allows users to add and list students by their names. It features a graphical user interface (GUI) built with Tkinter that interacts with a FastAPI backend. The application uses SQLite for persistent storage of student records.

## Main Functions

- **Add Student**: Users can input a student's name and add it to the database.
- **List Students**: Users can retrieve and display a list of all students stored in the database.

## Installation

To set up the environment and run the application, follow these steps:

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Install Dependencies

Create a virtual environment (optional but recommended) and install the required dependencies:

```bash
# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Run the FastAPI Backend

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The FastAPI application will be running at `http://127.0.0.1:8000`.

### Step 4: Run the GUI Application

In a separate terminal, run the GUI application:

```bash
python gui.py
```

## Usage

1. **Add Student**:
   - Enter the student's name in the input field.
   - Click the "Add Student" button.
   - A success message will appear if the student is added successfully.

2. **List Students**:
   - Click the "List Students" button.
   - The application will display a list of all students with their IDs and names.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Adds a new student.
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

- **GET /students/**: Retrieves a list of students.
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

This Student Application is a simple yet effective tool for managing student records. It demonstrates the use of FastAPI for backend development, SQLite for database management, and Tkinter for creating a user-friendly GUI. Feel free to extend its functionality or customize it to suit your needs!
```