```markdown
# ChatDev Course Management System

A comprehensive application for managing students, courses, and teachers, allowing for easy creation, listing, and enrollment functionalities.

## Main Functions

1. **Student Management**
   - Create new students.
   - List all existing students.

2. **Course Management**
   - Create new courses with an associated teacher.
   - List all existing courses.

3. **Teacher Management**
   - Create new teachers.
   - List all existing teachers.

4. **Enrollment Management**
   - Enroll students in courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment (Optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Use the following command to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the FastAPI Application**
   Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Access the GUI**
   Open the `gui.py` file and run it:
   ```bash
   python gui.py
   ```
   This will launch a Tkinter GUI for interacting with the backend.

3. **Using the GUI**
   - **Creating Students**
     - Enter the student's name and email, then click "Create Student".
     - The student will be added to the database.
   - **Listing Students**
     - Click "List Students" to view all existing students.
   - **Creating Courses**
     - Enter the course name, level, and teacher ID, then click "Create Course".
   - **Listing Courses**
     - Click "List Courses" to view all existing courses.
   - **Creating Teachers**
     - Enter the teacher's name and email, then click "Create Teacher".
   - **Listing Teachers**
     - Click "List Teachers" to view all existing teachers.
   - **Enrolling Students**
     - Enter the student ID and course ID, then click "Enroll Student in Course" to enroll the student in the specified course.

## Database Migration

The application uses Alembic for database migrations. The migration script `migration_script.py` adds a new `teachers` table and a `teacher_id` column to the `courses` table while preserving existing data.

To apply the migration, run:
```bash
alembic upgrade head
```

## API Documentation

The application exposes a RESTful API. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Conclusion

This application provides a robust framework for managing educational entities, allowing for seamless interaction between students, courses, and teachers. For any issues or feature requests, please contact the development team.
```