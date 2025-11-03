```markdown
# Student Management Application

A simple web application for managing student records using Python, FastAPI, and SQLite.

## Overview

This application allows users to add and list students by their names. It features a graphical user interface (GUI) built with Tkinter that interacts with a FastAPI backend. The backend handles the creation and retrieval of student records stored in an SQLite database.

## Main Functions

- **Add Student**: Users can enter a student's name and add it to the database.
- **List Students**: Users can view all students stored in the database.

## Installation Guide

### Prerequisites

Ensure you have Python 3.11+ installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment for your project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

1. **Start the FastAPI server**:

   Open a terminal and navigate to the `student_app` directory. Run the following command:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the FastAPI server at `http://127.0.0.1:8000`.

2. **Run the GUI**:

   Open another terminal (keeping the FastAPI server running) and run the GUI application:

   ```bash
   python gui.py
   ```

## How to Use the Application

1. **Adding a Student**:
   - In the GUI, enter the student's name in the input field.
   - Click the "Add Student" button.
   - If successful, a confirmation message will appear in the output area.

2. **Listing Students**:
   - Click the "List Students" button.
   - The application will display all students currently stored in the database in the output area.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Create a new student.
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

## Conclusion

This Student Management Application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and run the application on your local machine. For any issues or feature requests, please reach out to the development team.

Happy coding!
```