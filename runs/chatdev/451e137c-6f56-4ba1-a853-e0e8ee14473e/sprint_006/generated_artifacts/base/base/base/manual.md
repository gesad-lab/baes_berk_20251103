Here's the detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student and Course Management Application

A simple application for managing students and courses using a web-based interface. This application allows users to add students and courses, as well as retrieve lists of existing students and courses.

## Main Functions

- **Add Student**: Users can input a student's name and email to add them to the database.
- **Add Course**: Users can input a course name and level to create a new course entity.
- **Display Students**: Users can view a list of all students currently stored in the database.
- **Display Courses**: Users can view a list of all courses currently stored in the database.

## Quick Install

To set up the environment and run the application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Install Dependencies**:
   Make sure you have Python installed (version 3.7 or higher). Then, install the required dependencies using pip:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

3. **Run the Application**:
   Start the FastAPI server by running:
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000` to access the application.

## How to Use the Application

1. **Adding a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to submit the information.

2. **Adding a Course**:
   - Enter the course name in the "Enter Course Name" field.
   - Enter the course level in the "Enter Course Level" field.
   - Click the "Add Course" button to submit the information.

3. **Displaying Students**:
   - Click the "Display Students" button to retrieve and display a list of all students in the application.

4. **Displaying Courses**:
   - Click the "Display Courses" button to retrieve and display a list of all courses in the application.

## Database Migration

The application includes a migration script to create the Course table while preserving existing Student data. The migration can be executed using the following command:
```bash
python migration.py
```

## Troubleshooting

- If you encounter an error related to the tkinter module, ensure that it is installed. You can install it using:
  ```bash
  pip install tk
  ```

- If the application does not run, check that all dependencies are correctly installed and that the FastAPI server is running.

## Additional Resources

For more information about FastAPI and SQLAlchemy, you can refer to their official documentation:
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and troubleshooting tips. Let me know if you need any further modifications or additional information!