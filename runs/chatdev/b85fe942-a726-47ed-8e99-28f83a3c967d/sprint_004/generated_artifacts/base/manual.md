```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows users to manage student registrations and course creations seamlessly through a user-friendly interface. 

## Main Functions

1. **Student Registration**: Users can register new students by providing their name and email address.
2. **Course Creation**: Users can create new courses by specifying the course name and level.
3. **Database Management**: The system maintains a database of students and courses, ensuring data integrity and easy access.

## Installation Guide

To set up the ChatDev Course Management System, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-repo/chatdev-course-management.git
cd chatdev-course-management
```

### Step 2: Install Dependencies

Install the required Python packages using pip. You can do this by running:

```bash
pip install fastapi sqlalchemy alembic requests tkinter
```

### Step 3: Set Up the Database

The application uses SQLite as the database. The database schema will be created automatically when you run the application for the first time.

### Step 4: Run the Application

To start the FastAPI application and the Tkinter GUI, execute the following command:

```bash
python main.py
```

The application will be accessible at `http://127.0.0.1:8000`, and the GUI will pop up for user interaction.

## How to Use the Application

### Student Registration

1. Open the application.
2. Enter the student's name in the "Enter Student Name" field.
3. Enter the student's email in the "Enter Student Email" field.
4. Click the "Submit Student" button to register the student.
5. A success message will appear if the registration is successful.

### Course Creation

1. In the same application window, enter the course name in the "Enter Course Name" field.
2. Enter the course level in the "Enter Course Level" field.
3. Click the "Submit Course" button to create the course.
4. A success message will appear if the course creation is successful.

## Additional Information

- The application uses FastAPI for the backend and Tkinter for the graphical user interface.
- The database is managed using SQLAlchemy and Alembic for migrations.
- Ensure that the application is running before attempting to register students or create courses.

For further assistance or support, please contact the ChatDev support team.

Happy coding!
```