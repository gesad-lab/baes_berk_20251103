```markdown
# Student Course Management System

A FastAPI application for managing students and their course enrollments.

## Quick Install

To set up the environment and install the necessary dependencies, run the following command:

```bash
pip install fastapi sqlalchemy alembic
```

## 🛠️ Environment Setup

1. **Clone the Repository**:
   Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Install Dependencies**:
   Install the required Python packages using pip.

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Initialization**:
   The application uses SQLite for the database. The database will be initialized automatically when you run the application for the first time.

## 📖 Application Overview

This application allows you to manage students and their course enrollments. The main functionalities include:

- **Create Students**: Add new students to the database.
- **Create Courses**: Add new courses to the database.
- **Enroll Students in Courses**: Enroll students in specific courses.
- **Retrieve Students and Courses**: Fetch lists of students and courses.

## 🚀 How to Use

### 1. Start the Application

Run the application using the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server at `http://127.0.0.1:8000`.

### 2. API Endpoints

You can interact with the application using the following API endpoints:

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
  - **Response**: Returns a list of students.

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**: Returns a list of courses.

- **Enroll Student in Course**:
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}/enroll`
  - **Path Parameters**:
    - `student_id`: ID of the student to enroll.
    - `course_id`: ID of the course to enroll in.
  - **Response**: Confirmation message upon successful enrollment.

### 3. Database Migration

The application uses Alembic for database migrations. The migration script for the association table `student_courses` is included. To apply migrations, ensure that the database is initialized, and the application will automatically run migrations on startup.

## 📚 Documentation

For more detailed documentation, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).

## 🤝 Support

If you encounter any issues or have questions, please reach out to our support team or check the issues section of the repository.

```
