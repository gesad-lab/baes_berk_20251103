```markdown
# Course Management Application

A comprehensive application for managing courses and teachers, allowing users to create and view courses and teachers seamlessly.

## Main Functions

- **Create Teacher**: Allows users to add new teachers to the system.
- **Create Course**: Enables users to create new courses and associate them with existing teachers.
- **View Courses**: Displays a list of all courses along with their associated teacher IDs.

## Installation Guide

To set up the Course Management Application, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Required Dependencies

Install the required dependencies using pip:

```bash
pip install fastapi sqlalchemy alembic requests tkinter
```

### Step 4: Run Database Migrations

Before running the application, ensure the database schema is up to date. Run the migrations:

```bash
python -m alembic upgrade head
```

### Step 5: Start the Application

Run the application using the following command:

```bash
python main.py
```

## How to Use the Application

### Creating a Teacher

1. Enter the teacher's name in the "Teacher Name" field.
2. Enter the teacher's email in the "Teacher Email" field.
3. Click the "Create Teacher" button.
4. A success message will appear if the teacher is created successfully.

### Creating a Course

1. Enter the course name in the "Course Name" field.
2. Enter the course level in the "Course Level" field.
3. Enter the associated teacher's ID in the "Teacher ID" field.
4. Click the "Create Course" button.
5. A success message will appear if the course is created successfully.

### Viewing Courses

1. Click the "View Courses" button.
2. A list of all courses will be displayed, showing the course name, level, and associated teacher ID.

## Additional Information

For further documentation and examples, please refer to the code comments within the application files. If you encounter any issues or have questions, feel free to reach out for support.

Happy Course Management!
```