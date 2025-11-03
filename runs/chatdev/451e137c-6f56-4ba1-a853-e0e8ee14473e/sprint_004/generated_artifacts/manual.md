```markdown
# Student and Course Management Application

A simple application for managing students and their associated courses. This application allows users to add students, add courses, and view the list of students along with their courses.

## Main Functions

- **Add Student**: Allows users to input a student's name and email to create a new student record.
- **Add Course**: Enables users to input a course name and level to create a new course record.
- **Display Students**: Retrieves and displays a list of all students along with their email addresses.

## Installation Guide

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

4. **Run the Application**:
   Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the GUI**:
   The GUI will open automatically. If it does not, you can run the `gui.py` script:
   ```bash
   python gui.py
   ```

## How to Use the Application

1. **Adding a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to create the student record.

2. **Adding a Course**:
   - Enter the course name in the "Enter Course Name" field.
   - Enter the course level in the "Enter Course Level" field.
   - Click the "Add Course" button to create the course record.

3. **Displaying Students**:
   - Click the "Display Students" button to retrieve and display the list of all students along with their email addresses in the output area.

## Database Migration

The application includes migration scripts to ensure that the database schema is updated without losing existing data. The migration scripts handle the creation of the `Course` table and the association table `student_courses` for the many-to-many relationship between students and courses.

## Additional Information

For further details on the API endpoints, refer to the FastAPI documentation available at [FastAPI Documentation](https://fastapi.tiangolo.com/).

For any issues or feature requests, please reach out to the development team.

Happy managing!
```