```markdown
# Student and Course Management System

A simple application for managing students and courses, allowing users to add students, courses, and enroll students in courses.

## Main Functions

1. **Add Student**: Allows users to add a new student by providing their name and email.
2. **Get Students**: Fetches and displays a list of all registered students.
3. **Add Course**: Enables users to create a new course by specifying its name and level.
4. **Get Courses**: Retrieves and displays a list of all available courses.
5. **Enroll Student in Course**: Facilitates the enrollment of a student in a specific course by providing the student ID and course ID.

## Installation

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
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   tkinter  # Usually included with Python installations
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:
   Start the FastAPI application by running:
   ```bash
   python main.py
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

2. **Open the GUI**:
   The GUI will automatically launch, allowing you to interact with the application.

3. **Adding Students**:
   - Enter the student's name and email in the respective fields.
   - Click on "Add Student" to register the student.

4. **Viewing Students**:
   - Click on "Get Students" to display a list of all registered students.

5. **Adding Courses**:
   - Enter the course name and level in the respective fields.
   - Click on "Add Course" to create the course.

6. **Viewing Courses**:
   - Click on "Get Courses" to display a list of all available courses.

7. **Enrolling Students in Courses**:
   - Enter the student ID and course ID in the respective fields.
   - Click on "Enroll Student in Course" to enroll the student in the specified course.

## Database Migration

The application includes a migration script (`migration.py`) that ensures the database schema is updated to support the relationship between students and courses while preserving existing data. You can run this script to create the necessary tables if they do not already exist.

## Conclusion

This Student and Course Management System provides a straightforward interface for managing students and courses, making it easy to add, view, and enroll students in courses. For further customization or enhancements, feel free to modify the code as needed.
```