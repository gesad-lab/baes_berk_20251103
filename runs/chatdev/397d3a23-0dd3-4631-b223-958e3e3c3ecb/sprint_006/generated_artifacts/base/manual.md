Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Overview

This application allows users to create and manage entities for teachers, students, and courses. It provides a RESTful API for performing CRUD operations on these entities. The application is built using Python, FastAPI, and SQLAlchemy, with SQLite as the database.

## Main Features

- **Create and Retrieve Teachers**: Add new teachers with their names and email addresses and retrieve a list of all teachers.
- **Create and Retrieve Students**: Add new students with their names and email addresses and retrieve a list of all students.
- **Create and Retrieve Courses**: Add new courses with their names and levels and retrieve a list of all courses.
- **Manage Student-Course Relationships**: Associate students with courses.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

```bash
pip install fastapi[all] sqlalchemy alembic
```

### Step 4: Initialize the Database

Run the following command to create the database and tables:

```bash
python -m alembic upgrade head
```

## Usage

### Running the Application

To start the FastAPI application, run:

```bash
uvicorn main:app --reload
```

### API Endpoints

#### Teachers

- **Create a Teacher**

  **POST** `/teachers/`

  Request Body:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

  Response:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

- **Get All Teachers**

  **GET** `/teachers/`

  Response:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
  ]
  ```

#### Students

- **Create a Student**

  **POST** `/students/`

  Request Body:
  ```json
  {
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
  }
  ```

  Response:
  ```json
  {
    "id": 1,
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
  }
  ```

- **Get All Students**

  **GET** `/students/`

  Response:
  ```json
  [
    {
      "id": 1,
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
  ]
  ```

#### Courses

- **Create a Course**

  **POST** `/courses/`

  Request Body:
  ```json
  {
    "name": "Mathematics",
    "level": "Beginner"
  }
  ```

  Response:
  ```json
  {
    "id": 1,
    "name": "Mathematics",
    "level": "Beginner"
  }
  ```

- **Get All Courses**

  **GET** `/courses/`

  Response:
  ```json
  [
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
  ]
  ```

### Managing Student-Course Relationships

- **Add Course to Student**

  **POST** `/students/{student_id}/courses/{course_id}`

  Response:
  ```json
  {
    "message": "Course added to student successfully"
  }
  ```

## Conclusion

This Teacher Management System provides a simple yet effective way to manage teachers, students, and courses. For further customization and enhancements, feel free to explore the codebase and contribute!

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the application, installation instructions, usage details, and API endpoints, ensuring that users can easily understand and utilize the software.