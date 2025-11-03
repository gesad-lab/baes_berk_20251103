```markdown
# Student Management Web Application

This is a simple web application designed to manage student records using Python, FastAPI, and SQLite. The application allows users to add students and view the list of students through a graphical user interface (GUI) built with Tkinter.

## Main Functions

- **Add Student**: Users can enter a student's name and add it to the database.
- **Show Students**: Users can view the list of all students stored in the database.

## Installation Guide

To set up the environment and run the application, follow these steps:

### Prerequisites

- Ensure you have Python 3.11+ installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Install Dependencies

Create a virtual environment (optional but recommended) and install the required dependencies listed in `requirements.txt`:

```bash
# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Run the FastAPI Application

Start the FastAPI application by running the `main.py` file:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### Step 4: Run the GUI Application

In a separate terminal, run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Add a Student**:
   - Open the GUI application.
   - Enter the student's name in the input field.
   - Click the "Add Student" button. If successful, you will see a confirmation message.

2. **Show Students**:
   - Click the "Show Students" button to retrieve and display the list of students. The output will show each student's ID and name.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Add a new student.
  - Request Body: `{ "name": "Student Name" }`
  - Response: `{ "id": <student_id>, "name": "Student Name" }`

- **GET /students/**: Retrieve a list of students.
  - Query Parameters: `skip` (optional), `limit` (optional)
  - Response: `[{ "id": <student_id>, "name": "Student Name" }, ...]`

## Conclusion

This application provides a simple interface for managing student records. You can extend its functionality by adding more features such as updating or deleting student records, implementing user authentication, or enhancing the GUI.

For any issues or feature requests, please contact the development team.
```