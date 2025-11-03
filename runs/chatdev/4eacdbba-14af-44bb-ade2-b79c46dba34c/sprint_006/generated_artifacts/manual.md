```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage courses, students, and teachers efficiently. You can create relationships between courses and teachers, enroll students in courses, and retrieve information about all entities.

## Main Functions

- **Create and Manage Courses**: Add new courses and associate them with teachers.
- **Manage Students**: Create student profiles and enroll them in courses.
- **Teacher Management**: Add and retrieve teacher information.
- **Data Persistence**: All data is stored in a SQLite database, ensuring that your information is preserved.

## Quick Install

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
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Migration

Before running the application, you need to set up the database schema. Use Alembic to handle migrations:

1. **Run Migrations**:
   ```bash
   alembic upgrade head
   ```

This command will create the necessary tables in your SQLite database and ensure that existing data is preserved.

## How to Use the Application

1. **Start the Server**:
   Run the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI. Here, you can test the endpoints for creating and retrieving students, courses, and teachers.

### API Endpoints

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of students.

- **Courses**:
  - `POST /courses/`: Create a new course (associate with a teacher).
  - `GET /courses/`: Retrieve a list of courses.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of teachers.

### Example Usage

- **Create a Teacher**:
  ```json
  POST /teachers/
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

- **Create a Course**:
  ```json
  POST /courses/
  {
    "name": "Mathematics 101",
    "level": "Beginner",
    "teacher_id": 1  // ID of the teacher created earlier
  }
  ```

- **Enroll a Student in a Course**:
  ```json
  POST /students/{student_id}/courses/{course_id}
  ```

## Conclusion

The ChatDev Course Management System is designed to streamline the management of educational entities. With its intuitive API and robust database management, you can easily create and manage courses, students, and teachers. For further assistance, please refer to the API documentation or contact support.
```