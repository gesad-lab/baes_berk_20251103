Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management System

A simple application for managing students and courses.

## Overview

This software allows users to create and manage student records and course entities. It provides functionalities to add students, create courses, and retrieve existing records. The application is built using Python and utilizes FastAPI for the backend and Tkinter for the GUI.

## Main Functions

- **Create Student**: Add a new student with a name and email.
- **Create Course**: Add a new course with a name and level.
- **Retrieve Students**: Fetch a list of all students.
- **Retrieve Courses**: Fetch a list of all courses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic pydantic
   ```

4. **Install Tkinter** (if not already installed):
   - For Windows, Tkinter is included with Python installations.
   - For Ubuntu, you can install it using:
     ```bash
     sudo apt-get install python3-tk
     ```

## Database Setup

1. **Database Configuration**: The application uses SQLite for the database. The database file will be created automatically when the application runs for the first time.

2. **Run Migrations**: To create the necessary database tables, run the migration script:
   ```bash
   alembic upgrade head
   ```

## Usage

### Running the Application

1. **Start the FastAPI Server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Open the GUI**:
   - The GUI will launch automatically, allowing you to interact with the application.

### Creating a Student

1. Enter the student's name in the "Enter Student Name" field.
2. Enter the student's email in the "Enter Student Email" field.
3. Click the "Submit" button to add the student.

### Creating a Course

*Note: The GUI currently does not have a direct interface for creating courses. This functionality can be added in future enhancements.*

### Retrieving Records

- The application allows for the retrieval of student and course records through the backend API. You can access the API documentation at `http://127.0.0.1:8000/docs` after starting the server.

## Future Enhancements

- Implement a GUI for creating and managing courses.
- Add validation and error handling for user inputs.
- Expand the functionality to include editing and deleting records.

## Support

For any issues or feature requests, please reach out to the development team or create an issue in the repository.

```

This manual provides a comprehensive guide for users to understand the software, install the necessary dependencies, and utilize its features effectively.