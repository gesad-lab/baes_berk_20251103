```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows users to manage students and courses effectively through a simple GUI and a RESTful API.

## Main Functions

1. **Student Management**: Create and retrieve student records.
2. **Course Management**: Create and retrieve course records.
3. **Database Management**: Automatically handles database migrations to ensure data integrity.

## Quick Install

To get started with the ChatDev Course Management System, follow these steps to install the necessary environment dependencies:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   requests
   pydantic
   tkinter
   ```

4. **Run Database Migrations**:
   After installing the dependencies, run the following command to set up the database schema:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

### Starting the Application

1. **Run the FastAPI Application**:
   Start the FastAPI application by executing:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the GUI**:
   The GUI will be available on your local machine. Simply run the `gui.py` file:
   ```bash
   python gui.py
   ```

### Using the GUI

- **Creating a Student**:
  - Enter the student's name and email in the respective fields.
  - Click the "Create Student" button to save the student record.
  - You will see a confirmation message if the student is created successfully.

- **Fetching Students**:
  - Click the "Get Students" button to retrieve and display a list of all students.

- **Creating a Course**:
  - Enter the course name and level in the respective fields.
  - Click the "Create Course" button to save the course record.
  - You will see a confirmation message if the course is created successfully.

- **Fetching Courses**:
  - Click the "Get Courses" button to retrieve and display a list of all courses.

### API Endpoints

The application also provides RESTful API endpoints for programmatic access:

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of students.

- **Courses**:
  - `POST /courses/`: Create a new course.
  - `GET /courses/`: Retrieve a list of courses.

## Database Migration

The application uses Alembic for database migrations. The migration scripts ensure that the existing student data is preserved while adding new tables or columns. 

- To add new migrations, create a new migration script in the `migrations` folder and run:
  ```bash
  alembic revision --autogenerate -m "Your migration message"
  alembic upgrade head
  ```

## Conclusion

This software provides a robust solution for managing students and courses. For any issues or feature requests, please reach out to the ChatDev support team. Happy coding!
```