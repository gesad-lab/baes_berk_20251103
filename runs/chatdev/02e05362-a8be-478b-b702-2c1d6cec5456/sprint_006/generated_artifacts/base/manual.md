```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers.

## Main Functions

The Teacher Management System provides the following functionalities:

- **Student Management**: Add, view, and manage student information including names and emails.
- **Course Management**: Add, view, and manage courses including names and levels.
- **Teacher Management**: Add, view, and manage teachers including names and emails.

## Installation

To set up the Teacher Management System, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Ensure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   Run the following command to create the database and apply migrations:
   ```bash
   alembic upgrade head
   ```

## Usage

1. **Run the Application**:
   Start the application by running:
   ```bash
   python main.py
   ```

2. **Access the GUI**:
   The application will launch a graphical user interface (GUI) where you can manage students, courses, and teachers.

### Adding Students

- Enter the student's name and email in the respective fields.
- Click on the "Add Student" button to save the information.
- Use the "View Students" button to see the list of added students.

### Adding Courses

- Enter the course name and level in the respective fields.
- Click on the "Add Course" button to save the information.
- Use the "View Courses" button to see the list of added courses.

### Adding Teachers

- Enter the teacher's name and email in the respective fields.
- Click on the "Add Teacher" button to save the information.
- Use the "View Teachers" button to see the list of added teachers.

## Database Schema

The application uses a SQLite database with the following tables:

- **students**: Stores student information (id, name, email).
- **courses**: Stores course information (id, name, level).
- **teachers**: Stores teacher information (id, name, email).
- **student_courses**: A many-to-many relationship table linking students and courses.

## Additional Information

For any issues or feature requests, please contact the support team or create an issue in the repository.

Thank you for using the Teacher Management System!
```
