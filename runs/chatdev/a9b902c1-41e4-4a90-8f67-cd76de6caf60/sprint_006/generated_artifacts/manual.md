```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System, a powerful application designed to manage students, courses, and teachers efficiently. This software allows you to create and manage relationships between students, courses, and teachers seamlessly.

## Main Functions

- **Student Management**: Create and manage student profiles, including their associated courses.
- **Course Management**: Create and manage courses, including assigning teachers to each course.
- **Teacher Management**: Create and manage teacher profiles, allowing them to be associated with courses.

## Quick Install

To get started with the ChatDev Course Management System, you'll need to install the necessary environment dependencies. Follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

### Running the Application

1. **Start the FastAPI Server**:
   ```bash
   uvicorn main:app --reload
   ```

   This command will start the FastAPI server, and you can access the application at `http://127.0.0.1:8000`.

### Using the GUI

1. **Launch the GUI**:
   Run the following command in your terminal:
   ```bash
   python gui.py
   ```

2. **Registering Students**:
   - Enter the student's name and email.
   - Provide the course IDs (comma-separated) that the student will be enrolled in.
   - Click on "Create Student" to register the student.

3. **Registering Courses**:
   - Enter the course name and level.
   - Provide the teacher ID to associate a teacher with the course.
   - Click on "Create Course" to register the course.

4. **Registering Teachers**:
   - Enter the teacher's name and email.
   - Click on "Create Teacher" to register the teacher.

### Database Migration

The application includes a migration script to ensure that existing data is preserved while adding new relationships. To apply the migration, run the following command:

```bash
alembic upgrade head
```

This command will update the database schema to include the new relationship between courses and teachers while preserving existing student, course, and teacher data.

## Conclusion

The ChatDev Course Management System is designed to streamline the management of educational entities. With its intuitive GUI and robust backend, you can easily manage students, courses, and teachers. For more detailed documentation and examples, please refer to the code comments and the FastAPI documentation.

Happy coding!
```