```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage courses, students, and teachers effectively. You can create, read, and manage relationships between courses and teachers, ensuring a streamlined educational experience.

## Main Functions

- **Manage Students**: Create and manage student records, including their names and emails.
- **Manage Courses**: Create and manage courses, including their names, levels, and associated teachers.
- **Manage Teachers**: Create and manage teacher records, including their names and emails.
- **Relationships**: Establish relationships between courses and teachers, allowing each course to have a designated teacher.

## Quick Install

To get started, you need to install the necessary environment dependencies. You can do this using `pip`:

```bash
pip install sqlalchemy fastapi alembic pydantic
```

Or if you are using `conda`, you can install the dependencies as follows:

```bash
conda install sqlalchemy fastapi alembic pydantic -c conda-forge
```

## Setting Up the Environment

1. **Clone the Repository**: First, clone the repository containing the code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**: Use the commands provided above to install the required packages.

4. **Database Setup**: The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

## How to Use the Application

1. **Run the Application**: Start the FastAPI application by running the following command:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server at `http://127.0.0.1:8000`.

2. **Access the API Documentation**: Once the server is running, you can access the interactive API documentation at `http://127.0.0.1:8000/docs`. This interface allows you to test the API endpoints directly.

3. **API Endpoints**:
   - **Students**:
     - `POST /students/`: Create a new student.
     - `GET /students/`: Retrieve a list of students.
   - **Courses**:
     - `POST /courses/`: Create a new course (include `teacher_id` to associate with a teacher).
     - `GET /courses/`: Retrieve a list of courses.
   - **Teachers**:
     - `POST /teachers/`: Create a new teacher.
     - `GET /teachers/`: Retrieve a list of teachers.

4. **Example Requests**:
   - **Create a Student**:
     ```json
     POST /students/
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

   - **Create a Course**:
     ```json
     POST /courses/
     {
       "name": "Mathematics",
       "level": "Beginner",
       "teacher_id": 1  // Assuming teacher with ID 1 exists
     }
     ```

   - **Create a Teacher**:
     ```json
     POST /teachers/
     {
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
     }
     ```

## Conclusion

The ChatDev Course Management System is designed to simplify the management of educational entities. By following the instructions above, you can set up the environment, run the application, and start managing students, courses, and teachers effectively. If you have any questions or need further assistance, feel free to reach out!

Happy coding!
```