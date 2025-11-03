```markdown
# Course Management Application

A comprehensive application for managing students, courses, and teachers, allowing for seamless enrollment and course assignment.

## Main Functions

The Course Management Application provides the following key functionalities:

- **Student Management**: Create, retrieve, and manage student records.
- **Course Management**: Create, retrieve, and manage course records.
- **Teacher Management**: Create, retrieve, and manage teacher records.
- **Enrollment**: Enroll students into courses.
- **Teacher Assignment**: Assign teachers to specific courses.

## Installation

To set up the Course Management Application, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

Navigate to the project directory and install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 3: Set Up the Database

The application uses SQLite for database management. The database will be automatically created when you run the application for the first time.

### Step 4: Run the Application

You can start the application by executing the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI application, and you can access it at `http://127.0.0.1:8000`.

## How to Use the Application

### API Endpoints

The application exposes several API endpoints for managing students, courses, and teachers. Below are the key endpoints:

#### Student Endpoints

- **Create Student**: `POST /students/`
  - Request Body: `{ "name": "Student Name", "email": "student@example.com" }`
  
- **Get All Students**: `GET /students/`

#### Course Endpoints

- **Create Course**: `POST /courses/`
  - Request Body: `{ "name": "Course Name", "level": "Course Level" }`
  
- **Get All Courses**: `GET /courses/`

- **Assign Teacher to Course**: `POST /courses/{course_id}/assign_teacher/{teacher_id}`
  - Replace `{course_id}` and `{teacher_id}` with the respective IDs.

#### Teacher Endpoints

- **Create Teacher**: `POST /teachers/`
  - Request Body: `{ "name": "Teacher Name", "email": "teacher@example.com" }`
  
- **Get All Teachers**: `GET /teachers/`

#### Enrollment Endpoints

- **Enroll Student in Course**: `POST /students/{student_id}/courses/{course_id}`
  - Replace `{student_id}` and `{course_id}` with the respective IDs.

### Example Usage

1. **Create a Teacher**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
   ```

2. **Create a Course**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner"}'
   ```

3. **Assign Teacher to Course**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/courses/1/assign_teacher/1"
   ```

4. **Enroll a Student in a Course**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/students/1/courses/1"
   ```

## Conclusion

This Course Management Application provides a robust framework for managing educational entities. By following the installation and usage instructions, you can effectively manage students, courses, and teachers within your organization.

For further documentation and examples, please refer to the FastAPI documentation at [fastapi.tiangolo.com](https://fastapi.tiangolo.com).
```