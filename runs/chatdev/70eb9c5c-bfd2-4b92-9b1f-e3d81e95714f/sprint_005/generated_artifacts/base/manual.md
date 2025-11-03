```markdown
# Student-Course Management System

A comprehensive application for managing students and their enrolled courses. This system allows users to create students, create courses, and associate students with multiple courses.

## Main Functions

- **Create Students**: Add new students to the system with their name and email.
- **Create Courses**: Add new courses with a name and level.
- **Enroll Students in Courses**: Associate students with courses, allowing for a many-to-many relationship.
- **Retrieve Students and Courses**: Fetch lists of students and courses from the database.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-course-management.git
   cd student-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy alembic
   ```

4. **Set Up the Database**:
   The application uses SQLite for simplicity. The database will be created automatically when you run the application.

## How to Use

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Create a Student**:
   Use the `/students/` endpoint to create a new student by sending a POST request with the following JSON body:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

4. **Create a Course**:
   Use the `/courses/` endpoint to create a new course by sending a POST request with the following JSON body:
   ```json
   {
       "name": "Mathematics",
       "level": "Beginner"
   }
   ```

5. **Enroll a Student in a Course**:
   Use the `/students/{student_id}/courses/` endpoint to enroll a student in a course by sending a POST request with the following JSON body:
   ```json
   {
       "name": "Mathematics",
       "level": "Beginner"
   }
   ```
   Replace `{student_id}` with the actual ID of the student you want to enroll.

6. **Retrieve Students and Courses**:
   Use the `/students/` and `/courses/` endpoints to get lists of students and courses, respectively.

## Database Migration

The application uses Alembic for database migrations. To apply migrations, run the following command:
```bash
alembic upgrade head
```

This command will ensure that the database schema is up to date with the latest changes, preserving existing data.

## Conclusion

This Student-Course Management System provides a robust framework for managing students and their courses. With easy-to-use API endpoints and a simple installation process, you can quickly get started with managing educational data.
```
