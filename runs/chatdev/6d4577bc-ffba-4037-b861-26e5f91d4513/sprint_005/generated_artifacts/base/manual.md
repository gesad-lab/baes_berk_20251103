```markdown
# ChatDev Student-Course Management System

Welcome to the ChatDev Student-Course Management System! This software allows you to manage students and their course enrollments effectively. Below is a detailed user manual that covers the main functions of the software, how to install the necessary environment dependencies, and how to use the application.

## Main Functions

The Student-Course Management System provides the following functionalities:

1. **Student Management**:
   - Create new students with their names and email addresses.
   - Retrieve a list of all students.

2. **Course Management**:
   - Create new courses with their names and levels.
   - Retrieve a list of all courses.

3. **Enrollment Management**:
   - Enroll students in courses, allowing students to have multiple courses.

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
   pip install fastapi sqlalchemy pydantic
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

Once the application is running, you can interact with it using HTTP requests. Below are examples of how to use the main endpoints.

### 1. Create a New Student

**Endpoint**: `POST /students/`

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### 2. Retrieve All Students

**Endpoint**: `GET /students/`

**Response**:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "courses": []
  }
]
```

### 3. Create a New Course

**Endpoint**: `POST /courses/`

**Request Body**:
```json
{
  "name": "Mathematics",
  "level": "Beginner"
}
```

### 4. Retrieve All Courses

**Endpoint**: `GET /courses/`

**Response**:
```json
[
  {
    "id": 1,
    "name": "Mathematics",
    "level": "Beginner"
  }
]
```

### 5. Enroll a Student in a Course

**Endpoint**: `POST /students/{student_id}/courses/{course_id}`

**Example Request**:
```bash
POST /students/1/courses/1
```

**Response**:
```json
{
  "message": "Student enrolled in course successfully"
}
```

## Conclusion

The ChatDev Student-Course Management System is designed to streamline the management of students and their course enrollments. By following the instructions in this manual, you can set up the application and start managing your students and courses effectively. For any further assistance, please reach out to our support team.

Happy managing!
```