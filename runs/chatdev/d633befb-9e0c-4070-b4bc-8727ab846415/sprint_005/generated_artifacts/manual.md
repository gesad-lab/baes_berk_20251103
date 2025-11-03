```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers using FastAPI and a SQLite database.

## Main Functions

The Teacher Management System allows users to:

- **Add Students**: Create new student records with a name and email.
- **Add Courses**: Create new course records with a name and level.
- **Add Teachers**: Create new teacher records with a name and email.
- **Enroll Students in Courses**: Link students to courses they are enrolled in.

## Installation

To set up the environment and run the application, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone https://github.com/your-repo/teacher-management-system.git
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
pip install fastapi[all] sqlalchemy alembic requests
```

### Step 4: Run Database Migrations

Before running the application, you need to create the database schema. Run the following command to create the Teacher table while preserving existing Student and Course data:

```bash
alembic revision --autogenerate -m "Add Teacher table"
alembic upgrade head
```

### Step 5: Start the Application

Run the FastAPI application:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## How to Use the Application

### Accessing the GUI

1. Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.
2. You can also use the GUI implemented with Tkinter by running the `gui.py` file:

```bash
python gui.py
```

### Adding a Teacher

1. In the GUI, navigate to the "Teacher" section.
2. Enter the Teacher's name and email in the respective fields.
3. Click the "Add Teacher" button.
4. A success message will appear if the teacher was added successfully.

### Adding a Student or Course

Follow similar steps in their respective sections to add students or courses.

### Enrolling Students in Courses

1. Enter the Student ID and Course ID in the Enrollment section.
2. Click the "Enroll" button to enroll the student in the selected course.

## Conclusion

This Teacher Management System provides a straightforward way to manage educational entities. You can extend its functionality by adding more features as needed. For further assistance, please refer to the FastAPI documentation or reach out for support.

```
