```markdown
# Student Application

A simple web application for managing student records using FastAPI and SQLite.

## Overview

The Student Application allows users to create and manage student records with a focus on the student's name. The application is built using Python 3.11+ and utilizes the FastAPI framework for the backend, with SQLite as the database for persistence.

## Main Functions

- **Create Student**: Users can enter a student's name, which will be stored in the SQLite database.
- **View Students**: The application can be extended to retrieve and display a list of all students (this functionality can be added in the future).
- **User Interface**: A simple GUI built with Tkinter allows users to interact with the FastAPI application.

## Installation Guide

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository containing the application files:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Step 3: Run the FastAPI Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be running at `http://127.0.0.1:8000`.

### Step 4: Run the GUI Application

In a separate terminal, run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Open the GUI**: After running `gui.py`, a window will appear prompting you to enter a student's name.
2. **Enter Student Name**: Type the name of the student you wish to add in the input field.
3. **Submit**: Click the "Submit" button. If the student is added successfully, a confirmation message will be displayed. If there is an error, an error message will appear.
4. **Check Database**: You can check the `students.db` SQLite database file to see the records.

## Future Enhancements

- Implement functionality to view all students.
- Add error handling and validation for user inputs.
- Extend the GUI to display existing student records.

## Support

For any issues or questions, please contact the support team at [support@chatdev.com](mailto:support@chatdev.com).

```
