```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System, a powerful application designed to manage students, courses, and teachers effectively. This software allows you to create and manage relationships between courses and teachers, ensuring a seamless educational experience.

## Main Functions

- **Student Management**: Create, read, and manage student records, including their enrolled courses.
- **Course Management**: Create, read, and manage courses, including associating them with teachers.
- **Teacher Management**: Create and manage teacher records, allowing them to be linked to courses.
- **Enrollment**: Enroll students in courses and retrieve their enrolled courses.

## Quick Install

To get started with the ChatDev Course Management System, you need to install the required dependencies. You can do this using `pip` or `conda`.

### Using pip

```bash
pip install -r requirements.txt
```

### Using conda

```bash
conda install --file requirements.txt
```

## Environment Setup

1. **Clone the Repository**: Start by cloning the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use the commands above to install the necessary dependencies.

3. **Database Setup**: The application uses SQLite for database management. The database will be automatically created when you run the application for the first time.

## How to Use the Application

### Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the server, and you can access the API at `http://127.0.0.1:8000`.

### API Endpoints

The application provides several API endpoints for managing students, courses, and teachers. Below are some key endpoints:

- **Students**
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of students.
  - `GET /students/{student_id}/courses`: Retrieve courses for a specific student.

- **Courses**
  - `POST /courses/`: Create a new course.
  - `GET /courses/`: Retrieve a list of courses.
  - `POST /students/{student_id}/courses/{course_id}`: Enroll a student in a course.

- **Teachers**
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of teachers.

### Example Usage

1. **Creating a Student**:
   Send a POST request to `/students/` with the following JSON body:

   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

2. **Creating a Course**:
   Send a POST request to `/courses/` with the following JSON body:

   ```json
   {
       "name": "Mathematics 101",
       "level": "Beginner",
       "teacher_id": 1
   }
   ```

3. **Enrolling a Student in a Course**:
   Send a POST request to `/students/{student_id}/courses/{course_id}` to enroll a student in a specific course.

## Documentation

For more detailed documentation, please refer to the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)

## Support

If you encounter any issues or have questions, please reach out to our support team. We are here to help you make the most of the ChatDev Course Management System.

Thank you for choosing ChatDev!
```