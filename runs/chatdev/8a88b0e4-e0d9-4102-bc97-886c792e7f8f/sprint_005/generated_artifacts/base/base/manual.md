Here's a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Student Course Management Application

This application allows users to manage student information and course details. It provides functionalities to create and manage students and courses, ensuring a seamless experience for educational institutions.

## Main Functions

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create and manage courses with specific names and levels.
- **Database Management**: The application uses SQLite for data storage, ensuring that existing student data is preserved during schema updates.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   sqlalchemy
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions

1. **Database Initialization**:
   Before using the application, ensure that the database is initialized. You can do this by running the `main.py` script:
   ```bash
   python main.py
   ```
   This will create the necessary tables in the database, including the `students` and `courses` tables.

2. **Creating Students**:
   To create a new student, you can use the `StudentCreate` schema defined in `schemas.py`. Ensure to provide the required fields:
   - `name`: The name of the student (string, required).
   - `email`: The email of the student (string, required).

3. **Creating Courses**:
   To create a new course, use the `CourseCreate` schema. The required fields are:
   - `name`: The name of the course (string, required).
   - `level`: The level of the course (string, required).

4. **Running the Application**:
   The application is designed to be run in a dashboard modality. You can integrate it with a web framework like FastAPI or Flask to create a user interface for managing students and courses.

5. **Database Migration**:
   The application includes a migration script that ensures existing student data is preserved when adding new fields or tables. This is handled in the `main.py` file.

## Additional Resources

For more detailed documentation on SQLAlchemy and Pydantic, please refer to their official documentation:
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

Feel free to reach out for support or further inquiries regarding the application.
```

This manual provides a comprehensive overview of the application, guiding users through the installation and usage process while highlighting the main functionalities.