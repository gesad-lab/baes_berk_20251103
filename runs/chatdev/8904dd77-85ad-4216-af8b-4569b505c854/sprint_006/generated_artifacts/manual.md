```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. You can create, read, and enroll students in courses, as well as assign teachers to courses.

## Main Functions

### 1. Student Management
- **Create Student**: Add a new student with a name and email.
- **Read Students**: Retrieve a list of students with pagination.

### 2. Course Management
- **Create Course**: Add a new course with a name, level, and assigned teacher.
- **Read Courses**: Retrieve a list of courses with pagination.

### 3. Teacher Management
- **Create Teacher**: Add a new teacher with a name and email.
- **Read Teachers**: Retrieve a list of teachers with pagination.

### 4. Enrollment
- **Enroll Student in Course**: Enroll a student in a specific course.
- **Get Student Courses**: Retrieve all courses a student is enrolled in.

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
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the FastAPI application, use the following command:
```bash
uvicorn main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

## Using the API

You can interact with the API using tools like Postman or cURL. Below are some example requests:

### Create a Student
```http
POST /students/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Create a Course
```http
POST /courses/
Content-Type: application/json

{
  "name": "Mathematics 101",
  "level": "Beginner",
  "teacher_id": 1
}
```

### Create a Teacher
```http
POST /teachers/
Content-Type: application/json

{
  "name": "Jane Smith",
  "email": "jane.smith@example.com"
}
```

### Enroll a Student in a Course
```http
POST /students/1/courses/1
```

### Get Student Courses
```http
GET /students/1/courses
```

## Database Migration

To apply database migrations, ensure you have Alembic installed and run:
```bash
alembic upgrade head
```
This will create the necessary tables and relationships in your database.

## Conclusion

This Course Management System provides a robust framework for managing educational entities. Feel free to explore the API and customize it to fit your needs. For further assistance, please refer to the documentation or reach out to our support team.
```