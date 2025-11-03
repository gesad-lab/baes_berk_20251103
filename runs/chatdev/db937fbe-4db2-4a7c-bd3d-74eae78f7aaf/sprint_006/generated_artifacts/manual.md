# ChatDev Application User Manual

## Introduction

Welcome to the ChatDev application! This software is designed to manage educational entities such as Students, Courses, and Teachers. The primary function of the application is to facilitate the relationship between these entities, allowing for a comprehensive educational management system. 

With the recent update, we have added a relationship between the Course and Teacher entities, enabling each course to be associated with a specific teacher. This manual will guide you through the installation process, environment setup, and usage of the application.

## Main Functions

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create, read, update, and delete course records, including the ability to assign teachers to courses.
- **Teacher Management**: Create, read, update, and delete teacher records.
- **Relationship Management**: Establish relationships between students and courses, as well as between courses and teachers.

## Quick Install

To get started with the ChatDev application, you need to install the required dependencies. You can do this using pip:

```bash
pip install -r requirements.txt
```

Make sure you have Python installed on your machine. If you don't have it yet, you can download it from [python.org](https://www.python.org/downloads/).

## Environment Setup

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone https://github.com/your-repo/chatdev.git
   cd chatdev
   ```

2. **Install Dependencies**: Install the required Python packages.

   ```bash
   pip install sqlalchemy alembic pydantic
   ```

3. **Database Setup**: The application uses SQLite as the database. The database file will be created automatically when you run the application for the first time.

## Usage

### Running the Application

To run the application, execute the following command in your terminal:

```bash
python main.py
```

This will create the necessary database tables and run any migrations to ensure the schema is up to date.

### Creating Entities

You can create students, courses, and teachers using the provided Pydantic schemas. Here’s an example of how to create a new course with an associated teacher:

1. **Create a Teacher**:

   ```python
   from schemas import TeacherCreate
   new_teacher = TeacherCreate(name="John Doe", email="john.doe@example.com")
   ```

2. **Create a Course**:

   ```python
   from schemas import CourseCreate
   new_course = CourseCreate(name="Mathematics", level="Beginner", teacher_id=1)  # Assuming teacher with ID 1 exists
   ```

### Managing Relationships

- **Assigning a Teacher to a Course**: When creating a course, you can specify the `teacher_id` to associate the course with a specific teacher.
- **Enrolling Students in Courses**: You can manage student enrollments in courses through the many-to-many relationship established in the database.

### Database Migration

The application uses Alembic for database migrations. If you make changes to the models, you can run the following command to generate a new migration script:

```bash
alembic revision --autogenerate -m "Add teacher relationship to Course"
```

Then, apply the migration:

```bash
alembic upgrade head
```

## Conclusion

The ChatDev application provides a robust framework for managing educational entities and their relationships. By following this manual, you should be able to set up the application, manage entities, and utilize the new teacher-course relationship feature effectively. 

For further assistance, please refer to the documentation or reach out to our support team. Happy coding!