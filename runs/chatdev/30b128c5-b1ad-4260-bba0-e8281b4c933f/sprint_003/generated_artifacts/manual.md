```markdown
# Student Management Application

A simple GUI application for managing student records and courses.

## Main Functions

The Student Management Application allows users to:

- Add new students with their name and email.
- Fetch and display the list of existing students.
- Create and manage courses with their name and level.

## Installation

To run the Student Management Application, you need to install the required dependencies. Follow these steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install sqlalchemy alembic requests tkinter
   ```

4. **Set up the database**:
   - Ensure that the SQLite database file (`students.db`) is created in the project directory. The application will automatically create the necessary tables upon running.

## How to Use the Application

1. **Run the Application**:
   Start the application by running the `main.py` file:
   ```bash
   python main.py
   ```

2. **Adding a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to add the student to the database.
   - If the email format is invalid, an error message will be displayed.

3. **Fetching Students**:
   - Click the "Fetch Students" button to retrieve and display the list of students from the database.
   - The list will show each student's ID, name, and email.

4. **Creating a Course**:
   - To create a course, you will need to modify the code to include a GUI for course management (not currently implemented).
   - The `Course` entity is defined in `models.py` and can be used in conjunction with the database migration script in `database.py`.

## Database Migration

The application uses Alembic for database migrations. To add the `Course` table while preserving existing student data, run the migration script as follows:

1. **Initialize Alembic** (if not already done):
   ```bash
   alembic init alembic
   ```

2. **Edit the `alembic.ini` file** to point to your database:
   ```ini
   sqlalchemy.url = sqlite:///./students.db
   ```

3. **Run the migration**:
   ```bash
   alembic upgrade head
   ```

This will create the `courses` table in the database without affecting the existing `students` table.

## Conclusion

The Student Management Application provides a simple interface for managing student records and courses. Future enhancements may include a GUI for course management and additional features for better user experience. For any issues or feature requests, please contact the development team.
```