```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. You can create, read, and enroll students in courses while establishing relationships between courses and teachers.

## Main Functions

- **Student Management**: Create and manage student profiles.
- **Course Management**: Create and manage courses, including associating them with teachers.
- **Teacher Management**: Create and manage teacher profiles.
- **Enrollment**: Enroll students in courses and manage their course selections.

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
   ```bash
   pip install fastapi sqlalchemy pydantic
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Software

### API Endpoints

The application exposes several API endpoints to interact with the system. Below are the main endpoints you can use:

#### Student Endpoints

- **Create a Student**:
  - **POST** `/students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get a Student**:
  - **GET** `/students/{student_id}`

#### Course Endpoints

- **Create a Course**:
  - **POST** `/courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner",
      "teacher_id": 1  // ID of the teacher associated with the course
    }
    ```

- **Get a Course**:
  - **GET** `/courses/{course_id}`

#### Teacher Endpoints

- **Create a Teacher**:
  - **POST** `/teachers/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```

- **Get a Teacher**:
  - **GET** `/teachers/{teacher_id}`

#### Enrollment

- **Enroll a Student in a Course**:
  - **POST** `/students/{student_id}/courses/{course_id}`

### Database Migration

The application includes a migration script that ensures the database schema is updated to support the new teacher relationship in the Course entity. To run the migration, execute the following command:

```bash
python main.py
```

This will create the necessary tables and columns while preserving existing data for students, courses, and teachers.

## Conclusion

This Course Management System is designed to streamline the management of educational entities. For further assistance or to report issues, please contact our support team.

Happy coding!
```