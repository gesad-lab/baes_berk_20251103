```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows users to manage students, courses, and teachers efficiently. You can register students, create courses, and assign teachers to courses through a user-friendly graphical interface.

## Main Functions

- **Student Registration**: Register new students by providing their name, email, and the courses they wish to enroll in.
- **Course Creation**: Create new courses by specifying the course name, level, and assigning a teacher.
- **Teacher Registration**: Register new teachers by providing their name and email.

## Installation Guide

To set up the ChatDev Course Management System, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-repo/chatdev-course-management.git
cd chatdev-course-management
```

### Step 2: Create a Virtual Environment

It's recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install fastapi sqlalchemy alembic requests
```

### Step 4: Initialize the Database

Before running the application, initialize the database by running the following command:

```bash
python -m database
```

This will create the necessary database schema and tables.

## How to Use the Application

### Running the Application

To run the FastAPI application and the Tkinter GUI, execute the following command:

```bash
python main.py
```

### Using the GUI

1. **Student Registration**:
   - Enter the student's name and email.
   - Provide the course IDs (comma-separated) for the courses the student wishes to enroll in.
   - Click on the "Submit Student" button to register the student.

2. **Course Creation**:
   - Enter the course name and level.
   - Specify the teacher ID to assign a teacher to the course.
   - Click on the "Submit Course" button to create the course.

3. **Teacher Registration**:
   - Enter the teacher's name and email.
   - Click on the "Submit Teacher" button to register the teacher.

### Example Usage

- To register a student named "John Doe" with email "john@example.com" for courses with IDs 1 and 2, fill in the respective fields and click "Submit Student".
- To create a course named "Mathematics" at level "Beginner" and assign a teacher with ID 1, fill in the course details and click "Submit Course".
- To register a teacher named "Jane Smith" with email "jane@example.com", fill in the teacher details and click "Submit Teacher".

## Conclusion

The ChatDev Course Management System provides a comprehensive solution for managing students, courses, and teachers. With its intuitive interface and robust backend, users can efficiently handle educational administration tasks.

For further assistance or feature requests, please contact our support team.
```