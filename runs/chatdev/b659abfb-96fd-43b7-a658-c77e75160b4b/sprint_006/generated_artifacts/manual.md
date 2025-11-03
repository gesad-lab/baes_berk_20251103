```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers effectively. You can create and manage relationships between courses and teachers, ensuring a streamlined educational experience.

## Main Functions

- **Student Management**: Add and manage students, including their associated courses.
- **Course Management**: Create and manage courses, including assigning teachers to courses.
- **Teacher Management**: Add and manage teachers who can be assigned to courses.

## Quick Install

To get started with the ChatDev Course Management System, you need to install the required dependencies. You can do this using `pip`:

```bash
pip install fastapi sqlalchemy
```

If you are using a virtual environment, make sure to activate it before running the above command.

## Setting Up the Environment

1. **Clone the Repository**: Download the source code from the repository.
   
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Run the installation command mentioned above to install FastAPI and SQLAlchemy.

3. **Database Setup**: The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

## How to Use the Application

### Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

You can interact with the application using the following API endpoints:

- **Student Management**
  - `POST /students`: Create a new student.
    - Request Body: 
      ```json
      {
        "name": "Student Name",
        "email": "student@example.com",
        "course_ids": [1, 2]  // List of course IDs
      }
      ```

- **Course Management**
  - `POST /courses`: Create a new course.
    - Request Body:
      ```json
      {
        "name": "Course Name",
        "level": "Beginner",
        "teacher_id": 1  // Optional: ID of the teacher
      }
      ```

- **Teacher Management**
  - `POST /teachers`: Create a new teacher.
    - Request Body:
      ```json
      {
        "name": "Teacher Name",
        "email": "teacher@example.com"
      }
      ```

### Using the GUI

The application also includes a simple GUI for managing students:

1. Run the GUI script:
   ```bash
   python gui.py
   ```

2. Enter the student's name, email, and course IDs (comma-separated) in the respective fields.

3. Click the "Add Student" button to add the student to the database.

4. The result will be displayed below the button indicating whether the operation was successful.

## Database Migration

The application includes migration scripts to ensure that the database schema is updated without losing existing data. The migration script `migration.py` handles the addition of the `Teacher` table and the `teacher_id` column in the `Course` table.

To run the migration, execute:

```bash
python migration.py
```

This will create the necessary tables and columns in the database.

## Conclusion

The ChatDev Course Management System provides a robust platform for managing educational entities. With its easy-to-use API and GUI, you can efficiently handle students, courses, and teachers. For any issues or feature requests, please reach out to our support team.

Happy Learning!
```