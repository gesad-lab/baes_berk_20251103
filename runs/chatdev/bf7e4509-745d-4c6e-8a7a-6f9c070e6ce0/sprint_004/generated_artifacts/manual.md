```markdown
# Student and Course Management System

A comprehensive application for managing students and their course enrollments.

## Main Functions

The Student and Course Management System provides the following functionalities:

- **Student Management**: Create, retrieve, and manage student records.
- **Course Management**: Create, retrieve, and manage course records.
- **Enrollment**: Enroll students in courses and manage their course relationships.
- **Data Persistence**: All data is stored in a SQLite database, ensuring data integrity and persistence.

## Quick Install

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

3. **Install Required Dependencies**:
   ```bash
   pip install fastapi sqlalchemy alembic pydantic
   ```

4. **Run Database Migration**:
   Ensure that the database schema is up to date by running the migration script:
   ```bash
   alembic upgrade head
   ```

5. **Start the API Server**:
   Run the FastAPI application:
   ```bash
   uvicorn api:app --reload
   ```

6. **Launch the GUI**:
   Open another terminal and run:
   ```bash
   python main.py
   ```

## How to Use the Application

### API Endpoints

The application exposes several API endpoints for managing students and courses:

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "course_ids": [1, 2]  // Optional: List of course IDs to enroll in
    }
    ```

- **Get All Students**:
  - **Endpoint**: `GET /students/`

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get All Courses**:
  - **Endpoint**: `GET /courses/`

- **Enroll a Student in a Course**:
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}/enroll`

### GUI Usage

1. **Launch the Application**: After starting the GUI, you will see the main window.
2. **Add Students**: Fill in the student details and click "Add Student" to create a new student record.
3. **Add Courses**: Fill in the course details and click "Add Course" to create a new course record.
4. **Enroll Students**: Select a student and a course from the dropdowns and click "Enroll" to enroll the student in the selected course.

## Conclusion

The Student and Course Management System is designed to simplify the management of students and their course enrollments. With a user-friendly GUI and a robust API, it provides an efficient way to handle educational data.

For further assistance or to report issues, please contact our support team.
```