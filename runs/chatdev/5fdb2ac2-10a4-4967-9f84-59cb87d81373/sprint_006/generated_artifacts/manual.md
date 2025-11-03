```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers seamlessly. You can create, retrieve, and associate students with courses and teachers, making it an efficient tool for educational institutions.

## Main Functions

- **Student Management**: Create and manage student records, including their names, emails, and associated courses.
- **Course Management**: Create and manage courses, including their names, levels, and associated teachers.
- **Teacher Management**: Create and manage teacher records, including their names and emails.
- **Relationships**: Associate students with courses and courses with teachers.

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
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   pydantic
   requests
   ```

4. **Run Database Migrations**:
   Make sure your database is set up correctly and run the migrations to create the necessary tables.
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be running at `http://127.0.0.1:8000`.

## How to Use the Application

### GUI Interaction

1. **Open the GUI**:
   The GUI is built using Tkinter and allows you to interact with the FastAPI application. Run the following command to start the GUI:
   ```bash
   python gui.py
   ```

2. **Managing Students**:
   - **Create Student**: Enter the student's name, email, and associated course IDs (comma-separated) and click "Create Student".
   - **Get Students**: Click "Get Students" to retrieve and display a list of all students.

3. **Managing Courses**:
   - **Create Course**: Enter the course name, level, and teacher ID, then click "Create Course".
   - **Get Courses**: Click "Get Courses" to retrieve and display a list of all courses.

4. **Managing Teachers**:
   - **Create Teacher**: Enter the teacher's name and email, then click "Create Teacher".
   - **Get Teachers**: Click "Get Teachers" to retrieve and display a list of all teachers.

### API Endpoints

You can also interact with the application using the following API endpoints:

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of students.

- **Courses**:
  - `POST /courses/`: Create a new course.
  - `GET /courses/`: Retrieve a list of courses.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of teachers.

### Example API Request

To create a new course with a teacher, you can use the following example request:

```bash
curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner", "teacher_id": 1}'
```

## Conclusion

The ChatDev Course Management System is designed to streamline the management of educational entities. With its intuitive GUI and robust API, you can efficiently manage students, courses, and teachers. For any issues or further assistance, please refer to the documentation or contact support.

Happy Learning!
```