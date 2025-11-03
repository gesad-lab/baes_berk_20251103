```markdown
# Course Management System

A FastAPI application for managing students, courses, and teachers, allowing for easy enrollment and relationship management.

## Main Functions

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records, including teacher assignments.
- **Teacher Management**: Create and retrieve teacher records.
- **Enrollment**: Enroll students in courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/course-management-system.git
   cd course-management-system
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

The application uses SQLite for database management. On startup, the database will be created automatically if it does not exist. The schema will be updated to include the new relationships as specified in the task.

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API Documentation**:
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Creating Entities**:
   - **Create a Student**:
     - Endpoint: `POST /students/`
     - Body:
       ```json
       {
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```
   - **Create a Teacher**:
     - Endpoint: `POST /teachers/`
     - Body:
       ```json
       {
         "name": "Jane Smith",
         "email": "jane.smith@example.com"
       }
       ```
   - **Create a Course**:
     - Endpoint: `POST /courses/`
     - Body:
       ```json
       {
         "name": "Mathematics 101",
         "level": "Beginner",
         "teacher_id": 1  # Replace with the actual teacher ID
       }
       ```

4. **Retrieving Entities**:
   - **Get Students**:
     - Endpoint: `GET /students/`
   - **Get Teachers**:
     - Endpoint: `GET /teachers/`
   - **Get Courses**:
     - Endpoint: `GET /courses/`

5. **Enroll a Student in a Course**:
   - Endpoint: `POST /students/{student_id}/courses/{course_id}`
   - Example:
     ```bash
     curl -X POST "http://127.0.0.1:8000/students/1/courses/1"
     ```

## Conclusion

This Course Management System provides a robust API for managing educational entities and their relationships. With the ability to create, retrieve, and manage students, teachers, and courses, it serves as a foundational tool for educational institutions.

For further customization or feature requests, please contact the development team.
```