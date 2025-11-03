```markdown
# Student Course Management System

A simple application for managing students and their course enrollments using FastAPI and Tkinter.

## Main Functions

- **Student Registration**: Allows users to register new students with their names, emails, and associated course IDs.
- **Course Creation**: Enables users to create new courses with specified names and levels.
- **Course Enrollment**: Students can be enrolled in multiple courses, establishing a many-to-many relationship between students and courses.

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

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests tkinter
   ```

4. **Initialize the Database**:
   Ensure that the database is set up correctly by running the application, which will automatically create the necessary tables.
   ```bash
   python main.py
   ```

## How to Use the Application

### Starting the Application

1. Run the application:
   ```bash
   python main.py
   ```

2. The FastAPI server will start at `http://127.0.0.1:8000`, and the Tkinter GUI will open for user interaction.

### Registering a Student

1. In the GUI, enter the student's name and email.
2. Enter the course IDs (comma-separated) that the student will be enrolled in.
3. Click the "Submit Student" button.
4. If successful, a message box will confirm the registration. If there are errors (e.g., invalid email format), appropriate warnings will be displayed.

### Creating a Course

1. In the GUI, enter the course name and level.
2. Click the "Submit Course" button.
3. A confirmation message will appear if the course is created successfully.

### Viewing Students and Courses

- Currently, the application does not provide a direct way to view registered students or courses through the GUI. However, you can use the FastAPI endpoints to retrieve this information:
  - **Get All Students**: `GET http://127.0.0.1:8000/students/`
  - **Get All Courses**: `GET http://127.0.0.1:8000/courses/`

## Database Migration

The application uses Alembic for database migrations. The migration scripts are located in the `xxxx_add_courses_table.py` file. To apply migrations, ensure that the application is running, and the database will be updated automatically on startup.

## Troubleshooting

- If you encounter issues with the Tkinter GUI not displaying, ensure that the Tkinter library is installed correctly.
- For any errors related to database connections, check the `DATABASE_URL` in `database.py` and ensure that the SQLite database file is accessible.

## Conclusion

This application provides a straightforward way to manage students and their course enrollments. Feel free to extend its functionality or integrate it with other systems as needed.
```