Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management System

A simple application for managing students and courses.

## Overview

The Course Management System allows users to create and manage student and course entities. It provides a RESTful API for creating and retrieving students and courses, making it easy to integrate with other applications.

## Main Functions

- **Create Student**: Add a new student with a name and email.
- **Get Students**: Retrieve a list of all students.
- **Create Course**: Add a new course with a name and level.
- **Get Courses**: Retrieve a list of all courses.

## Installation

To set up the Course Management System, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository from GitHub (or your source control):

```bash
git clone <repository-url>
cd course-management-system
```

### Step 2: Install Dependencies

Install the required Python packages using pip:

```bash
pip install fastapi[all] sqlalchemy
```

### Step 3: Set Up the Database

The application uses SQLite for the database. To create the database and the necessary tables, run the migration script:

```bash
python main.py
```

## Usage

### Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn routes:student_router --reload
```

This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

#### Students

- **Create Student**
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get Students**
  - **Endpoint**: `GET /students/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    ]
    ```

#### Courses

- **Create Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get Courses**
  - **Endpoint**: `GET /courses/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
      }
    ]
    ```

## Conclusion

The Course Management System provides a straightforward way to manage students and courses through a RESTful API. By following the installation and usage instructions, you can quickly set up and start using the application.

For further assistance, please refer to the documentation or reach out for support.
```

This manual provides a comprehensive overview of the software, including installation instructions, main functions, and usage details. Let me know if you need any modifications or additional information!