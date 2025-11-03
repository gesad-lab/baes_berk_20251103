```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses in an educational context.

## Main Functions

The Teacher Management System allows users to perform the following operations:

- **Create Teachers**: Add new teachers with their names and email addresses.
- **Create Students**: Add new students with their names, email addresses, and enroll them in courses.
- **Create Courses**: Add new courses with their names and levels.
- **Enroll Students in Courses**: Enroll students in specific courses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Set Up the Database**:
   The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

## Usage

1. **Run the Application**:
   To start the FastAPI application, run:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Once the server is running, you can access the API documentation at:
   ```
   http://127.0.0.1:8000/docs
   ```

3. **Creating a Teacher**:
   To create a new teacher, send a POST request to `/teachers/` with the following JSON body:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

4. **Creating a Student**:
   To create a new student, send a POST request to `/students/` with the following JSON body:
   ```json
   {
       "name": "Jane Smith",
       "email": "jane.smith@example.com",
       "course_ids": [1, 2]  // Optional: IDs of courses to enroll in
   }
   ```

5. **Creating a Course**:
   To create a new course, send a POST request to `/courses/` with the following JSON body:
   ```json
   {
       "name": "Mathematics",
       "level": "Intermediate"
   }
   ```

6. **Enroll a Student in a Course**:
   To enroll a student in a course, send a POST request to `/students/{student_id}/courses/{course_id}/` where you replace `{student_id}` and `{course_id}` with the respective IDs.

## Database Migrations

The application uses Alembic for database migrations. To create a new migration after modifying the models, run:
```bash
alembic revision --autogenerate -m "Your migration message"
```
Then, apply the migration with:
```bash
alembic upgrade head
```

## Conclusion

This Teacher Management System provides a simple yet effective way to manage teachers, students, and courses. With FastAPI's automatic documentation, you can easily interact with the API and extend its functionality as needed.
```
