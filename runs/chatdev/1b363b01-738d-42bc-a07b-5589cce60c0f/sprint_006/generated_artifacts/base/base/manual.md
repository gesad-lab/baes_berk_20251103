```markdown
# ChatDev Student Course Management System

Welcome to the ChatDev Student Course Management System! This software allows you to manage students and their course enrollments effectively. Below is a detailed user manual that covers the main functions of the software, how to install the necessary environment dependencies, and how to use the application.

## Main Functions

The ChatDev application provides the following key functionalities:

1. **Student Management**:
   - Create new students with their names and email addresses.
   - Retrieve a list of all students.

2. **Course Management**:
   - Create new courses with their names and levels.
   - Retrieve a list of all courses.

3. **Enrollment Management**:
   - Enroll students in courses, establishing a many-to-many relationship between students and courses.

## Installation of Environment Dependencies

To run the ChatDev application, you need to install the required dependencies. Follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev.git
   cd chatdev
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
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Database Setup**:
   The application uses SQLite for database management. The database will be created automatically when you start the application for the first time.

2. **Start the Application**:
   Run the following command to start the FastAPI application:
   ```bash
   python main.py
   ```

3. **Access the API**:
   Once the application is running, you can access the API at `http://127.0.0.1:8000`. You can also access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Using the Application

### Creating a Student
To create a new student, send a POST request to `/students` with the following JSON body:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Retrieving Students
To retrieve a list of students, send a GET request to `/students`.

### Creating a Course
To create a new course, send a POST request to `/courses` with the following JSON body:
```json
{
  "name": "Mathematics",
  "level": "Beginner"
}
```

### Retrieving Courses
To retrieve a list of courses, send a GET request to `/courses`.

### Enrolling a Student in a Course
To enroll a student in a course, send a POST request to `/students/{student_id}/courses/{course_id}`. Replace `{student_id}` and `{course_id}` with the respective IDs of the student and course.

Example:
```bash
POST /students/1/courses/2
```

## Conclusion

The ChatDev Student Course Management System provides a robust solution for managing students and their course enrollments. By following the instructions in this manual, you can easily set up and use the application. For further assistance or feature requests, please contact our support team.

Happy Learning!
```