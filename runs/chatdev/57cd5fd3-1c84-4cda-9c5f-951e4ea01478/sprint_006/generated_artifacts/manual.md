```markdown
# Student Course Management System

A comprehensive application for managing students, courses, and teachers. This system allows users to create and manage relationships between students, courses, and teachers effectively.

## Main Functions

- **Student Management**: Create, retrieve, and manage student records.
- **Course Management**: Create, retrieve, and manage course records, including associating courses with teachers.
- **Teacher Management**: Create and manage teacher records.
- **Enrollment**: Enroll students in courses and manage their course registrations.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-course-management.git
   cd student-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Use pip to install the required packages:
   ```bash
   pip install fastapi sqlalchemy alembic pydantic
   ```

4. **Database Setup**:
   The application uses SQLite for the database. The database will be initialized automatically when the application starts.

## Usage

1. **Run the Application**:
   Start the FastAPI application by running:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

2. **API Endpoints**:
   The following API endpoints are available:

   - **Students**:
     - `POST /students/`: Create a new student.
     - `GET /students/`: Retrieve a list of students.

   - **Courses**:
     - `POST /courses/`: Create a new course (optionally assign a teacher).
   
   - **Teachers**:
     - `POST /teachers/`: Create a new teacher.

   - **Enrollment**:
     - `POST /students/{student_id}/courses/{course_id}/`: Enroll a student in a course.

3. **Testing the API**:
   You can use tools like Postman or cURL to test the API endpoints. For example, to create a new student, send a POST request to `http://127.0.0.1:8000/students/` with the following JSON body:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

## Database Migration

To apply database migrations, use Alembic. Run the following command to upgrade the database schema:
```bash
alembic upgrade head
```

This command will create the necessary tables and relationships in the database while preserving existing data.

## Conclusion

This Student Course Management System provides a robust framework for managing educational entities. By following the installation and usage instructions, you can set up and run the application efficiently. For further customization and development, refer to the codebase and documentation provided within the repository.
```