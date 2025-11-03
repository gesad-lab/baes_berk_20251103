```markdown
# Student Management Application

A simple application for managing student records, including adding and viewing student information.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address, which will be stored in the database.
- **Show Students**: Displays a list of all students currently stored in the database, showing their ID, name, and email.

## Installation

To set up the environment and run the application, follow these steps:

### Prerequisites

Make sure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Install Dependencies

Install the required Python packages using pip. You can create a virtual environment for better dependency management:

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install required packages
pip install fastapi sqlalchemy alembic requests
pip install uvicorn  # For running the FastAPI server
```

### Step 3: Initialize the Database

Before running the application, you need to initialize the database. You can do this by running the following command:

```bash
python -c "from database import init_db; init_db()"
```

### Step 4: Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The application will be running at `http://127.0.0.1:8000`.

### Step 5: Run the GUI

To run the GUI, execute the following command in a separate terminal:

```bash
python gui.py
```

## How to Use the Application

1. **Add a Student**:
   - Open the GUI.
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button.
   - If successful, the added student's information will be displayed in the output area.

2. **Show Students**:
   - Click the "Show Students" button.
   - A list of all students will be displayed in the output area, showing their ID, name, and email.

## Database Migration

If you need to update the database schema (e.g., adding new fields), you can use Alembic for migrations. To create a migration script for adding the email field, run:

```bash
alembic revision --autogenerate -m "Add email field to Student"
alembic upgrade head
```

This will ensure that the existing student data is preserved while adding the new email field.

## Conclusion

This Student Management Application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and run the application. For any issues or further assistance, please refer to the documentation or contact support.
```