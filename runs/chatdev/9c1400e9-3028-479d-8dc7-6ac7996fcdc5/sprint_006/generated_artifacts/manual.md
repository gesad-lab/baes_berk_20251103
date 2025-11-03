```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. You can create, update, and manage relationships between these entities seamlessly.

## Main Functions

- **Student Management**: Add, view, and manage student information including name and email.
- **Course Management**: Create and manage courses, including associating them with teachers.
- **Teacher Management**: Add and manage teacher information including name and email.
- **Relationships**: Establish relationships between courses and teachers, and between students and courses.

## Quick Install

To get started, you need to install the required dependencies. You can do this using pip:

```bash
pip install fastapi sqlalchemy alembic requests
```

If you are using Anaconda, you can install the dependencies with:

```bash
conda install fastapi sqlalchemy alembic requests -c conda-forge
```

## Setting Up the Environment

1. **Clone the Repository**: Clone the repository containing the code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run Migrations**: Ensure the database schema is up to date by running the migrations.

   ```bash
   alembic upgrade head
   ```

3. **Start the Application**: Run the FastAPI application.

   ```bash
   uvicorn main:app --reload
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

## How to Use the Application

### API Endpoints

The application exposes the following API endpoints:

- **Students**
  - `POST /students`: Create a new student.
    - Request Body: `{ "name": "Student Name", "email": "student@example.com" }`
  
- **Courses**
  - `POST /courses`: Create a new course associated with a teacher.
    - Request Body: `{ "name": "Course Name", "level": "Course Level", "teacher_id": 1 }`
  
- **Teachers**
  - `POST /teachers`: Create a new teacher.
    - Request Body: `{ "name": "Teacher Name", "email": "teacher@example.com" }`

### GUI Interaction

You can also interact with the application using the provided GUI built with Tkinter. Follow these steps:

1. **Run the GUI**: Ensure the FastAPI server is running, then execute the GUI script.

   ```bash
   python gui.py
   ```

2. **Register Students**: Fill in the student name and email, then click "Submit Student".

3. **Register Courses**: Fill in the course name, level, and the teacher ID, then click "Submit Course".

4. **Register Teachers**: Fill in the teacher name and email, then click "Submit Teacher".

### Example Usage

1. **Add a Teacher**:
   - Name: John Doe
   - Email: john.doe@example.com

2. **Add a Course**:
   - Name: Mathematics 101
   - Level: Beginner
   - Teacher ID: 1 (assuming John Doe is the first teacher added)

3. **Add a Student**:
   - Name: Jane Smith
   - Email: jane.smith@example.com

## Conclusion

The ChatDev Course Management System is designed to streamline the management of educational entities. With its intuitive API and GUI, you can easily manage students, courses, and teachers, while maintaining the relationships between them. For further assistance, please refer to the documentation or contact support.

Happy Learning!
```