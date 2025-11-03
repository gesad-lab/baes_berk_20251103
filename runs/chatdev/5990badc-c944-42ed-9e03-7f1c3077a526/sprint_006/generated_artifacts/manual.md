```markdown
# Student Application

A comprehensive application for managing students, courses, and teachers, allowing users to create and manage educational entities seamlessly.

## Main Functions

- **Create Students**: Add new students to the database with their names and email addresses.
- **Create Teachers**: Add new teachers to the database with their names and email addresses.
- **Create Courses**: Add new courses to the database, associating them with teachers and allowing students to enroll.
- **Manage Relationships**: Establish relationships between courses and teachers, ensuring that each course can have a designated teacher.

## Installation

To set up the environment and run the application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-application.git
   cd student-application
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

   If you don't have a `requirements.txt`, you may need to install the following packages manually:
   ```bash
   pip install sqlalchemy tkinter pydantic
   ```

## How to Use the Application

1. **Run the Application**:
   Start the application by executing the following command:
   ```bash
   python main.py
   ```

2. **User Interface**:
   The application will launch a graphical user interface (GUI) where you can perform the following actions:

   - **Add a Student**:
     - Enter the student's name and email address in the respective fields.
     - Click on the "Add Student" button to save the student.

   - **Add a Teacher**:
     - Enter the teacher's name and email address in the respective fields.
     - Click on the "Add Teacher" button to save the teacher.

   - **Add a Course**:
     - Enter the course name and level in the respective fields.
     - Enter the Teacher ID associated with the course.
     - Click on the "Add Course" button to save the course.

3. **Database Migration**:
   The application includes a database migration feature that ensures existing data for students, courses, and teachers is preserved when the application is run for the first time. The `upgrade_database` function handles this automatically.

## Additional Information

- **Database**: The application uses SQLite for data storage, and the database file will be created in the project directory as `students.db`.
- **Data Models**: The application is built using SQLAlchemy ORM for managing database interactions, with models defined for `Student`, `Teacher`, and `Course`.

## Support

For any issues or feature requests, please reach out to the development team via the project's GitHub repository or contact support at support@yourcompany.com.

Happy Learning!
```
