```markdown
# Student Management Application

A simple application for managing students and their courses, built using FastAPI and Tkinter.

## Main Functions

- **Add Student**: Allows users to create a new student profile by entering their name and email.
- **Add Course**: Enables users to create a new course by specifying its name and level.
- **View Students**: Displays a list of all registered students.
- **View Courses**: Shows a list of all available courses.

## Installation

To set up the environment and run the application, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Create a Virtual Environment

It's recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install fastapi[all] sqlalchemy alembic requests
```

### Step 4: Initialize the Database

Run the following command to create the database and tables:

```bash
python -c "from database import create_database; create_database()"
```

### Step 5: Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Then, run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Adding a Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to create the student profile.

2. **Adding a Course**:
   - Enter the course name and level in the respective fields.
   - Click the "Add Course" button to create the course.

3. **Viewing Students**:
   - Click the "View Students" button to display all registered students in the output area.

4. **Viewing Courses**:
   - Click the "View Courses" button to display all available courses in the output area.

## Database Migration

The application uses Alembic for database migrations. The migration script ensures that the existing data is preserved while adding the new `Course` entity and the many-to-many relationship between `Student` and `Course`.

## Troubleshooting

- If you encounter issues with Tkinter, ensure it is installed. You can install it via your package manager or check the Python installation options.
- For any errors related to FastAPI or SQLAlchemy, ensure all dependencies are correctly installed and the database is initialized.

## Support

For further assistance, please contact the support team or refer to the documentation for FastAPI and SQLAlchemy.

```
