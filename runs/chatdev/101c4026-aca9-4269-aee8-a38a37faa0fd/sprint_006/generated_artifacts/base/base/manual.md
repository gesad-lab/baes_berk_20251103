Here's a detailed user manual for the software, formatted in Markdown:

```markdown
# Student Course Management System

A FastAPI application for managing students and their course enrollments.

## Overview

This application allows users to perform CRUD operations on `Student` and `Course` entities. Students can enroll in multiple courses, and the application supports a many-to-many relationship between students and courses.

## Main Functions

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create, read, update, and delete course records.
- **Enrollment**: Enroll students in multiple courses and manage their course associations.

## Quick Install

To get started, you'll need to install the necessary dependencies. You can do this using pip:

```bash
pip install fastapi[all] sqlalchemy alembic
```

Alternatively, if you are using conda, you can install the dependencies as follows:

```bash
conda install fastapi sqlalchemy alembic -c conda-forge
```

## Setting Up the Environment

1. **Clone the Repository**: Clone the repository containing the source code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**: Run the installation command mentioned above.

4. **Database Migration**: Before running the application, you need to apply the database migrations to create the necessary tables.
   ```bash
   alembic upgrade head
   ```

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Student Endpoints

- **Create a Student**
  - **POST** `/students/`
  - Request Body: `{ "name": "John Doe", "email": "john@example.com", "course_ids": [1, 2] }`
  
- **Get All Students**
  - **GET** `/students/`
  
- **Get a Student by ID**
  - **GET** `/students/{student_id}`
  
- **Update a Student**
  - **PUT** `/students/{student_id}`
  - Request Body: `{ "name": "John Doe", "email": "john@example.com", "course_ids": [1, 2] }`
  
- **Delete a Student**
  - **DELETE** `/students/{student_id}`

### Course Endpoints

- **Create a Course**
  - **POST** `/courses/`
  - Request Body: `{ "name": "Mathematics", "level": "Beginner" }`
  
- **Get All Courses**
  - **GET** `/courses/`
  
- **Get a Course by ID**
  - **GET** `/courses/{course_id}`
  
- **Update a Course**
  - **PUT** `/courses/{course_id}`
  - Request Body: `{ "name": "Mathematics", "level": "Intermediate" }`
  
- **Delete a Course**
  - **DELETE** `/courses/{course_id}`

## Conclusion

This application provides a robust framework for managing students and their course enrollments. With the ability to create, read, update, and delete both students and courses, it serves as a comprehensive solution for educational institutions.

For further details, please refer to the code documentation or the FastAPI documentation.
```

This manual provides a comprehensive overview of the application, including installation instructions, usage, and API endpoints. It should serve as a useful guide for users to effectively interact with the software.