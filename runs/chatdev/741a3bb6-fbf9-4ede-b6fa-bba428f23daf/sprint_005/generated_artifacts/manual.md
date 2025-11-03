Here is the `manual.md` file that provides a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses.

## Overview

The Teacher Management System allows users to create and manage entities related to teachers, students, and courses. This application provides functionalities to add new teachers, students, and courses, as well as retrieve lists of these entities.

## Main Functions

- **Create Teacher**: Add a new teacher with a name and email.
- **Create Student**: Add a new student with a name and email.
- **Create Course**: Add a new course with a name and level.
- **Assign Courses to Students**: Link students to courses they are enrolled in.
- **Retrieve Lists**: Get lists of teachers, students, and courses with pagination support.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Ensure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migration**:
   Before using the application, you need to run the migration script to set up the database schema:
   ```bash
   python main.py
   ```

## Usage

Once the application is set up, you can interact with it through the provided functions. Here are some examples of how to use the application:

### Creating a Teacher

To create a new teacher, you can use the `create_teacher` function in the `crud.py` file. Here’s an example:

```python
from sqlalchemy.orm import Session
from crud import create_teacher
from schemas import TeacherCreate

# Assuming you have a session created
db: Session = SessionLocal()

new_teacher = TeacherCreate(name="John Doe", email="john.doe@example.com")
teacher = create_teacher(db, new_teacher)
print(f"Created Teacher: {teacher.name}, Email: {teacher.email}")
```

### Creating a Student

Similar to creating a teacher, you can create a student:

```python
from schemas import StudentCreate

new_student = StudentCreate(name="Jane Smith", email="jane.smith@example.com")
student = create_student(db, new_student)
print(f"Created Student: {student.name}, Email: {student.email}")
```

### Creating a Course

To create a new course, use the `create_course` function:

```python
from schemas import CourseCreate

new_course = CourseCreate(name="Mathematics", level="Beginner")
course = create_course(db, new_course)
print(f"Created Course: {course.name}, Level: {course.level}")
```

### Assigning a Course to a Student

You can assign a course to a student using the `add_course_to_student` function:

```python
add_course_to_student(db, student_id=1, course_id=1)  # Replace with actual IDs
```

### Retrieving Lists

To retrieve lists of teachers, students, or courses, you can use the respective `get_teachers`, `get_students`, or `get_courses` functions:

```python
teachers = get_teachers(db)
for teacher in teachers:
    print(f"Teacher ID: {teacher.id}, Name: {teacher.name}, Email: {teacher.email}")
```

## Conclusion

This Teacher Management System provides a simple yet effective way to manage educational entities. For further customization and enhancements, feel free to explore the codebase and modify it according to your needs.

For any issues or feature requests, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand the functionalities of the Teacher Management System, how to install it, and how to use it effectively.