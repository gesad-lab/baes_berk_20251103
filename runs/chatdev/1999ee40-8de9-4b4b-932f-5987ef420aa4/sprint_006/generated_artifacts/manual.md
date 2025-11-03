```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage courses, students, and teachers effectively. With the recent updates, you can now establish relationships between courses and teachers, enhancing the functionality of the application.

## Main Functions

- **Manage Courses**: Create, read, update, and delete courses.
- **Manage Students**: Create, read, update, and delete student records.
- **Manage Teachers**: Create, read, update, and delete teacher records.
- **Course-Teacher Relationship**: Each course can now have an associated teacher, allowing for better organization and management of educational resources.

## Installation

To get started with the ChatDev Course Management System, you'll need to install the necessary environment dependencies. Follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   sqlalchemy
   pydantic
   ```

4. **Initialize the Database**:
   Run the following command to create the necessary database tables:
   ```bash
   python main.py
   ```

## How to Use

### Starting the Application

1. **Run the Application**:
   Start the application by executing:
   ```bash
   python gui.py
   ```

### Managing Entities

- **Adding a Teacher**:
  - Use the GUI to input teacher details (name and email).
  
- **Adding a Course**:
  - Input course details (name, level) and select a teacher from the dropdown list to associate with the course.

- **Adding a Student**:
  - Input student details (name and email) and assign courses as needed.

### Viewing Relationships

- Each course will display its associated teacher, and each teacher can be linked to multiple courses.
- You can view all students enrolled in a course and all courses taught by a teacher.

## Database Migration

The database schema has been updated to include the new relationship between courses and teachers. Existing data for students, courses, and teachers will be preserved during migration.

### Upgrade and Downgrade Functions

- The `upgrade()` function in `main.py` creates the necessary tables and relationships.
- The `downgrade()` function is currently not implemented due to SQLite limitations on dropping columns.

## Documentation

For more detailed documentation and examples, please refer to the following resources:

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

If you have any questions or need further assistance, feel free to reach out to our support team!

Happy coding!
```