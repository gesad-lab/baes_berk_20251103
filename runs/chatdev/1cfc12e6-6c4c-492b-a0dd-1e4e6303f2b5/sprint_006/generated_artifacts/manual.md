```markdown
# Student Management Application

A comprehensive application for managing students, courses, and teachers, designed to streamline educational administration.

## Main Functions

The Student Management Application allows users to:

- **Manage Students**: Add, view, and enroll students in courses.
- **Manage Teachers**: Add and view teachers.
- **Manage Courses**: Create courses and assign teachers to them.
- **Enroll Students in Courses**: Facilitate student enrollment in specific courses.

## Installation

To set up the Student Management Application, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Create a Virtual Environment

It's recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install fastapi[all] sqlalchemy alembic requests
```

### Step 4: Run Database Migration

Before running the application, you need to set up the database schema. Run the migration script:

```bash
alembic upgrade head
```

## How to Use the Application

### Starting the Application

To start the application, run the following command:

```bash
uvicorn api:app --reload
```

This will start the FastAPI server, and you can access the API at `http://127.0.0.1:8000`.

### Using the GUI

1. **Run the GUI**: Execute the following command in your terminal:

    ```bash
    python main.py
    ```

2. **Adding Students**:
   - Enter the student's name and email in the respective fields.
   - Click on "Add Student" to save the student.

3. **Adding Teachers**:
   - Enter the teacher's name and email in the respective fields.
   - Click on "Add Teacher" to save the teacher.

4. **Creating Courses**:
   - Enter the course name and level.
   - Enter the Teacher ID for the course (this can be obtained from the teacher list).
   - Click on "Add Course" to create the course.

5. **Enrolling Students in Courses**:
   - Enter the Student ID (you can find this in the student list) and the Course ID.
   - Click on "Enroll in Course" to enroll the student.

6. **Viewing Students**:
   - Click on "View Students" to see a list of all registered students.

### API Endpoints

The application exposes several API endpoints that can be used for programmatic access:

- **Add Student**: `POST /students/`
- **Add Teacher**: `POST /teachers/`
- **Add Course**: `POST /courses/`
- **Enroll Student in Course**: `POST /enroll/{student_id}/{course_id}`
- **Get Students**: `GET /students/`
- **Get Courses**: `GET /courses/`

## Conclusion

The Student Management Application provides a user-friendly interface for managing educational entities. By following the installation and usage instructions, users can effectively manage students, teachers, and courses within their educational institutions.
```