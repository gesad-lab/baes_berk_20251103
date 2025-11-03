Here is the `manual.md` file for the Student Management web application:

```markdown
# Student Management Web Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite. This application allows users to add and view students by their names.

## Main Functions

- **Add Student**: Users can input a student's name and add it to the database.
- **View Students**: Users can view a list of all students stored in the database.

## Installation

To run the Student Management application, you need to set up your environment and install the required dependencies. Follow the steps below:

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
pip install fastapi[all] sqlalchemy requests
```

### Step 4: Run the Application

To start the FastAPI server, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### Step 5: Run the GUI

Open another terminal window and run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Add a Student**:
   - Open the GUI application.
   - Enter the student's name in the input field.
   - Click the "Add Student" button to add the student to the database.

2. **View Students**:
   - The list of students will automatically update and display in the list box after adding a student.
   - You can see the student ID and name in the list.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Add a new student.
  - Request Body: `{ "name": "Student Name" }`
  - Response: `{ "id": <student_id>, "name": "Student Name" }`

- **GET /students/**: Retrieve a list of students.
  - Query Parameters: `skip` (optional), `limit` (optional)
  - Response: `[{ "id": <student_id>, "name": "Student Name" }, ...]`

## Conclusion

This Student Management web application provides a simple interface for managing student records. Feel free to explore and modify the code as needed to fit your requirements.
```

This manual provides a comprehensive guide for users to install, run, and utilize the Student Management web application effectively.