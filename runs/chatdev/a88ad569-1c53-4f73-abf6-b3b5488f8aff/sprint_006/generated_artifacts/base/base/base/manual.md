Here's a detailed user manual for the Student Management System, including installation instructions and usage guidelines.

```markdown
# Student Management System

A web application for managing students and courses, allowing users to create and manage student and course records efficiently.

## Main Functions

- **Student Management**: Create, read, and manage student records, including their names and email addresses.
- **Course Management**: Create and manage courses with specific names and levels.
- **Database Migration**: Automatically updates the database schema to include new entities while preserving existing data.

## Quick Install

To set up the Student Management System, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy pydantic uvicorn
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be available at `http://127.0.0.1:8000`.

## How to Use

### Accessing the API

The application exposes a RESTful API for managing students and courses. You can interact with the API using tools like Postman or cURL.

### Creating a Student

To create a new student, send a POST request to `/students/` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Creating a Course

To create a new course, send a POST request to `/courses/` with the following JSON body:

```json
{
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

### Database Migration

The application includes a migration script that automatically updates the database schema to include the new Course table while preserving existing Student data. This is handled during the startup event of the application.

### Viewing Documentation

For more detailed API documentation, visit `http://127.0.0.1:8000/docs` to explore the available endpoints and their functionalities.

## Conclusion

The Student Management System is designed to simplify the management of student and course records. By following the installation and usage instructions, you can quickly set up and start using the application. For further assistance, please refer to the documentation or reach out for support.
```

This manual provides a comprehensive overview of the Student Management System, including its main functions, installation steps, and usage instructions.