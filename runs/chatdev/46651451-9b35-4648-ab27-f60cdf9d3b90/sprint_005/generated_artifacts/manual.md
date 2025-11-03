Here's a detailed user manual for the software that includes an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses in an educational environment.

## Main Functions

The Teacher Management System allows users to:

- **Create Teachers**: Add new teachers with their names and email addresses.
- **Manage Students**: Add and manage student information, including their names and email addresses.
- **Manage Courses**: Create and manage courses, including their names and levels.
- **Associate Students with Courses**: Link students to the courses they are enrolled in.

## Quick Install

To set up the Teacher Management System, you need to install the required dependencies. You can do this using pip:

```bash
pip install sqlalchemy pydantic uvicorn
```

Alternatively, if you are using Anaconda, you can install the dependencies with:

```bash
conda install sqlalchemy pydantic -c conda-forge
```

## Database Setup

The application uses SQLite as its database. The database file will be created automatically when you run the application for the first time. Ensure that you have write permissions in the directory where you are running the application.

## How to Use

1. **Run the Application**: Start the application using the following command:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server and allow you to interact with the API.

2. **Create a Teacher**: To create a new teacher, send a POST request to the `/teachers` endpoint with the following JSON body:

   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

   This will create a new teacher in the database.

3. **Create a Student**: To add a new student, send a POST request to the `/students` endpoint with the following JSON body:

   ```json
   {
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
   }
   ```

4. **Create a Course**: To create a new course, send a POST request to the `/courses` endpoint with the following JSON body:

   ```json
   {
       "name": "Mathematics",
       "level": "Intermediate"
   }
   ```

5. **Enroll a Student in a Course**: To associate a student with a course, you will need to use the many-to-many relationship. This can be done by sending a POST request to the `/enroll` endpoint with the student ID and course ID.

## API Documentation

For more detailed API documentation, including endpoints and request/response formats, please refer to the code comments and the Pydantic schemas defined in `schemas.py`.

## Conclusion

The Teacher Management System provides a simple yet effective way to manage teachers, students, and courses. By following the installation and usage instructions above, you can quickly set up and start using the application.

For any issues or support, please reach out to the development team.
```

This manual provides a comprehensive overview of the software, installation instructions, and usage guidelines, ensuring that users can easily understand and utilize the Teacher Management System.