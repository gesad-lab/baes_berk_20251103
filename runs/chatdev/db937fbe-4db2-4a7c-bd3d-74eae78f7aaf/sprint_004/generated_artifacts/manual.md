```markdown
# ChatDev Student-Course Management System

Welcome to the ChatDev Student-Course Management System! This software allows you to manage students and their associated courses effectively. Below is a detailed user manual that covers the main functions of the software, how to install environment dependencies, and how to use the application.

## Main Functions

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create, read, update, and delete course records.
- **Course Enrollment**: Associate students with multiple courses through a many-to-many relationship.
- **Data Persistence**: All data is stored in a SQLite database, ensuring data integrity and persistence.

## Quick Install

To get started with the ChatDev application, you need to install the required dependencies. You can do this using `pip` or `conda`.

### Using pip

```bash
pip install -r requirements.txt
```

### Using conda

```bash
conda install --file requirements.txt
```

## Environment Dependencies

The following dependencies are required for the application:

- **SQLAlchemy**: ORM (Object-Relational Mapping) library for database interactions.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **FastAPI**: A modern web framework for building APIs with Python.
- **Uvicorn**: ASGI server to run FastAPI applications.

Make sure to adjust the versions according to your project's compatibility and requirements.

## How to Use the Application

1. **Set Up the Database**:
   - Run the `main.py` script to create the necessary database tables and association tables.
   ```bash
   python main.py
   ```

2. **Start the Application**:
   - Use Uvicorn to run the FastAPI application.
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the Dashboard**:
   - Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

4. **Create a Student**:
   - Use the `/students` endpoint to create a new student by sending a POST request with the student's name and email.

5. **Create a Course**:
   - Use the `/courses` endpoint to create a new course by sending a POST request with the course's name and level.

6. **Enroll a Student in a Course**:
   - To associate a student with a course, you can update the student's record by sending a PATCH request to the `/students/{student_id}` endpoint with the list of course IDs.

7. **View Students and Courses**:
   - Use the GET requests on `/students` and `/courses` endpoints to retrieve lists of students and courses, respectively.

## Conclusion

The ChatDev Student-Course Management System provides a robust framework for managing students and their courses. With easy installation and a user-friendly API, you can efficiently handle student enrollments and course management. For further assistance, please refer to the API documentation or reach out to our support team.

Happy coding!
```