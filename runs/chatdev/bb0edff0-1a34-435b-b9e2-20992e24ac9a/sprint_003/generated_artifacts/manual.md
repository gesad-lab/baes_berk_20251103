Here's the `manual.md` file for the software, detailing its main functions, installation instructions, and usage guidelines.

```markdown
# Student Management Application

A simple application for managing students and courses, built with FastAPI and a Tkinter GUI.

## Main Functions

The Student Management Application provides the following functionalities:

- **Add Students**: Users can add new students by providing their name and email.
- **List Students**: Users can view a list of all registered students.
- **Add Courses**: Users can create new courses by specifying the course name and level.
- **List Courses**: Users can view a list of all available courses.

## Quick Install

To set up the environment and run the application, follow these steps:

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

3. **Install Dependencies**:
   Make sure you have `pip` installed, then run:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

4. **Run the Application**:
   Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. **Open the GUI**:
   Run the GUI application:
   ```bash
   python main.py
   ```

## How to Use the Application

### Adding a Student

1. Open the application.
2. Enter the student's name in the "Enter Student Name" field.
3. Enter the student's email in the "Enter Student Email" field.
4. Click the "Add Student" button to save the student.

### Listing Students

1. Click the "List Students" button to view all registered students.
2. A pop-up will display the list of students with their IDs, names, and emails.

### Adding a Course

1. Enter the course name in the "Enter Course Name" field.
2. Enter the course level in the "Enter Course Level" field.
3. Click the "Add Course" button to save the course.

### Listing Courses

1. Click the "List Courses" button to view all available courses.
2. A pop-up will display the list of courses with their IDs, names, and levels.

## Additional Information

- The application uses SQLite as its database, and the database schema is automatically created when the application starts.
- Existing student data will be preserved during any database migrations.

For further assistance or feature requests, please contact the development team.

```

This manual provides a comprehensive overview of the software, ensuring users can easily install and utilize the application effectively.