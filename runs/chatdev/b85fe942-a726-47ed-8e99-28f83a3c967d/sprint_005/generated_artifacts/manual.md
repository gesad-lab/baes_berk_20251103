```markdown
# Teacher Management System

A comprehensive application for managing students, courses, and teachers. This system allows users to register students, create courses, and register teachers seamlessly through a graphical user interface (GUI) and a RESTful API.

## Main Functions

- **Student Registration**: Allows users to register students with their names, emails, and associated course IDs.
- **Course Creation**: Enables users to create courses by specifying the course name and level.
- **Teacher Registration**: Facilitates the registration of teachers with their names and emails.
- **Database Management**: Utilizes SQLAlchemy for ORM and Alembic for database migrations, ensuring data integrity and schema evolution.

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

3. **Install Required Packages**:
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

2. The FastAPI server will start on `http://127.0.0.1:8000`, and the Tkinter GUI will open for user interaction.

### Using the GUI

- **Registering a Student**:
  - Enter the student's name and email.
  - Input the course IDs (comma-separated) that the student will be enrolled in.
  - Click on "Submit Student" to register the student.

- **Creating a Course**:
  - Enter the course name and level.
  - Click on "Submit Course" to create the course.

- **Registering a Teacher**:
  - Enter the teacher's name and email.
  - Click on "Submit Teacher" to register the teacher.

### API Endpoints

You can also interact with the application through the API. Here are the available endpoints:

- **Create Student**:
  - `POST /students/`
  - Request Body: 
    ```json
    {
      "name": "Student Name",
      "email": "student@example.com",
      "course_ids": [1, 2]
    }
    ```

- **Create Course**:
  - `POST /courses/`
  - Request Body:
    ```json
    {
      "name": "Course Name",
      "level": "Beginner"
    }
    ```

- **Create Teacher**:
  - `POST /teachers/`
  - Request Body:
    ```json
    {
      "name": "Teacher Name",
      "email": "teacher@example.com"
    }
    ```

## Database Migration

The application uses Alembic for managing database migrations. To apply migrations, ensure that the application is running, and it will automatically create the necessary tables, including the new `teachers` table, while preserving existing data for students and courses.

## Conclusion

This Teacher Management System provides a robust solution for managing educational entities. With its user-friendly interface and powerful backend, it simplifies the process of student, course, and teacher management. For further assistance, please refer to the documentation or contact support.
```