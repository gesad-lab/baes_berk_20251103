```markdown
# Student and Course Management System

A simple API and GUI application for managing students and their courses.

## Main Functions

This software allows users to perform the following operations:

1. **Create Students**: Add new students to the system with their name and email.
2. **Create Courses**: Add new courses with a name and level.
3. **Enroll Students in Courses**: Enroll existing students in courses, allowing them to have multiple courses associated with them.
4. **View Student Information**: Retrieve information about a student, including the courses they are enrolled in.

## Installation

To set up the environment and run the application, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository containing the code:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

Install the required Python packages using pip:

```bash
pip install fastapi sqlalchemy uvicorn requests
```

### Step 3: Initialize the Database

Run the following command to initialize the database:

```bash
python -c "from database import init_db; init_db()"
```

## Running the Application

### Step 1: Start the FastAPI Server

Run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### Step 2: Launch the GUI

You can run the GUI application by executing:

```bash
python gui.py
```

This will open a simple Tkinter window where you can interact with the API.

## How to Use the Application

### Creating a Student

1. Enter the student's name and email in the respective fields.
2. Click the "Create Student" button.
3. A confirmation message will appear if the student is created successfully.

### Creating a Course

1. Enter the course name and level in the respective fields.
2. Click the "Create Course" button.
3. A confirmation message will appear if the course is created successfully.

### Enrolling a Student in a Course

1. Enter the student ID of the student you want to enroll.
2. Enter the course name and level in the respective fields.
3. Click the "Enroll in Course" button.
4. A confirmation message will appear if the student is enrolled successfully.

### Viewing Student Information

To view a student's information, you can use the GET endpoint `/students/{student_id}` via a tool like Postman or directly from the browser.

## API Endpoints

- **POST /students/**: Create a new student.
- **GET /students/{student_id}**: Retrieve a student's information.
- **POST /courses/**: Create a new course.
- **POST /students/{student_id}/courses/**: Enroll a student in a course.

## Conclusion

This application provides a straightforward way to manage students and their courses. You can extend its functionality by adding more features as needed. For any issues or feature requests, please reach out to the development team.
```