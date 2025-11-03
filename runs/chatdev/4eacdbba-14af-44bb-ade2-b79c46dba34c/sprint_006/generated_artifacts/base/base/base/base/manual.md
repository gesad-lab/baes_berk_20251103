```markdown
# Student Management Application

A simple application for managing student records, including adding and retrieving student information with email support.

## Main Functions

- **Add Student**: Allows users to input a student's name and email, which are then stored in the database.
- **Get Students**: Retrieves and displays a list of all students stored in the database, including their names and emails.

## Installation Guide

To set up the environment and run the application, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Create a Virtual Environment (Optional)

It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migration

Before running the application, ensure the database schema is updated to include the new email field. Run the migration script using Alembic:

```bash
alembic upgrade head
```

### Step 5: Start the Application

Run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## How to Use the Application

### Adding a Student

1. Open the GUI application.
2. Enter the student's name in the "Enter Student Name" field.
3. Enter the student's email in the "Enter Student Email" field.
4. Click the "Submit" button to add the student. A success message will appear if the student is added successfully.

### Retrieving Students

1. Click the "Get Students" button to fetch and display the list of all students.
2. The output area will show each student's ID, name, and email.

## Additional Information

### Dependencies

- **fastapi**: Web framework for building the API.
- **uvicorn**: ASGI server for running the FastAPI application.
- **sqlalchemy**: ORM for database interactions.
- **pydantic**: Data validation and settings management.
- **requests**: For making HTTP requests in the GUI.
- **alembic**: For handling database migrations.

### Note

- **tkinter**: The GUI toolkit is included with Python's standard library and does not require installation.

For further documentation and examples, please refer to the official FastAPI documentation at [FastAPI Docs](https://fastapi.tiangolo.com/).

```
