```markdown
# Student Management System

Welcome to the Student Management System, a comprehensive application designed to manage students and courses effectively. This software allows users to create students, create courses, and enroll students in courses seamlessly.

## Main Functions

1. **Create Student**: Add new students to the system by providing their name and email.
2. **Create Course**: Add new courses by specifying the course name and level.
3. **Enroll Student in Course**: Enroll existing students in specific courses using their IDs.

## Installation Guide

To get started with the Student Management System, you need to set up your environment and install the necessary dependencies.

### Prerequisites

- Python 3.7 or higher
- SQLite (comes pre-installed with Python)

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/student_management_system.git
cd student_management_system
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment for your project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Required Dependencies

Install the required Python packages using pip:

```bash
pip install fastapi[all] sqlalchemy alembic requests
```

### Step 4: Initialize the Database

Run the following command to create the database and tables:

```bash
python -c "from database import init_db; init_db()"
```

## How to Use the Application

### Running the Application

To start the FastAPI server, run the following command:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

### Using the GUI

1. **Add Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to create a new student.

2. **Add Course**:
   - Enter the course name and level in the respective fields.
   - Click the "Add Course" button to create a new course.

3. **Enroll Student in Course**:
   - Enter the Student ID and Course ID in the respective fields.
   - Click the "Enroll Student in Course" button to enroll the student in the specified course.

### Example Usage

- To add a student named "John Doe" with the email "john.doe@example.com", fill in the fields and click "Add Student".
- To create a course named "Mathematics" at the "Intermediate" level, fill in the course details and click "Add Course".
- To enroll the student with ID 1 in the course with ID 1, enter the IDs and click "Enroll Student in Course".

## Conclusion

The Student Management System provides a user-friendly interface for managing students and courses. With the ability to create and enroll students in courses, this application simplifies the educational management process. For further assistance, please refer to the documentation or contact support.

Happy managing!
```