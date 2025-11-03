Here's a detailed user manual for the software, including the main functions, installation instructions, and usage guidelines.

```markdown
# Course Management System

A simple API for managing students and courses, built using FastAPI and SQLAlchemy.

## Main Functions

This application provides the following functionalities:

- **Create Students**: Allows users to create new student records with a name and email.
- **Retrieve Students**: Fetches a list of all students with pagination support.
- **Create Courses**: Enables users to create new course records with a name and level.
- **Retrieve Courses**: Fetches a list of all courses with pagination support.

## Installation Instructions

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   ```

   Then, install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Once the server is running, you can access the API documentation at:
   ```
   http://127.0.0.1:8000/docs
   ```

3. **Creating a Student**:
   To create a new student, send a POST request to `/students/` with the following JSON body:
   ```json
   {
     "name": "John Doe",
     "email": "john.doe@example.com"
   }
   ```

4. **Retrieving Students**:
   To retrieve a list of students, send a GET request to `/students/`. You can also use query parameters `skip` and `limit` for pagination:
   ```
   GET /students/?skip=0&limit=10
   ```

5. **Creating a Course**:
   To create a new course, send a POST request to `/courses/` with the following JSON body:
   ```json
   {
     "name": "Introduction to Programming",
     "level": "Beginner"
   }
   ```

6. **Retrieving Courses**:
   To retrieve a list of courses, send a GET request to `/courses/`. Similar to students, you can use `skip` and `limit` for pagination:
   ```
   GET /courses/?skip=0&limit=10
   ```

## Database Migration

The application is designed to preserve existing student data while adding the new Course table. The migration process is handled automatically when the application starts, ensuring that the database schema is up-to-date.

## Conclusion

This Course Management System provides a straightforward way to manage students and courses through a RESTful API. For further customization or feature requests, feel free to reach out to the development team.

```

This manual provides a comprehensive overview of the software, guiding users through installation, usage, and understanding the main functionalities.