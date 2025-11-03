```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers effectively. Below is a detailed user manual that introduces the main functions of the software, guides you through installing the necessary environment dependencies, and explains how to use the application.

## Main Functions

The ChatDev Course Management System provides the following key functionalities:

- **Manage Students**: Create, read, update, and delete student records.
- **Manage Courses**: Create, read, update, and delete course records.
- **Manage Teachers**: Create, read, update, and delete teacher records.
- **Enroll Students in Courses**: Associate students with courses they are enrolled in.
- **Assign Teachers to Courses**: Establish a relationship between courses and teachers.

## Quick Install

To set up the ChatDev Course Management System, you need to install the required dependencies. You can do this using pip. Open your terminal and run:

```bash
pip install sqlalchemy alembic pydantic
```

If you are using Anaconda, you can install the dependencies with:

```bash
conda install sqlalchemy alembic pydantic -c conda-forge
```

## Setting Up the Environment

1. **Clone the Repository**: Start by cloning the repository containing the source code.

   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
   ```

2. **Run Database Migration**: After installing the dependencies, you need to run the database migration to set up the initial database schema.

   ```bash
   python alembic_upgrade.py
   ```

3. **Create the Database**: Ensure that the database and tables are created by running the following command:

   ```bash
   python database.py
   ```

## How to Use the Application

1. **Starting the Application**: You can start the application by running the main entry point.

   ```bash
   python main.py
   ```

2. **Using the Graphical User Interface**: The application provides a GUI for easy interaction. You can perform the following actions:

   - **Add a Student**: Fill in the required fields (name and email) to create a new student.
   - **Add a Course**: Specify the course name, level, and assign a teacher by selecting from the available teachers.
   - **Add a Teacher**: Enter the teacher's name and email to create a new teacher record.
   - **Enroll Students in Courses**: Select a student and a course to enroll the student in that course.
   - **Assign Teachers to Courses**: When creating or updating a course, you can assign a teacher to that course.

3. **Database Management**: The application uses SQLite for database management. You can access the `students.db` file to view the data directly if needed.

## Additional Resources

For more detailed documentation on specific functionalities, please refer to the following sections:

- **Getting Started**: [Installation and Setup](https://your-docs-link.com/getting-started)
- **How-To Examples**: [Demos and Integrations](https://your-docs-link.com/how-to)
- **API Reference**: [Full API Documentation](https://your-docs-link.com/api)
- **Core Concepts**: [Understanding the Application](https://your-docs-link.com/resources)

Thank you for using the ChatDev Course Management System! We hope you find it helpful in managing your educational needs.
```