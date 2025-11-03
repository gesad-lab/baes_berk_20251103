```markdown
# Student Management System

A simple application for managing students and courses using a graphical user interface (GUI) built with Tkinter and a FastAPI backend.

## Main Functions

The Student Management System allows users to:

- **Add Students**: Users can input student names and emails to create new student records.
- **View Students**: Users can retrieve and display a list of all registered students.
- **Add Courses**: Users can input course names and levels to create new course records.
- **View Courses**: Users can retrieve and display a list of all available courses.

## Installation

To set up the Student Management System, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the code:

```bash
git clone https://github.com/your-repo/student-management-system.git
cd student-management-system
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

### Step 4: Create the Database

Run the following command to create the database and tables:

```bash
python -c "from database import create_database; create_database()"
```

### Step 5: Run the FastAPI Server

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The server will be running at `http://127.0.0.1:8000`.

### Step 6: Run the GUI Application

In a new terminal window, ensure your virtual environment is activated and run:

```bash
python gui.py
```

The GUI application will open, allowing you to interact with the Student Management System.

## How to Use the Application

1. **Adding a Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to create a new student record.

2. **Viewing Students**:
   - Click the "View Students" button to display a list of all registered students.

3. **Adding a Course**:
   - Enter the course name and level in the respective fields.
   - Click the "Add Course" button to create a new course record.

4. **Viewing Courses**:
   - Click the "View Courses" button to display a list of all available courses.

## Additional Information

- The application uses SQLite as the database, and all data is stored in `students.db`.
- The backend is built using FastAPI, which provides a RESTful API for managing students and courses.
- The GUI is built using Tkinter, providing a simple interface for user interaction.

For any issues or feature requests, please contact the development team.

```
