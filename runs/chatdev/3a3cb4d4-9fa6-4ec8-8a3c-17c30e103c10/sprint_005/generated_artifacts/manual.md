```markdown
# Teacher Management System

A simple application for managing students and teachers, allowing users to add and manage their information through a user-friendly interface.

## Main Functions

- **Add Student**: Users can input student names and emails to add them to the database.
- **Add Teacher**: Users can input teacher names and emails to add them to the database.
- **Database Management**: The application manages student and teacher data using a SQLite database, preserving existing data during migrations.

## Installation Guide

To set up the Teacher Management System, follow these steps:

### Prerequisites

Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

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
pip install -r requirements.txt
```

Make sure to include the following dependencies in your `requirements.txt` file:

```
fastapi
uvicorn
pydantic
sqlalchemy
requests
tkinter  # Note: Tkinter is included with Python installations on most systems
```

### Step 4: Run Database Migration

Before running the application, you need to set up the database schema. Run the migration script:

```bash
python migration.py
```

### Step 5: Start the Application

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

### Step 6: Launch the GUI

Run the GUI application:

```bash
python main.py
```

## How to Use the Application

1. **Adding Students**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to submit the information.

2. **Adding Teachers**:
   - Enter the teacher's name in the "Enter Teacher Name" field.
   - Enter the teacher's email in the "Enter Teacher Email" field.
   - Click the "Add Teacher" button to submit the information.

3. **Feedback**:
   - After submitting, you will receive feedback on whether the addition was successful or if there was an error.

## Conclusion

This Teacher Management System provides a straightforward interface for managing student and teacher data. By following the installation and usage instructions, you can easily set up and run the application. For any issues or further assistance, please refer to the documentation or contact support.

```
