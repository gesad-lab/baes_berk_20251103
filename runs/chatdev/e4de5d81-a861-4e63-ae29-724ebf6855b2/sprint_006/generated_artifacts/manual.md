```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows users to manage students, courses, and teachers efficiently. You can create and view students, courses, and teachers, as well as establish relationships between courses and teachers.

## Main Functions

- **Student Management**: Create and manage student records, including their names, emails, and enrolled courses.
- **Course Management**: Create and manage courses, including course names, levels, and assigned teachers.
- **Teacher Management**: Create and manage teacher records, including their names and emails.
- **Relationships**: Establish a relationship between courses and teachers, allowing each course to have a designated teacher.

## Installation

To run the ChatDev Course Management System, you need to set up your environment with the required dependencies. Follow these steps:

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

3. **Install Required Dependencies**:
   Ensure you have `pip` installed, then run:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Initialize the Database**:
   The application uses SQLite for the database. You can initialize the database by running:
   ```bash
   python database.py
   ```

5. **Run the Application**:
   Start the FastAPI application with the following command:
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the Dashboard**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation and test the endpoints.

## How to Use the Application

### 1. Adding a Student
- Enter the student's name and email.
- Provide the course IDs (comma-separated) they will be enrolled in.
- Click the "Add Student" button to create the student record.

### 2. Adding a Course
- Enter the course name and level.
- Specify the teacher ID for the course.
- Click the "Add Course" button to create the course record.

### 3. Adding a Teacher
- Enter the teacher's name and email.
- Click the "Add Teacher" button to create the teacher record.

### 4. Viewing Records
- Use the "Get Students", "Get Courses", and "Get Teachers" buttons to retrieve and display the lists of students, courses, and teachers, respectively.

### 5. Managing Relationships
- When creating a course, you can specify a teacher by entering their ID. This establishes a relationship between the course and the teacher.

## Conclusion

The ChatDev Course Management System provides a simple yet powerful way to manage educational entities. By following the installation and usage instructions, you can effectively utilize this software to streamline your course management processes.

For further assistance or feature requests, please contact our support team.
```