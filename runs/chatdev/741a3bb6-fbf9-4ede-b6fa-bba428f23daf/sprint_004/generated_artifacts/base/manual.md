Here's the `manual.md` file that provides a detailed user manual for the software, including an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Course Management Application

A simple application for managing students and courses, allowing users to create and retrieve information about students and courses.

## Main Functions

The Course Management Application provides the following functionalities:

- **Student Management**: Create and retrieve student records, including their names and email addresses.
- **Course Management**: Create and retrieve course records, including course names and levels.
- **Database Migration**: Automatically handles database migrations to ensure that existing student data is preserved while adding new course entities.

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
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   sqlalchemy
   pydantic
   ```

## Usage

1. **Run the Application**:
   To start the application and perform database migrations, run:
   ```bash
   python main.py
   ```

   This will create the necessary database tables, including the new `Course` table, while preserving existing student data.

2. **Creating a Student**:
   To create a new student, you can use the `create_student` function in the `crud.py` file. You will need to provide a name and an email address.

3. **Creating a Course**:
   To create a new course, use the `create_course` function in the `crud.py` file. You will need to provide a course name and level.

4. **Retrieving Students**:
   To retrieve a list of students, use the `get_students` function. You can specify pagination options such as `skip` and `limit`.

5. **Retrieving Courses**:
   To retrieve a list of courses, use the `get_courses` function with pagination options.

## Example Usage

Here’s a quick example of how to create a student and a course:

```python
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import StudentCreate, CourseCreate
from crud import create_student, create_course

# Create a new database session
db: Session = SessionLocal()

# Create a new student
new_student = StudentCreate(name="John Doe", email="john.doe@example.com")
created_student = create_student(db, new_student)

# Create a new course
new_course = CourseCreate(name="Introduction to Programming", level="Beginner")
created_course = create_course(db, new_course)

print(f"Created Student: {created_student.name}, Email: {created_student.email}")
print(f"Created Course: {created_course.name}, Level: {created_course.level}")
```

## Additional Resources

For more detailed documentation on the application, including API references and advanced usage, please refer to the code comments and the Pydantic documentation for data validation.

Feel free to reach out if you have any questions or need further assistance!
```

This manual provides a comprehensive overview of the application, its functionalities, installation steps, and usage examples, ensuring that users can effectively utilize the software.