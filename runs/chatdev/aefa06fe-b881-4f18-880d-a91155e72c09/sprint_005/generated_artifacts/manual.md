```markdown
# Teacher Management Application

A simple application for managing teacher entities, allowing users to create and store teacher information including their names and email addresses.

## Main Functions

- **Create Teacher**: Users can input a teacher's name and email to create a new teacher record in the database.
- **Database Management**: The application manages a SQLite database to store teacher, student, and course information.
- **Data Preservation**: The migration scripts ensure that existing student and course data is preserved when updating the database schema.

## Installation Guide

To set up the Teacher Management Application, follow these steps:

### Prerequisites

Ensure you have Python 3.6 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

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
pip install sqlalchemy alembic pydantic tkinter
```

### Step 4: Run Database Migrations

Before running the application, you need to apply the database migrations to create the necessary tables:

```bash
alembic upgrade head
```

## How to Use the Application

1. **Start the Application**: Run the main application script to launch the GUI.

   ```bash
   python main.py
   ```

2. **Create a Teacher**:
   - Enter the teacher's name in the "Name" field.
   - Enter the teacher's email in the "Email" field.
   - Click on the "Create Teacher" button to save the teacher record.

3. **Check for Success**: Upon successful creation, a message will be printed in the console indicating that the teacher was created successfully.

## Additional Information

- **Database**: The application uses SQLite as the database backend, and the database file will be created in the project directory as `students.db`.
- **Data Models**: The application defines models for `Student`, `Course`, and `Teacher` using SQLAlchemy, allowing for easy interaction with the database.
- **Error Handling**: The application includes basic error handling to manage database operations and user input validation.

For further assistance or to report issues, please contact the development team.

```
