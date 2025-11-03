Here's a detailed user manual for the software, following your requirements:

```markdown
# ChatDev Course Management System

A comprehensive solution for managing student and course relationships in educational environments.

## Overview

The ChatDev Course Management System allows users to manage students and their associated courses effectively. This system supports a many-to-many relationship between students and courses, enabling students to enroll in multiple courses while also allowing courses to have multiple students.

## Main Functions

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create, read, update, and delete course records.
- **Enrollment Management**: Associate students with courses, allowing for easy tracking of course enrollments.

## Quick Install

To set up the ChatDev Course Management System, you need to install the required environment dependencies. You can do this using pip:

```bash
pip install sqlalchemy pydantic uvicorn
```

## Setting Up the Environment

1. **Clone the Repository**: 
   Clone the repository containing the source code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: 
   Use pip to install the necessary packages as mentioned above.

3. **Database Setup**: 
   The application uses SQLite as the database. The database will be created automatically when you run the application for the first time.

## How to Use the Application

1. **Run the Application**: 
   Start the application using Uvicorn. This will run the FastAPI server.

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**: 
   Once the server is running, you can access the API at `http://127.0.0.1:8000`. You can use tools like Postman or curl to interact with the API.

3. **API Endpoints**:
   - **Create a Student**: 
     - Endpoint: `POST /students`
     - Body: 
       ```json
       {
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```

   - **Get All Students**: 
     - Endpoint: `GET /students`

   - **Create a Course**: 
     - Endpoint: `POST /courses`
     - Body: 
       ```json
       {
         "name": "Mathematics",
         "level": "Beginner"
       }
       ```

   - **Get All Courses**: 
     - Endpoint: `GET /courses`

   - **Enroll a Student in a Course**: 
     - Endpoint: `POST /enroll`
     - Body: 
       ```json
       {
         "student_id": 1,
         "course_id": 1
       }
       ```

4. **Database Migration**: 
   The application handles database migrations automatically. When you run the application for the first time, it will create the necessary tables and relationships while preserving existing data.

## Documentation

For more detailed documentation, including examples and advanced usage, please refer to the [FastAPI Documentation](https://fastapi.tiangolo.com/) and [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/).

## Support

If you encounter any issues or have questions, please reach out to our support team through the designated support channels.

---

Thank you for using the ChatDev Course Management System. We hope it enhances your educational management experience!
```

This manual provides a comprehensive overview of the software, installation instructions, usage guidelines, and links to further documentation. Let me know if you need any modifications or additional sections!