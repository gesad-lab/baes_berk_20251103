```markdown
# Student Management Application

Welcome to the Student Management Application! This software allows you to manage students and their course enrollments efficiently. You can create students, create courses, and enroll students in courses through a user-friendly interface.

## Main Functions

1. **Create Students**: Add new students to the system with their name and email.
2. **View Students**: Retrieve a list of all students in the system.
3. **Create Courses**: Add new courses with their name and level.
4. **View Courses**: Retrieve a list of all courses available in the system.
5. **Enroll Students in Courses**: Enroll a student in a specific course, establishing a relationship between them.

## Installation

To run the Student Management Application, you need to set up your environment with the required dependencies. Follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone https://github.com/your-repo/student-management-app.git
cd student-management-app
```

### Step 2: Install Dependencies

Install the required Python packages using pip:

```bash
pip install fastapi sqlalchemy alembic pydantic
```

### Step 3: Set Up the Database

The application uses SQLite as the database. The database will be created automatically when you run the application for the first time.

### Step 4: Run the Application

You can run the application using the following command:

```bash
python main.py
```

This will start the GUI for the Student Management Application.

## How to Use the Application

1. **Creating a Student**:
   - Navigate to the "Create Student" section in the GUI.
   - Enter the student's name and email.
   - Click the "Create" button to add the student.

2. **Viewing Students**:
   - Navigate to the "View Students" section.
   - You will see a list of all students with their names and emails.

3. **Creating a Course**:
   - Navigate to the "Create Course" section.
   - Enter the course name and level.
   - Click the "Create" button to add the course.

4. **Viewing Courses**:
   - Navigate to the "View Courses" section.
   - You will see a list of all courses with their names and levels.

5. **Enrolling a Student in a Course**:
   - Navigate to the "Enroll Student in Course" section.
   - Select a student and a course from the dropdown menus.
   - Click the "Enroll" button to enroll the student in the selected course.

## Database Migration

The application uses Alembic for database migrations. When you run the application for the first time, it will automatically create the necessary database tables. If you make changes to the database schema, you can run the following command to apply migrations:

```bash
python alembic_migration.py
```

## Support

If you encounter any issues or have questions, please reach out to our support team at support@chatdev.com.

Thank you for using the Student Management Application!
```