```markdown
# Student Course Management System

A FastAPI application for managing students and their course enrollments. This system allows users to create students, create courses, and enroll students in courses, all while maintaining a many-to-many relationship between students and courses.

## Main Functions

- **Create Students**: Add new students to the system with their name and email.
- **Read Students**: Retrieve student information, including the courses they are enrolled in.
- **Enroll Students in Courses**: Enroll a student in a specific course.
- **Create Courses**: Add new courses to the system with their name and level.
- **Read Courses**: Retrieve course information.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by Swagger UI.

3. **API Endpoints**:
   - **Create a Student**:
     - **POST** `/students/`
     - Body: `{ "name": "John Doe", "email": "john@example.com" }`
   - **Read a Student**:
     - **GET** `/students/{student_id}`
   - **Enroll a Student in a Course**:
     - **POST** `/students/{student_id}/courses/{course_id}`
   - **Create a Course**:
     - **POST** `/courses/`
     - Body: `{ "name": "Mathematics", "level": "Beginner" }`
   - **Read a Course**:
     - **GET** `/courses/{course_id}`

## Database Migration

The application uses Alembic for database migrations. To apply the migrations, ensure that the database is set up correctly and run the following command:
```bash
alembic upgrade head
```

This command will create the necessary tables and relationships in the SQLite database while preserving existing data.

## Conclusion

This Student Course Management System provides a robust framework for managing students and their course enrollments. With the FastAPI framework, it offers a fast and efficient way to handle CRUD operations and maintain relationships between entities. For further customization and development, refer to the codebase and the API documentation.
```