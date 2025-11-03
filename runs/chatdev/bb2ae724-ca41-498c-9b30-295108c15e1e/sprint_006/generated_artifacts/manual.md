```markdown
# ChatDev Course Management System

A comprehensive application for managing students, courses, and teachers, allowing for easy enrollment and assignment of teachers to courses.

## Main Functions

- **Student Management**: Create and manage student records.
- **Course Management**: Create and manage courses, including assigning teachers.
- **Teacher Management**: Create and manage teacher records.
- **Enrollment**: Enroll students in courses.
- **Teacher Assignment**: Assign teachers to specific courses.

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Migration

Before running the application, ensure the database schema is set up correctly. Run the following command to apply the migrations:
```bash
alembic upgrade head
```

## How to Use the Application

1. **Start the API Server**:
   Run the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

2. **Access the GUI**:
   The application includes a simple GUI built with Tkinter. To run the GUI, execute the following command:
   ```bash
   python gui.py
   ```

3. **Using the GUI**:
   - **Create Student**: Enter the student's name and email, then click "Create Student".
   - **Create Course**: Enter the course name and level, then click "Create Course".
   - **Enroll in Course**: Enter the student ID and course details, then click "Enroll in Course".
   - **Create Teacher**: Enter the teacher's name and email, then click "Create Teacher".
   - **Assign Teacher to Course**: Enter the course ID and teacher ID, then click "Assign Teacher to Course".

4. **API Endpoints**:
   You can also interact with the API directly using tools like Postman or cURL. Here are some key endpoints:
   - **Create Student**: `POST /students/`
   - **Create Course**: `POST /courses/`
   - **Enroll Student in Course**: `POST /students/{student_id}/courses/`
   - **Create Teacher**: `POST /teachers/`
   - **Assign Teacher to Course**: `PUT /courses/{course_id}/assign_teacher/{teacher_id}`

## Documentation

For more detailed documentation, including API reference and examples, please refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).

## Support

If you encounter any issues or have questions, please reach out to our support team at support@chatdev.com.

Happy coding!
```