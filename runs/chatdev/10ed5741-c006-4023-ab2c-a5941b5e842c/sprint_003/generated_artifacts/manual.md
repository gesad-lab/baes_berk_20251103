```markdown
# Student Management System

A simple application for managing students and courses using FastAPI and SQLite.

## Main Functions

The Student Management System allows users to perform the following functions:

- **Add Students**: Create new student records with their names and email addresses.
- **View Students**: Retrieve and display a list of all registered students.
- **Add Courses**: Create new course records with their names and levels.
- **View Courses**: Retrieve and display a list of all available courses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
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
   pydantic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the Database**:
   Run the following command to create the SQLite database and tables:
   ```bash
   python -c "from database import create_database; create_database()"
   ```

## Running the Application

To start the FastAPI server, run the following command:
```bash
uvicorn main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

## Using the Application

### Adding Students

1. Open the application GUI.
2. Enter the student's name and email in the respective fields.
3. Click the "Add Student" button to submit the information.
4. A confirmation message will appear if the student is added successfully.

### Viewing Students

- The application will automatically display the list of students after adding a new student.

### Adding Courses

1. In the GUI, enter the course name and level in the respective fields.
2. Click the "Add Course" button to submit the information.
3. A confirmation message will appear if the course is added successfully.

### Viewing Courses

- The application will automatically display the list of courses after adding a new course.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Create a new student.
- **GET /students/**: Retrieve all students.
- **POST /courses/**: Create a new course.
- **GET /courses/**: Retrieve all courses.

## Conclusion

The Student Management System provides a straightforward interface for managing students and courses. By following the installation and usage instructions, users can easily set up and interact with the application.

For any issues or feature requests, please reach out to the development team.
```