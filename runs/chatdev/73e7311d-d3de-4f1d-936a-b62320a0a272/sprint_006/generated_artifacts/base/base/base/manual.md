Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Course Management System

A simple application for managing students and courses, built with FastAPI and SQLAlchemy.

## Main Functions

- **Create Course**: Allows users to create a new course with a name and level.
- **Read Course**: Enables users to retrieve information about a specific course by its ID.
- **Student Management**: (Future functionality) Manage student data, including adding and retrieving student information.

## Quick Install

To set up the environment and install the required dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://your-repo-url.git
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
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI application by running:
   ```bash
   python main.py
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

2. **Create a Course**:
   To create a new course, send a POST request to `/courses/` with the following JSON body:
   ```json
   {
       "name": "Course Name",
       "level": "Beginner"
   }
   ```
   You can use tools like Postman or curl to make this request.

3. **Read a Course**:
   To retrieve a course by its ID, send a GET request to `/courses/{course_id}` where `{course_id}` is the ID of the course you want to retrieve. For example:
   ```bash
   curl http://127.0.0.1:8000/courses/1
   ```

## API Documentation

For more detailed API documentation, you can access the automatically generated documentation provided by FastAPI at:
```
http://127.0.0.1:8000/docs
```

## Future Enhancements

- **Student Management**: Implement endpoints for creating, reading, updating, and deleting student records.
- **User Authentication**: Add user authentication to secure the application.
- **Frontend Dashboard**: Develop a user-friendly dashboard for managing courses and students.

## Conclusion

This application serves as a foundational tool for managing courses and students. It can be expanded with additional features and functionalities based on user needs. For any questions or support, please reach out to the development team.

```

This manual provides a comprehensive overview of the software, installation instructions, usage guidelines, and future enhancement ideas, ensuring users can effectively utilize the Student Course Management System.