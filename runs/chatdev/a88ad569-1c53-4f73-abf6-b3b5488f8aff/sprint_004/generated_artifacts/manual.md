Here's a detailed user manual for the Student Management System, incorporating the main functions, installation instructions, and usage guidelines.

```markdown
# Student Management System

A comprehensive application for managing students and their course enrollments.

## Quick Install

To set up the Student Management System, you need to install the required environment dependencies. You can do this using pip:

```bash
pip install fastapi sqlalchemy pydantic
```

Additionally, you will need to install an ASGI server to run the application. We recommend using `uvicorn`:

```bash
pip install uvicorn
```

## 🤔 What is this?

The Student Management System allows users to manage student records and their associated courses. It provides functionalities to create students, create courses, and manage the relationships between them. The system supports a many-to-many relationship between students and courses, allowing students to enroll in multiple courses.

### Main Features

- **Create Students**: Add new students to the system with their name and email.
- **Create Courses**: Add new courses with a name and level.
- **Enroll Students in Courses**: Associate students with multiple courses.
- **Data Persistence**: All data is stored in a SQLite database, ensuring data is preserved across sessions.

## 📖 How to Use

### Starting the Application

To start the application, run the following command in your terminal:

```bash
uvicorn main:app --reload
```

This will start the FastAPI application, and you can access the API documentation at `http://127.0.0.1:8000/docs`.

### API Endpoints

#### 1. Create a Student

**Endpoint**: `POST /students/`

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "course_ids": [1, 2]  // Optional: List of course IDs to enroll the student in
}
```

**Response**:
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "courses": [1, 2]
}
```

#### 2. Create a Course

**Endpoint**: `POST /courses/`

**Request Body**:
```json
{
  "name": "Mathematics",
  "level": "Intermediate"
}
```

**Response**:
```json
{
  "id": 1,
  "name": "Mathematics",
  "level": "Intermediate"
}
```

### Database Migration

The application includes a migration script that ensures the database schema is updated without losing existing data. The following changes are made during migration:

- An `email` column is added to the `students` table.
- A many-to-many relationship is established between `students` and `courses` through the `student_courses` association table.

### Accessing the Database

The application uses SQLite for data storage. The database file is located at `./students.db`. You can use any SQLite client to view and manage the data directly if needed.

## Conclusion

The Student Management System is a powerful tool for managing student and course data. With its easy-to-use API and robust features, it simplifies the process of tracking student enrollments and course offerings. For further assistance, please refer to the API documentation or reach out for support.
```

This manual provides a comprehensive overview of the Student Management System, guiding users through installation, usage, and understanding the application's core functionalities.