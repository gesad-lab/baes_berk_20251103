```markdown
# Student Management Application

A comprehensive application for managing students and their courses, built using Python and Tkinter for the GUI, and SQLAlchemy for database interactions.

## Main Functions

The Student Management Application allows users to:

- **Add Students**: Input student names and emails to create new student records.
- **Fetch Students**: Retrieve and display a list of all registered students.
- **Add Courses**: Associate courses with students by inputting course names and levels.
- **Manage Relationships**: Each student can have multiple courses, establishing a one-to-many relationship between students and courses.

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

3. **Install Required Packages**:
   Ensure you have `pip` installed, then run:
   ```bash
   pip install sqlalchemy alembic requests tkinter
   ```

4. **Set Up the Database**:
   The application uses SQLite for the database. The database will be initialized automatically when you run the application for the first time.

## How to Use the Application

1. **Run the Application**:
   Start the application by executing the following command:
   ```bash
   python main.py
   ```

2. **Adding a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to save the student record.

3. **Fetching Students**:
   - Click the "Fetch Students" button to retrieve and display all registered students in the list box.

4. **Adding a Course**:
   - Enter the course name in the "Course Name" field.
   - Enter the course level in the "Course Level" field.
   - Select a student from the list box.
   - Click the "Add Course" button to associate the course with the selected student.

5. **Viewing Relationships**:
   - The application maintains a relationship where each student can have multiple courses. This relationship is managed through the database schema.

## Additional Information

- The application uses SQLAlchemy for ORM and Alembic for database migrations, ensuring that existing data is preserved during schema updates.
- The GUI is built using Tkinter, providing a user-friendly interface for managing student and course data.

For further assistance or to report issues, please contact the support team.
```
