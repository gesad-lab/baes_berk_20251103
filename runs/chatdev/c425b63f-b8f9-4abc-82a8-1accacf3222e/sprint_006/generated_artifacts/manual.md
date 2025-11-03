```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System, a powerful application designed to manage students, courses, and teachers efficiently. This software allows you to create and manage courses, assign teachers, and enroll students seamlessly.

## Main Functions

- **Course Management**: Create, update, and delete courses. Each course can be associated with a teacher.
- **Teacher Management**: Add and manage teacher information, including their name and email.
- **Student Management**: Enroll students in courses and manage their information, including their email and associated courses.

## Quick Install

To get started with the ChatDev Course Management System, you need to install the required dependencies. You can do this using `pip` or `conda`.

### Using pip

```bash
pip install -r requirements.txt
```

### Using conda

```bash
conda install --file requirements.txt
```

## Environment Setup

1. **Clone the Repository**: Start by cloning the repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/chatdev-course-management.git
   cd chatdev-course-management
   ```

2. **Install Dependencies**: Use one of the methods mentioned above to install the necessary dependencies.

3. **Database Setup**: The application uses SQLite for database management. The database schema will be created automatically on startup. Ensure that you have the necessary permissions to create files in the project directory.

## How to Use the Application

1. **Run the Application**: Start the application by running the `main.py` file.

   ```bash
   python main.py
   ```

2. **Access the Dashboard**: Once the application is running, you can access the dashboard through your web browser. The default URL is `http://localhost:8000`.

3. **Managing Courses**:
   - **Create a Course**: Fill in the course name, level, and select a teacher from the dropdown list.
   - **Update a Course**: Select a course from the list, make the necessary changes, and save.
   - **Delete a Course**: Select a course and click the delete button.

4. **Managing Teachers**:
   - **Add a Teacher**: Enter the teacher's name and email, then save.
   - **Update Teacher Information**: Select a teacher and update their details.
   - **Delete a Teacher**: Select a teacher and click the delete button.

5. **Managing Students**:
   - **Enroll a Student**: Enter the student's name and email, and select the courses they will be enrolled in.
   - **Update Student Information**: Select a student and update their details.
   - **Delete a Student**: Select a student and click the delete button.

## Database Migration

The application includes migration scripts to manage database changes. When you add or modify entities, ensure to run the migration scripts to update the database schema without losing existing data.

### Running Migrations

To run the migrations, use the following command:

```bash
alembic upgrade head
```

This command will apply all pending migrations to the database.

## Conclusion

The ChatDev Course Management System is designed to simplify the management of courses, teachers, and students. With its user-friendly interface and robust backend, you can efficiently manage educational resources. For further assistance, please refer to the documentation or contact support.

Happy Learning!
```