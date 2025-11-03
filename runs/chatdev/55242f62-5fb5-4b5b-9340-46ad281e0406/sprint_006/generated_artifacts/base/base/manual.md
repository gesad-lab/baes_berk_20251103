```markdown
# Student Course Management Application

A simple application to manage students and their course enrollments.

## Main Functions

This application allows users to:

- Create new students with their email addresses.
- Create new courses with specified levels.
- Enroll students in courses, establishing a many-to-many relationship between students and courses.
- Retrieve student and course information, including enrolled courses for each student.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install fastapi sqlalchemy alembic pydantic
   ```

4. **Install an ASGI server for running the application:**
   ```bash
   pip install uvicorn
   ```

## Database Setup

1. **Run the database migrations to set up the schema:**
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation:**
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation provided by FastAPI.

### API Endpoints

- **Create a Student**
  - **Endpoint:** `POST /students/`
  - **Request Body:**
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Create a Course**
  - **Endpoint:** `POST /courses/`
  - **Request Body:**
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Enroll a Student in a Course**
  - **Endpoint:** `POST /students/{student_id}/enroll/`
  - **Path Parameters:**
    - `student_id`: ID of the student to enroll.
    - `course_id`: ID of the course to enroll the student in.
  - **Example Request:**
    ```bash
    curl -X POST "http://127.0.0.1:8000/students/1/enroll/?course_id=1"
    ```

## Additional Information

- **Data Persistence:** The application uses SQLite for data storage, and all data will be preserved across server restarts.
- **Error Handling:** The application includes basic error handling for cases where students or courses are not found.

## Conclusion

This application provides a straightforward way to manage students and their course enrollments. For further customization or feature requests, please reach out to our support team.
```