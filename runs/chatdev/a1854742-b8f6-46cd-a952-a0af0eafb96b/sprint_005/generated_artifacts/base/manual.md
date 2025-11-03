```markdown
# ChatDev Student Course Management System

Welcome to the ChatDev Student Course Management System! This software allows you to manage students and their course enrollments efficiently. Below, you will find detailed instructions on how to install the necessary dependencies, as well as how to use the software.

## Main Functions

- **Student Management**: Create and manage student records, including their names, emails, and enrolled courses.
- **Course Management**: Create and manage courses, including course names and levels.
- **Enrollment**: Enroll students in courses and manage their course relationships.
- **Database Management**: The system uses SQLAlchemy for ORM and Alembic for database migrations, ensuring data integrity and easy schema updates.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-student-course-management.git
   cd chatdev-student-course-management
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
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Software

### Running the Application

1. **Start the FastAPI Application**:
   To run the application, execute the following command:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Access the API Documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI. Here, you can test the API endpoints.

### API Endpoints

- **Create a Student**:
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com",
       "course_ids": [1, 2]
     }
     ```
   - **Description**: Creates a new student and enrolls them in the specified courses.

- **Create a Course**:
   - **Endpoint**: `POST /courses/`
   - **Request Body**:
     ```json
     {
       "name": "Mathematics",
       "level": "Beginner"
     }
     ```
   - **Description**: Creates a new course.

- **Enroll a Student in a Course**:
   - **Endpoint**: `POST /students/{student_id}/courses/{course_id}/`
   - **Description**: Enrolls an existing student in a specified course.

### Database Migration

To apply database migrations, use Alembic. You can create migration scripts and apply them to ensure your database schema is up to date. The migration scripts are located in the `migrations` directory.

1. **Create a Migration**:
   ```bash
   alembic revision --autogenerate -m "Add course relationship to Student entity"
   ```

2. **Apply Migrations**:
   ```bash
   alembic upgrade head
   ```

## Conclusion

This software provides a robust solution for managing students and their course enrollments. By following the instructions above, you can set up the environment, run the application, and start managing your student data effectively. For further assistance, please refer to the API documentation or contact support.

Happy coding!
```