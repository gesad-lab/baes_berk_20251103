```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students and their associated courses efficiently. Below is a comprehensive user manual to help you get started.

## Main Functions

- **Student Management**: Create, read, and manage student records, including their email addresses.
- **Course Management**: Create, read, and manage course records, including course names and levels.
- **Student-Course Relationship**: Associate students with multiple courses and manage these relationships seamlessly.

## Quick Install

To get started with the ChatDev Course Management System, you need to install the required environment dependencies. You can do this using `pip`:

```bash
pip install fastapi sqlalchemy alembic pydantic
```

If you are using `conda`, you can install the dependencies as follows:

```bash
conda install fastapi sqlalchemy alembic pydantic -c conda-forge
```

## Setting Up the Environment

1. **Clone the Repository**: 
   Clone the repository containing the source code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   Create a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**: 
   Use the commands provided in the Quick Install section to install the necessary packages.

4. **Database Setup**: 
   The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI application by running the following command:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server at `http://127.0.0.1:8000`.

2. **Access the API Documentation**:
   You can access the interactive API documentation at `http://127.0.0.1:8000/docs`. This will allow you to test the API endpoints directly from your browser.

3. **Creating a Student**:
   To create a new student, send a POST request to `/students/` with the following JSON body:

   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

4. **Reading Students**:
   To retrieve a list of students, send a GET request to `/students/`.

5. **Creating a Course**:
   To create a new course, send a POST request to `/courses/` with the following JSON body:

   ```json
   {
       "name": "Mathematics",
       "level": "Beginner"
   }
   ```

6. **Reading Courses**:
   To retrieve a list of courses, send a GET request to `/courses/`.

7. **Associating Students with Courses**:
   To associate a student with a course, you will need to modify the student and course records in the database. This can be done by updating the `courses` field in the `Student` model.

## Database Migrations

The application uses Alembic for database migrations. To apply migrations, run the following command:

```bash
alembic upgrade head
```

This will ensure that your database schema is up to date with the latest changes.

## Conclusion

The ChatDev Course Management System provides a robust solution for managing students and courses. With the ability to create, read, and manage relationships between students and courses, this system is designed to streamline educational administration.

For further assistance, please refer to the API documentation or contact our support team.
```