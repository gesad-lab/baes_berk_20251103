```markdown
# Student Course Management System

A simple application for managing students and courses, allowing users to add students, courses, and associate them with each other.

## Main Functions

- **Add Student**: Allows users to input student details (name and email) and add them to the database.
- **Add Course**: Enables users to input course details (name and level) and add them to the database.
- **Associate Students with Courses**: Students can be associated with multiple courses, and courses can have multiple students.

## Installation

To run the application, you need to set up your environment and install the required dependencies. Follow the steps below:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/student-course-management.git
cd student-course-management
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment for your project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

Make sure to include the following dependencies in your `requirements.txt` file:

```
fastapi
uvicorn
sqlalchemy
pydantic
alembic
requests
tkinter  # Note: Tkinter is included with Python installations on most systems
```

### Step 4: Run Database Migrations

Before running the application, you need to set up the database schema. Run the migration scripts to create the necessary tables:

```bash
alembic upgrade head
```

## Usage

### Step 1: Start the Application

Run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### Step 2: Open the GUI

The application provides a simple GUI using Tkinter. Run the GUI script:

```bash
python main.py
```

### Step 3: Add Students and Courses

1. **Adding a Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to save the student to the database.

2. **Adding a Course**:
   - Enter the course name and level in the respective fields.
   - Click the "Add Course" button to save the course to the database.

### Step 4: Associate Students with Courses

To associate students with courses, you can extend the functionality in the GUI or use the API endpoints provided by FastAPI.

## API Documentation

You can access the automatically generated API documentation at `http://127.0.0.1:8000/docs` to explore the endpoints for adding students, courses, and managing relationships.

## Conclusion

This application provides a simple yet effective way to manage students and courses. Feel free to extend its functionality or integrate it with other systems as needed.
```