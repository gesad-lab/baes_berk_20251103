```markdown
# ChatDev Course Management System

## Introduction

The ChatDev Course Management System is designed to facilitate the management of courses, students, and teachers within an educational environment. This software allows users to create and manage courses, associate them with teachers, and enroll students in courses. The system is built using FastAPI and SQLAlchemy, ensuring a robust and scalable solution.

## Main Functions

- **Create Courses**: Users can create new courses by providing necessary details such as course name, level, and associated teacher.
- **Manage Teachers**: Users can add teachers to the system, ensuring that each course can have a designated instructor.
- **Enroll Students**: Students can be enrolled in multiple courses, allowing for flexible learning paths.
- **Data Persistence**: The system uses SQLite for data storage, ensuring that all information is preserved across sessions.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the FastAPI application, execute the following command in your terminal:

```bash
uvicorn main:app --reload
```

This command will start the server, and you can access the API documentation at `http://127.0.0.1:8000/docs`.

## Using the Application

### Creating a Teacher

To create a new teacher, send a POST request to `/teachers` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Creating a Course

To create a new course, send a POST request to `/courses` with the following JSON body:

```json
{
  "name": "Mathematics 101",
  "level": "Beginner",
  "teacher_id": 1  // ID of the teacher associated with this course
}
```

### Enrolling a Student in a Course

To enroll a student in a course, send a POST request to `/students/{student_id}/courses/{course_id}`.

### Viewing Courses and Teachers

You can retrieve all courses and teachers by sending a GET request to `/courses` and `/teachers`, respectively.

## Database Migration

The application includes a migration script that creates the necessary tables for students, courses, and teachers while preserving existing data. To run the migration, execute the following command:

```bash
python main.py
```

This will create the tables in the SQLite database specified in `database.py`.

## Conclusion

The ChatDev Course Management System provides a comprehensive solution for managing educational courses, teachers, and students. With its easy-to-use API and robust backend, it is well-suited for educational institutions looking to streamline their course management processes.

For further assistance, please refer to the API documentation or contact our support team.
```