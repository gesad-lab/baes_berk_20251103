```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. You can create and enroll students in courses, manage teacher information, and establish relationships between courses and teachers.

## Main Functions

1. **Student Management**
   - Add new students.
   - View existing students.

2. **Course Management**
   - Create new courses and associate them with teachers.
   - View existing courses.

3. **Teacher Management**
   - Add new teachers.
   - View existing teachers.

4. **Enrollment Management**
   - Enroll students in courses.

## Installation

To set up the environment and run the application, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo/chatdev-course-management.git
cd chatdev-course-management
```

### Step 2: Install Dependencies

You can install the required dependencies using pip. Run the following command in your terminal:

```bash
pip install fastapi[all] sqlalchemy alembic requests
```

### Step 3: Initialize the Database

Before running the application, you need to initialize the database. You can do this by running the following command:

```bash
python main.py
```

This will create the necessary database tables and run any migrations.

## How to Use the Application

### Running the Application

To start the application, run:

```bash
python main.py
```

The application will be available at `http://127.0.0.1:8000`.

### Using the GUI

1. **Add Student**
   - Enter the student's name and email.
   - Click on "Add Student" to save the information.

2. **Show Students**
   - Click on "Show Students" to view the list of all students.

3. **Add Course**
   - Enter the course name, level, and the teacher ID associated with the course.
   - Click on "Add Course" to save the information.

4. **Show Courses**
   - Click on "Show Courses" to view the list of all courses.

5. **Add Teacher**
   - Enter the teacher's name and email.
   - Click on "Add Teacher" to save the information.

6. **Show Teachers**
   - Click on "Show Teachers" to view the list of all teachers.

7. **Enroll Student in Course**
   - Enter the Student ID and Course ID.
   - Click on "Enroll" to enroll the student in the specified course.

### API Endpoints

You can also interact with the application using the following API endpoints:

- **Students**
  - `POST /students/` - Create a new student.
  - `GET /students/` - Retrieve a list of students.

- **Courses**
  - `POST /courses/` - Create a new course.
  - `GET /courses/` - Retrieve a list of courses.

- **Teachers**
  - `POST /teachers/` - Create a new teacher.
  - `GET /teachers/` - Retrieve a list of teachers.

- **Enrollment**
  - `POST /students/{student_id}/courses/{course_id}` - Enroll a student in a course.
  - `GET /students/{student_id}/courses/` - Retrieve courses for a specific student.

## Conclusion

The ChatDev Course Management System is designed to simplify the management of educational entities. By following the steps outlined in this manual, you can easily set up and use the application to manage students, courses, and teachers effectively. If you encounter any issues or have questions, please refer to the documentation or reach out for support.
```