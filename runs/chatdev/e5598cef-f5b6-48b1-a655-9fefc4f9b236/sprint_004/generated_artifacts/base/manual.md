Here's the user manual for the software, formatted in Markdown as requested:

```markdown
# Course and Student Management System

A simple GUI application for managing students and courses using FastAPI and SQLite.

## Main Functions

This application allows users to perform the following functions:

- **Create Students**: Add new students by entering their name and email.
- **List Students**: View a list of all registered students.
- **Create Courses**: Add new courses by entering the course name and level.
- **List Courses**: View a list of all available courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

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
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run Database Migration**:
   Ensure that the database schema is updated to include the new Course table.
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

1. **Open the GUI**:
   After starting the application, a GUI window will appear.

2. **Creating a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Create Student" button to add the student.
   - A success message will appear if the student is created successfully.

3. **Listing Students**:
   - Click the "List Students" button to view all registered students.
   - The list will display each student's ID, name, and email.

4. **Creating a Course**:
   - Enter the course name in the "Course Name" field.
   - Enter the course level in the "Course Level" field.
   - Click the "Create Course" button to add the course.
   - A success message will appear if the course is created successfully.

5. **Listing Courses**:
   - Click the "List Courses" button to view all available courses.
   - The list will display each course's ID, name, and level.

## Additional Information

- The application uses SQLite as the database, and all data is stored in `students.db`.
- The application is built using FastAPI, which allows for easy RESTful API development.
- The GUI is created using Tkinter, providing a simple interface for user interaction.

For any issues or further assistance, please contact the support team.
```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, and usage guidelines. Let me know if you need any modifications or additional information!