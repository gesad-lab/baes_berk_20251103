```markdown
# Course Management System

A comprehensive application for managing courses, students, and teachers. This system allows users to create and manage courses, associate them with teachers, and enroll students in those courses.

## Main Functions

- **Create Students**: Add new students to the system with their names and email addresses.
- **Create Teachers**: Add new teachers to the system with their names and email addresses.
- **Create Courses**: Create new courses and associate them with a teacher.
- **View Students**: Retrieve a list of students along with the courses they are enrolled in.
- **View Courses**: Retrieve a list of courses along with the associated teacher ID.

## Installation

To set up the Course Management System, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the Course Management System code:

```bash
git clone <repository-url>
cd course-management-system
```

### Step 2: Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install fastapi[all] sqlalchemy alembic requests
```

### Step 4: Run Database Migrations

Run the database migrations to set up the initial database schema:

```bash
alembic upgrade head
```

### Step 5: Start the Application

Run the FastAPI application:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## How to Use the Application

### Accessing the API

You can interact with the API using tools like Postman or cURL, or through the automatically generated documentation at `http://127.0.0.1:8000/docs`.

### Creating Students

To create a new student, send a POST request to `/students/` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Creating Teachers

To create a new teacher, send a POST request to `/teachers/` with the following JSON body:

```json
{
  "name": "Jane Smith",
  "email": "jane.smith@example.com"
}
```

### Creating Courses

To create a new course, send a POST request to `/courses/` with the following JSON body:

```json
{
  "name": "Mathematics",
  "level": "Beginner",
  "teacher_id": 1  # Replace with the actual teacher ID
}
```

### Viewing Students

To retrieve a list of students, send a GET request to `/students/`.

### Viewing Courses

To retrieve a list of courses, send a GET request to `/courses/`.

## Graphical User Interface (GUI)

The application also includes a simple GUI built with Tkinter. To run the GUI, execute the following command:

```bash
python main.py
```

This will open a window where you can add courses and view the list of courses.

## Conclusion

The Course Management System provides a robust platform for managing educational entities. With the ability to create and associate students, teachers, and courses, it serves as a valuable tool for educational institutions.

For further assistance, please refer to the API documentation or contact support.
```