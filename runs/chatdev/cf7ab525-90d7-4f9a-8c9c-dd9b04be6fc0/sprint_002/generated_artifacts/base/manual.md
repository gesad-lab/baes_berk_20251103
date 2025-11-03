```markdown
# Student Management Web Application

This is a simple web application designed to manage student records using FastAPI and SQLite. The application allows users to add students and view the list of students through a graphical user interface (GUI) built with Tkinter.

## Main Functions

- **Add Student**: Users can input a student's name and add it to the database.
- **Show Students**: Users can view the list of all students stored in the database.

## Installation Guide

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

### Step 2: Create a Virtual Environment (Optional but Recommended)

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Run the FastAPI Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be running at `http://127.0.0.1:8000`.

### Step 5: Run the GUI Application

In a separate terminal, run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Add a Student**:
   - Enter the student's name in the input field.
   - Click the "Add Student" button.
   - If successful, a confirmation message will appear in the output area.

2. **Show Students**:
   - Click the "Show Students" button.
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

This application provides a simple yet effective way to manage student records using modern web technologies. Feel free to modify and enhance the application as needed to suit your requirements.

For any issues or feature requests, please contact the development team.
```