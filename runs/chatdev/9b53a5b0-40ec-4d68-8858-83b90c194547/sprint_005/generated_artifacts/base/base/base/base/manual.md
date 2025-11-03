Here's a detailed user manual for the Student Management application, structured in Markdown format as requested:

```markdown
# Student Management Application

A simple web application for managing student records using FastAPI and SQLite.

## Overview

The Student Management Application allows users to add and view student records. Each student has a name associated with their record. The application consists of a FastAPI backend that handles API requests and a Tkinter GUI for user interaction.

## Main Functions

- **Add Student**: Users can enter a student's name and add it to the database.
- **View Students**: Users can retrieve and view a list of all students stored in the database.

## Installation

To run the Student Management Application, you need to set up your environment and install the necessary dependencies. Follow the steps below:

### Step 1: Install Python

Ensure you have Python 3.11+ installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

### Step 2: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 3: Create a Virtual Environment (Optional)

It's a good practice to create a virtual environment for your project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 4: Install Dependencies

Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 5: Run the FastAPI Server

Start the FastAPI server by running the following command in the terminal:

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

### Step 6: Run the GUI Application

In a separate terminal, run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Add a Student**:
   - Open the GUI application.
   - Enter the student's name in the input field.
   - Click the "Add Student" button.
   - A confirmation message will appear if the student is successfully added.

2. **View Students**:
   - Click the "View Students" button.
   - The application will display a list of all students with their IDs and names.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Add a new student.
  - Request Body: `{ "name": "Student Name" }`
  - Response: JSON object of the added student.

- **GET /students/**: Retrieve all students.
  - Response: JSON array of student objects.

## Troubleshooting

- If you encounter issues with Tkinter, ensure it is installed. Tkinter is included with most Python installations, but you can install it separately if needed.
- Make sure the FastAPI server is running before attempting to use the GUI application.

## Conclusion

The Student Management Application is a simple yet effective tool for managing student records. By following the installation and usage instructions, you can easily set up and interact with the application.
```

This manual provides a comprehensive guide for users to understand the application, install the necessary dependencies, and utilize its features effectively.