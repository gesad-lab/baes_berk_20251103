Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Course Management System

A simple application for managing students and their course enrollments.

## Main Functions

The Student Course Management System allows users to:

- Create and manage student records.
- Create and manage course records.
- Enroll students in courses.
- Retrieve lists of students and courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install fastapi[all] sqlalchemy
   ```

## Database Setup

The application uses SQLite as the database. The database will be created automatically when you run the application for the first time. 

### Initial Database Creation

When you run the application, it will automatically create the necessary tables for students and courses, including the association table for student-course relationships.

## How to Use the Application

### Running the Application

To start the application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the API documentation at `http://127.0.0.1:8000/docs`.

### API Endpoints

#### Students

- **Create a Student**
  - **Endpoint:** `POST /students/`
  - **Request Body:**
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get All Students**
  - **Endpoint:** `GET /students/`
  - **Response:**
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

- **Create a Course**
  - **Endpoint:** `POST /courses/`
  - **Request Body:**
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get All Courses**
  - **Endpoint:** `GET /courses/`
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
      }
    ]
    ```

#### Enroll Student in Course

- **Enroll a Student in a Course**
  - **Endpoint:** `POST /students/{student_id}/courses/{course_id}`
  - **Path Parameters:**
    - `student_id`: ID of the student to enroll.
    - `course_id`: ID of the course to enroll the student in.
  - **Response:**
    ```json
    {
      "message": "Student enrolled in course successfully"
    }
    ```

## Conclusion

This Student Course Management System provides a straightforward way to manage students and their course enrollments. For further customization or enhancements, feel free to modify the code as per your requirements.

For any issues or support, please reach out to the development team.
```

This manual provides a comprehensive overview of the software, including installation instructions, main functionalities, and how to use the application effectively.