```markdown
# Course Management System

A comprehensive application for managing students, courses, and teachers, allowing for easy enrollment and relationship management.

## Main Functions

- **Student Management**: Create, retrieve, and manage student records.
- **Course Management**: Create, retrieve, and manage course records, including assigning teachers to courses.
- **Teacher Management**: Create, retrieve, and manage teacher records.
- **Enrollment**: Enroll students in courses and manage their course selections.

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   alembic
   pydantic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

1. **Create the Database**:
   Ensure that the database is created by running the following command:
   ```bash
   python -c "from database import create_database; create_database()"
   ```

2. **Run Migrations**:
   To apply the database migrations, run:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

### Running the API

1. **Start the FastAPI Server**:
   Run the following command to start the API server:
   ```bash
   uvicorn api:router --reload
   ```
   The API will be accessible at `http://127.0.0.1:8000`.

### Interacting with the API

You can interact with the API using tools like Postman or cURL, or through the provided GUI.

#### API Endpoints

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of students.

- **Courses**:
  - `POST /courses/`: Create a new course.
  - `GET /courses/`: Retrieve a list of courses.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of teachers.

- **Enrollment**:
  - `POST /students/{student_id}/courses/{course_id}/enroll`: Enroll a student in a course.

### Using the GUI

1. **Run the GUI Application**:
   Execute the following command:
   ```bash
   python main.py
   ```
   This will launch the GUI for managing students, courses, and teachers.

2. **Navigate the GUI**:
   - Use the interface to add, view, and manage students, courses, and teachers.
   - Enroll students in courses through the GUI.

## Conclusion

This Course Management System provides a robust framework for managing educational entities and their relationships. By following the installation and usage instructions, you can effectively manage students, courses, and teachers, ensuring a seamless educational experience.
```