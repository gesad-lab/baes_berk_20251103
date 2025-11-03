```markdown
# Student Management Web Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite. This application allows users to add and view students by their names.

## Main Functions

- **Add Student**: Users can input a student's name and add it to the database.
- **Show Students**: Users can view a list of all students stored in the database.

## Installation Guide

To run this application, you need to set up your environment and install the necessary dependencies. Follow the steps below:

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository containing the application files:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment to manage dependencies:

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

This command will run the application on `http://127.0.0.1:8000`. The `--reload` flag enables auto-reload for development.

### Step 5: Run the GUI Application

In a separate terminal, run the GUI application:

```bash
python gui.py
```

This will open a Tkinter window where you can interact with the application.

## How to Use the Application

1. **Adding a Student**:
   - Enter the student's name in the input field.
   - Click the "Add Student" button.
   - A success message will appear if the student is added successfully.

2. **Viewing Students**:
   - Click the "Show Students" button.
   - A list of all students will be displayed in the list box.

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

- **GET /students/**: Retrieves a list of all students.
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

This Student Management Web Application provides a simple interface for managing student records. With FastAPI and SQLite, it offers a lightweight solution for basic CRUD operations. Feel free to modify and expand upon this application as needed!
```