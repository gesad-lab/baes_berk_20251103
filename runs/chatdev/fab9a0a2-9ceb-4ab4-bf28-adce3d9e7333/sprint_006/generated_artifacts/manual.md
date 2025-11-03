```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. You can create and manage relationships between these entities, making it easier to organize educational content.

## Main Functions

- **Student Management**: Create, read, and enroll students in courses.
- **Course Management**: Create and read courses, including assigning teachers to courses.
- **Teacher Management**: Create and read teacher profiles.
- **Enrollment**: Enroll students in courses and manage their course registrations.

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

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

Before running the application, you need to initialize the database:

1. **Run Database Migration**:
   ```bash
   alembic upgrade head
   ```

This command will set up the database schema, including the new relationships between courses and teachers while preserving existing data.

## How to Use the Application

### Start the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

The application exposes several API endpoints for managing students, courses, and teachers. Below are the key endpoints:

#### Student Endpoints

- **Create Student**: `POST /students/`
  - Request Body: `{ "name": "John Doe", "email": "john@example.com" }`
  
- **Get Student**: `GET /students/{student_id}`

#### Course Endpoints

- **Create Course**: `POST /courses/`
  - Request Body: `{ "name": "Mathematics", "level": "Beginner", "teacher_id": 1 }`
  
- **Get Course**: `GET /courses/{course_id}`

#### Teacher Endpoints

- **Create Teacher**: `POST /teachers/`
  - Request Body: `{ "name": "Jane Smith", "email": "jane@example.com" }`
  
- **Get Teacher**: `GET /teachers/{teacher_id}`

#### Enrollment

- **Enroll Student in Course**: `POST /students/{student_id}/enroll/{course_id}`

### Example Usage

1. **Create a Teacher**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "Jane Smith", "email": "jane@example.com"}'
   ```

2. **Create a Course**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner", "teacher_id": 1}'
   ```

3. **Enroll a Student**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/students/1/enroll/1"
   ```

## Documentation

For more detailed documentation, including examples and API reference, please refer to the [FastAPI Documentation](https://fastapi.tiangolo.com/).

## Support

If you encounter any issues or have questions, please reach out to our support team at support@chatdev.com.

Thank you for using the ChatDev Course Management System!
```