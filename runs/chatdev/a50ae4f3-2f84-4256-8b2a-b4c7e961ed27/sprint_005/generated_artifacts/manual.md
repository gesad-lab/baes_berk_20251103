Here's the `manual.md` file that provides a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers using a graphical user interface (GUI) and a RESTful API.

## Main Functions

The Teacher Management System allows users to perform the following operations:

- **Student Management**: Create and view students with their names and emails.
- **Course Management**: Create and view courses with their names and levels.
- **Teacher Management**: Create and view teachers with their names and emails.
- **Course Enrollment**: Enroll students in courses and view their enrolled courses.

## Installation

To set up the environment and run the application, follow these steps:

### Prerequisites

Make sure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd <repository-directory>
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

### Step 4: Run Database Migration

Before running the application, apply the database migration to create the necessary tables:

```bash
alembic upgrade head
```

### Step 5: Start the Application

Run the FastAPI application:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## How to Use the Application

1. **Access the GUI**: Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

2. **Manage Students**:
   - To create a new student, enter the student's name and email in the respective fields and click "Create Student".
   - To view existing students, click "Get Students".

3. **Manage Courses**:
   - To create a new course, enter the course name and level in the respective fields and click "Create Course".
   - To view existing courses, click "Get Courses".

4. **Manage Teachers**:
   - To create a new teacher, enter the teacher's name and email in the respective fields and click "Create Teacher".
   - To view existing teachers, click "Get Teachers".

5. **Enroll Students in Courses**:
   - To enroll a student in a course, use the appropriate API endpoint to add a course to a student.

## Additional Information

For more detailed documentation on the API endpoints, please refer to the interactive API documentation available at `http://127.0.0.1:8000/docs`.

## Support

If you encounter any issues or have questions, please reach out to our support team at [support@chatdev.com](mailto:support@chatdev.com).

```

This manual provides a comprehensive overview of the application, installation steps, and usage instructions, ensuring that users can effectively utilize the Teacher Management System.