# Course Management System

A simple application for managing students and courses using a graphical user interface (GUI) built with Tkinter and a FastAPI backend.

## Main Functions

The Course Management System allows users to:

- **Add Students**: Input student names and emails to add them to the database.
- **View Students**: Retrieve and display a list of all registered students.
- **Add Courses**: Input course names and levels to add them to the database.
- **View Courses**: Retrieve and display a list of all available courses.

## Installation

To set up the Course Management System, follow these steps:

### Prerequisites

Make sure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the Course Management System code:

```bash
git clone https://github.com/yourusername/course-management-system.git
cd course-management-system
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
pip install fastapi[all] sqlalchemy pydantic requests
```

### Step 4: Run the Application

1. **Start the FastAPI server**:

   Open a terminal and run the following command:

   ```bash
   python main.py
   ```

   This will start the FastAPI server at `http://127.0.0.1:8000`.

2. **Run the GUI**:

   In another terminal, run the following command:

   ```bash
   python gui.py
   ```

   This will open the GUI for managing students and courses.

## How to Use the Application

### Adding Students

1. Enter the student's name in the "Student Name" field.
2. Enter the student's email in the "Student Email" field.
3. Click the "Add Student" button to add the student to the database.
4. Click the "Get Students" button to view all registered students.

### Adding Courses

1. Enter the course name in the "Course Name" field.
2. Enter the course level in the "Course Level" field.
3. Click the "Add Course" button to add the course to the database.
4. Click the "Get Courses" button to view all available courses.

### Viewing Data

- The application will display the list of students and courses in the result label area after fetching the data.

## Database Migration

The application uses SQLite as the database. The migration script (`migration.py`) ensures that the Course table is created without affecting existing Student data. You can run this script to set up the database schema.

## Conclusion

The Course Management System provides a simple and effective way to manage students and courses through a user-friendly interface. Feel free to extend the functionality or customize it according to your needs!