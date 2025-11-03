Here's the user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management System

A simple application for managing students and courses, allowing users to add and view student and course information.

## Main Functions

- **Add Student**: Allows users to input student details (name and email) and store them in the database.
- **View Students**: Displays a list of all students currently stored in the database.
- **Add Course**: Enables users to input course details (name and level) and store them in the database.
- **View Courses**: Displays a list of all courses currently stored in the database.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Make sure to include the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   pydantic
   requests
   tkinter
   ```

4. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

1. **Launch the Application**:
   After running the application, a GUI window will open.

2. **Adding a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to save the student information.

3. **Viewing Students**:
   - Click the "View Students" button to retrieve and display a list of all students.

4. **Adding a Course**:
   - Enter the course name in the "Enter Course Name" field.
   - Enter the course level in the "Enter Course Level" field.
   - Click the "Add Course" button to save the course information.

5. **Viewing Courses**:
   - Click the "View Courses" button to retrieve and display a list of all courses.

## Additional Information

- The application uses SQLite as the database to store student and course information.
- The database schema is designed to preserve existing student data while allowing for the addition of new courses.
- Ensure that the FastAPI server is running before using the GUI to interact with the application.

For any issues or further assistance, please reach out to the support team.
```

This manual provides a comprehensive overview of the software, its installation process, and usage instructions, ensuring that users can effectively utilize the Course Management System.