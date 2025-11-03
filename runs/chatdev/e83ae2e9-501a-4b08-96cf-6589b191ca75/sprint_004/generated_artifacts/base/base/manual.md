```markdown
# Student Management Application

A simple application for managing student records, including adding and viewing students with their email addresses.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address, which are then stored in the database.
- **View Students**: Displays a list of all students along with their email addresses.

## Installation Guide

To set up the Student Management Application, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It is a good practice to create a virtual environment for your project to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip. Create a `requirements.txt` file with the following content:

```
fastapi
uvicorn
sqlalchemy
alembic
requests
```

Then run:

```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migration

Before running the application, you need to apply the database migration to add the email field to the Student entity. Run the migration script:

```bash
alembic upgrade head
```

### Step 5: Start the Application

Run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

### Step 6: Launch the GUI

Run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Adding a Student**:
   - Open the GUI application.
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to save the student record.
   - A success message will appear if the student is added successfully.

2. **Viewing Students**:
   - Click the "View Students" button to display a list of all students along with their email addresses in the list box.

## Additional Information

- The application uses FastAPI for the backend API and Tkinter for the GUI.
- The database is managed using SQLAlchemy, and migrations are handled by Alembic.
- Ensure that the FastAPI server is running before using the GUI to interact with the application.

For further assistance or feature requests, please contact the development team.

```
