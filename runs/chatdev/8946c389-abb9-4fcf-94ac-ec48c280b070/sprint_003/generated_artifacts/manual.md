```markdown
# Course and Student Management System

A simple application for managing students and courses, built using FastAPI and Tkinter.

## Main Functions

This software provides the following functionalities:

- **Student Management**:
  - Add new students with their names and email addresses.
  - Retrieve a list of all registered students.

- **Course Management**:
  - Add new courses with their names and levels.
  - Retrieve a list of all available courses.

## Installation

To set up the environment and install the required dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:
   Install the necessary dependencies using pip:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migrations**:
   To create the necessary database tables, run the following command:
   ```bash
   alembic upgrade head
   ```

## How to Use

### Starting the Application

1. **Run the Application**:
   Start the FastAPI application and the GUI by executing:
   ```bash
   python main.py
   ```

2. **Access the GUI**:
   The GUI will open, allowing you to manage students and courses.

### Using the GUI

- **Adding a Student**:
  1. Enter the student's name in the "Enter Student Name" field.
  2. Enter the student's email in the "Enter Student Email" field.
  3. Click the "Add Student" button to save the student.

- **Viewing Students**:
  - Click the "Show Students" button to display a list of all registered students.

- **Adding a Course**:
  1. Enter the course name in the "Enter Course Name" field.
  2. Enter the course level in the "Enter Course Level" field.
  3. Click the "Add Course" button to save the course.

- **Viewing Courses**:
  - Click the "Show Courses" button to display a list of all available courses.

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file is named `students.db` and is created in the project directory.
- **Migrations**: The application uses Alembic for database migrations. You can create new migration scripts as needed.
- **API Endpoints**: The application exposes RESTful API endpoints for managing students and courses. You can interact with these endpoints using tools like Postman or curl.

## Support

For any issues or questions, please reach out to the development team or check the documentation for further assistance.
```
