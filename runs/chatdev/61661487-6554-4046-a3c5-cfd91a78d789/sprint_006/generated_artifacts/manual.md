Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management System

A comprehensive application for managing students, courses, and teachers.

## Overview

The Course Management System allows educational institutions to manage their courses, students, and teachers effectively. Users can create, read, and manage relationships between courses and teachers, ensuring a streamlined educational experience.

## Main Functions

- **Manage Students**: Create and retrieve student records.
- **Manage Courses**: Create and retrieve course records, including the ability to assign teachers to courses.
- **Manage Teachers**: Create and retrieve teacher records.

## Installation

To set up the Course Management System, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/course-management-system.git
   cd course-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Install the required dependencies using pip:
   ```bash
   pip install fastapi sqlalchemy pydantic
   ```

4. **Database Setup**:
   The application uses SQLite for database management. The database file will be created automatically when you run the application for the first time.

## Usage

### Running the Application

To start the application, run the following command:
```bash
uvicorn main:app --reload
```
This will start the FastAPI server, and you can access the API at `http://127.0.0.1:8000`.

### API Endpoints

The following endpoints are available for managing students, courses, and teachers:

#### Students

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get Students**:
  - **Endpoint**: `GET /students/`

#### Courses

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Intermediate",
      "student_id": 1,
      "teacher_id": 1
    }
    ```

- **Get Courses**:
  - **Endpoint**: `GET /courses/`

#### Teachers

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```

- **Get Teachers**:
  - **Endpoint**: `GET /teachers/`

### Database Migration

The application includes a migration script that creates the necessary tables for courses and teachers while preserving existing student data. To run the migration, execute:
```bash
python main.py
```

This will ensure that the database schema is updated to support the new relationships.

## Conclusion

The Course Management System is designed to simplify the management of educational entities. With its intuitive API and robust functionality, it serves as an essential tool for educational institutions.

For further assistance, please refer to the documentation or reach out to our support team.
```

This manual provides a comprehensive overview of the software, installation instructions, usage details, and API endpoints, ensuring that users can effectively utilize the Course Management System.