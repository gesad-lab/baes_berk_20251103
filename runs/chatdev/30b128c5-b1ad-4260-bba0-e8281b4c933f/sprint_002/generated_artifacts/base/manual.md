Here’s a detailed user manual for the Student Management application, structured in Markdown format as requested:

```markdown
# Student Management Application

A simple web application for managing student records using FastAPI and SQLite.

## Overview

The Student Management Application allows users to add and fetch student records. Each student has a name, which is a required field. The application provides a graphical user interface (GUI) built with Tkinter for easy interaction with the FastAPI backend.

## Main Functions

- **Add Student**: Users can input a student's name and submit it to the database.
- **Fetch Students**: Users can retrieve and view a list of all students stored in the database.

## Installation Instructions

To run the Student Management Application, you need to set up your environment and install the required dependencies.

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

It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required packages using pip:

```bash
pip install fastapi[all] sqlalchemy requests
```

### Step 4: Run the FastAPI Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

This will run the application on `http://127.0.0.1:8000`.

### Step 5: Run the GUI Application

In a separate terminal, run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Open the GUI**: After running `gui.py`, a window will appear.
2. **Add a Student**:
   - Enter the student's name in the provided text field.
   - Click the "Add Student" button.
   - If successful, a confirmation message will appear in the output area.
3. **Fetch Students**:
   - Click the "Fetch Students" button to retrieve the list of students.
   - The list will be displayed in the output area, showing each student's ID and name.

## Troubleshooting

- If you encounter an error stating that `tkinter` is not installed, you can install it using your system's package manager or by ensuring you have the correct Python installation that includes Tkinter.
- Ensure that the FastAPI server is running before trying to add or fetch students from the GUI.

## Conclusion

The Student Management Application provides a simple yet effective way to manage student records using modern web technologies. Feel free to modify and enhance the application as per your requirements.

For any further assistance, please contact our support team.
```

This manual provides a comprehensive guide for users to understand the application, install the necessary dependencies, and use the software effectively.