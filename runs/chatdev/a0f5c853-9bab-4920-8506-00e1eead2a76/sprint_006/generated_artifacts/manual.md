```markdown
# Student Management System

A comprehensive application for managing students, courses, and teachers. This system allows users to create, read, and manage relationships between students, courses, and teachers efficiently.

## Main Functions

- **Student Management**: Add, view, and manage student information.
- **Course Management**: Create and manage courses, including associating them with teachers.
- **Teacher Management**: Add and manage teacher information.
- **Enrollment**: Enroll students in courses and manage their course registrations.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-management-system.git
   cd student-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy alembic requests
   ```

4. **Run Database Migrations**:
   Ensure you have an `alembic.ini` file configured correctly, then run:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the application using:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

1. **Launch the GUI**:
   After starting the application, the GUI will open. You can interact with the system through this interface.

2. **Adding Students**:
   - Enter the student's name and email in the respective fields.
   - Click on the "Add Student" button to save the student information.

3. **Adding Courses**:
   - Enter the course name, level, and the teacher's ID in the respective fields.
   - Click on the "Add Course" button to save the course information.

4. **Adding Teachers**:
   - Enter the teacher's name and email in the respective fields.
   - Click on the "Add Teacher" button to save the teacher information.

5. **Viewing Students**:
   - Click on the "Show Students" button to display a list of all registered students.

6. **Enroll Students in Courses**:
   - To enroll a student in a course, you can use the enrollment functionality (not explicitly shown in the GUI but can be implemented as needed).

## Additional Information

- **Database**: The application uses SQLite for data storage, and the database schema is managed using Alembic for migrations.
- **API Endpoints**: The application exposes RESTful API endpoints for managing students, courses, and teachers. You can interact with these endpoints using tools like Postman or directly through the GUI.

For more detailed documentation, please refer to the code comments and the FastAPI documentation at [FastAPI Documentation](https://fastapi.tiangolo.com/).

## Support

If you encounter any issues or have questions, please reach out to our support team at support@yourcompany.com.
```
