```markdown
# Student Management Application

A comprehensive application for managing students, courses, and teachers in an educational environment.

## Main Functions

The Student Management Application allows users to:

- **Add Students**: Create new student profiles with names and email addresses.
- **Add Teachers**: Create new teacher profiles with names and email addresses.
- **Add Courses**: Create new courses that can be associated with teachers and students.
- **Manage Relationships**: Establish relationships between courses and teachers, as well as between students and courses.

## Installation

To set up the Student Management Application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student_management_app.git
   cd student_management_app
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**:
   Ensure you have Python 3.7 or higher installed. Then, install the necessary packages using pip:
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
   tkinter
   ```

4. **Initialize the Database**:
   Run the following command to create the database and tables:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

## How to Use the Application

1. **Run the Application**:
   Start the application by executing:
   ```bash
   python main.py
   ```

2. **User Interface**:
   The application will open a graphical user interface (GUI) where you can perform the following actions:

   - **Add Student**:
     - Enter the student's name and email.
     - Click the "Add Student" button to save the student.

   - **Add Teacher**:
     - Enter the teacher's name and email.
     - Click the "Add Teacher" button to save the teacher.

   - **Add Course**:
     - Enter the course name and level.
     - Enter the teacher's name and email (if the teacher does not exist, the application will create a new teacher).
     - Click the "Add Course" button to save the course.

3. **Data Persistence**:
   The application uses SQLite as the database, ensuring that all data (students, teachers, and courses) is preserved even after the application is closed.

## Additional Information

- **Database Migration**: The application includes a migration script to add the teacher relationship to the course entity without losing existing data.
- **Error Handling**: The application provides user-friendly error messages for failed operations, ensuring a smooth user experience.

For any issues or feature requests, please reach out to the development team.

Happy managing!
```