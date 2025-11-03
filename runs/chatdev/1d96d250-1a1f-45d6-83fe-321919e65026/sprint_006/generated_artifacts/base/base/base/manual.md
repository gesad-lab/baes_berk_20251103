```markdown
# Student Management Application

A simple application for managing students and courses, allowing users to add student information and course details.

## Main Functions

- **Add Student**: Users can input student names and emails to create new student records.
- **Add Course**: Users can input course names and levels to create new course records.
- **Database Management**: The application maintains a database of students and courses, ensuring data integrity and easy access.

## Installation

To run the Student Management Application, you need to set up the environment and install the necessary dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student-management-app.git
   cd student-management-app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure you have `pip` installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should include:
   ```
   fastapi
   sqlalchemy
   alembic
   requests
   pydantic
   ```

4. **Initialize the Database**:
   Run the following command to create the necessary database tables:
   ```bash
   python -m database
   ```

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI server by running:
   ```bash
   uvicorn main:app --reload
   ```

2. **Open the GUI**:
   The application will open a graphical user interface (GUI) using Tkinter. You can add students and courses through this interface.

3. **Adding a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to save the student information.

4. **Adding a Course**:
   - Enter the course name in the "Enter Course Name" field.
   - Enter the course level in the "Enter Course Level" field.
   - Click the "Add Course" button to save the course information.

5. **Database Migration**:
   The application includes a migration script to add the courses table while preserving existing student data. Ensure to run the migration script whenever you update the database schema.

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file is named `students.db` and is located in the project directory.
- **Error Handling**: The application provides basic error handling for network requests and user input validation.

For further assistance or to report issues, please contact the development team.
```
