```markdown
# Teacher Management System

A simple application for managing teachers and courses using a GUI interface and a RESTful API.

## Main Functions

- **Create Teacher**: Allows users to add a new teacher with a name and email.
- **View Teachers**: Displays a list of all teachers in the system.
- **Create Course**: Enables users to create new courses with a name and level.
- **View Courses**: Shows a list of all courses available in the system.

## Installation

To set up the environment and run the application, follow these steps:

### Prerequisites

Make sure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone https://github.com/yourusername/teacher-management-system.git
cd teacher-management-system
```

### Step 2: Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install fastapi sqlalchemy alembic requests
```

### Step 4: Run Database Migrations

Before running the application, ensure that the database schema is up to date:

```bash
python -m alembic upgrade head
```

### Step 5: Start the Application

Run the application using the following command:

```bash
python main.py
```

The GUI will open, allowing you to interact with the application.

## How to Use the Application

### Creating a Teacher

1. In the GUI, locate the "Teacher Name" and "Teacher Email" fields.
2. Enter the required information.
3. Click the "Create Teacher" button.
4. A success message will appear if the teacher is created successfully.

### Viewing Teachers

1. Click on the "View Teachers" button to display a list of all teachers.
2. The list will show the names and emails of the teachers.

### Creating a Course

1. Fill in the "Course Name" and "Course Level" fields.
2. Click the "Create Course" button to add the course.
3. A success message will confirm the course creation.

### Viewing Courses

1. Click on the "View Courses" button to see all available courses.
2. The list will display the names and levels of the courses.

## Conclusion

This application provides a straightforward way to manage teachers and courses. For further enhancements or support, feel free to reach out to the development team.
```
