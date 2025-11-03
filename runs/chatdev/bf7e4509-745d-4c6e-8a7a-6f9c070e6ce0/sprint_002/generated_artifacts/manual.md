```markdown
# Student Management Application

A simple application for managing student records, including adding and viewing student information.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address to create a new student record.
- **View Students**: Displays a list of all students along with their IDs, names, and email addresses.

## Installation Guide

To run the Student Management Application, you need to set up your environment and install the required dependencies. Follow the steps below:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Install Dependencies

Install the required Python packages using pip:

```bash
pip install fastapi[all] sqlalchemy alembic requests
```

### Step 3: Set Up the Database

Before running the application, you need to create the database. You can do this by running the following command in the terminal:

```bash
python -c "from database import create_database; create_database()"
```

### Step 4: Run the Application

Start the FastAPI server by executing:

```bash
uvicorn main:app --reload
```

This will run the application on `http://127.0.0.1:8000`.

### Step 5: Access the GUI

Open a new terminal window and run the GUI application:

```bash
python main.py
```

This will open a Tkinter window where you can interact with the application.

## How to Use the Application

1. **Adding a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to save the student record.

2. **Viewing Students**:
   - The list of students will automatically update to show all added students, displaying their IDs, names, and email addresses.

## Database Migration

The application includes a migration script to add the email field to the Student entity. To apply the migration, run the following command:

```bash
alembic upgrade head
```

This will add the email column to the existing Student records while preserving the existing data.

## Conclusion

This Student Management Application provides a simple interface for managing student records. You can easily add and view students, and the application is built using FastAPI and Tkinter for a smooth user experience. For any issues or feature requests, please contact the development team.

```
