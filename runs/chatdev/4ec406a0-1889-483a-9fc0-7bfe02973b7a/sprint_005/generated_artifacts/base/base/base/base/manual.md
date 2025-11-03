Here's a detailed user manual for the Student Management application, structured in Markdown format:

```markdown
# Student Management Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite.

## Overview

The Student Management Application allows users to add and view student names. It features a graphical user interface (GUI) built with Tkinter, which interacts with a FastAPI backend to handle data persistence using SQLite.

## Main Functions

- **Add Student**: Users can input a student's name and add it to the database.
- **Fetch Students**: Users can retrieve and view the list of all students stored in the database.

## Installation Instructions

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

### Step 3: Run the FastAPI Application

Start the FastAPI backend server:

```bash
uvicorn main:app --reload
```

This will run the application on `http://127.0.0.1:8000`.

### Step 4: Run the GUI Application

In a separate terminal, run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Adding a Student**:
   - Open the GUI application.
   - Enter the student's name in the input field.
   - Click the "Add Student" button to save the student to the database.

2. **Fetching Students**:
   - Click the "Fetch Students" button to retrieve the list of all students.
   - The names of the students will be displayed in the list box.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Add a new student.
  - Request Body: 
    ```json
    {
      "name": "Student Name"
    }
    ```
  - Response: Returns the created student object.

- **GET /students/**: Retrieve the list of all students.
  - Response: Returns a list of student objects.

## Conclusion

This Student Management Application provides a simple yet effective way to manage student records using modern web technologies. For any issues or feature requests, please contact the development team.

```

This manual provides a comprehensive guide for users to understand the application, install it, and utilize its features effectively.