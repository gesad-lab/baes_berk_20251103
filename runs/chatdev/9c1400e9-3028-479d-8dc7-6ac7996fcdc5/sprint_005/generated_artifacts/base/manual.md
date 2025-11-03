```markdown
# ChatDev Student and Course Management System

Welcome to the ChatDev Student and Course Management System! This software allows users to manage student and course registrations efficiently. Below, you will find a detailed user manual that covers the main functions of the software, installation instructions, and usage guidelines.

## Main Functions

- **Student Registration**: Add new students to the system with their names and email addresses.
- **Course Registration**: Add new courses with their names and levels.
- **Student-Course Relationship**: Students can be associated with multiple courses, allowing for a many-to-many relationship.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-student-course-management.git
   cd chatdev-student-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## Usage Instructions

### Accessing the GUI

1. Once the application is running, open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the API documentation.
2. Alternatively, you can run the GUI application using Tkinter by executing the following command:
   ```bash
   python gui.py
   ```

### Registering a Student

1. In the GUI, enter the student's name and email address in the respective fields.
2. Click on the "Submit Student" button.
3. If successful, a message will display confirming the addition of the student.

### Registering a Course

1. Enter the course name and level in the respective fields.
2. Click on the "Submit Course" button.
3. A confirmation message will appear if the course is added successfully.

### Associating Students with Courses

- The system allows for students to be associated with multiple courses. This relationship is managed through the backend and can be extended in future versions.

## Database Migration

The application uses Alembic for database migrations. To apply the latest migrations, run the following command:
```bash
alembic upgrade head
```

This command will ensure that the database schema is up-to-date and that existing data is preserved.

## Additional Resources

For more detailed documentation on FastAPI, SQLAlchemy, and Alembic, please refer to the following links:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)

## Support

If you encounter any issues or have questions, please reach out to our support team at support@chatdev.com.

Thank you for using the ChatDev Student and Course Management System!
```