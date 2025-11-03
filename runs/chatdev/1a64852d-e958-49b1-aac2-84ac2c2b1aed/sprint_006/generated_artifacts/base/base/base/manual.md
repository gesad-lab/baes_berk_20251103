```markdown
# Course Management System

A simple application for managing courses and students using FastAPI and a Tkinter GUI.

## Main Functions

This software allows users to:

- **Create Courses**: Add new courses with a name and level.
- **View Courses**: Retrieve and display a list of all courses.
- **Manage Students**: Create and view student records (email and name).

## Installation Guide

To set up the environment and run the application, follow these steps:

### Prerequisites

Make sure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the code:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install fastapi[all] sqlalchemy alembic requests
```

### Step 4: Run Database Migrations

To set up the database schema, run the following command:

```bash
alembic upgrade head
```

### Step 5: Start the FastAPI Server

Run the FastAPI application:

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

### Step 6: Run the GUI Application

In a separate terminal, run the GUI application:

```bash
python main.py
```

## How to Use the Application

### Adding a Course

1. Open the GUI application.
2. Enter the course name in the "Enter Course Name" field.
3. Enter the course level in the "Enter Course Level" field.
4. Click the "Add Course" button to submit the course.
5. A success message will appear if the course is added successfully.

### Viewing Courses

1. Click the "Show Courses" button in the GUI.
2. A list of all courses will be displayed in the list box.

### Managing Students

- The API allows for creating and viewing students through the `/students/` endpoint.
- You can create a student by sending a POST request with the student's name and email.
- Retrieve all students by sending a GET request to the same endpoint.

## Additional Information

For more detailed documentation on FastAPI, please refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).

For any issues or support, please reach out to our support team.

Happy coding!
```