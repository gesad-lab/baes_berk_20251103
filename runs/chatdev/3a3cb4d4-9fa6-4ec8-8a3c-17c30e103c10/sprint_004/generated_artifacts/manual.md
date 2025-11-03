Here's a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Student Management System

A simple application for managing students and their course enrollments.

## Overview

The Student Management System allows users to manage student information and their associated courses. Users can add students, view their details, and enroll them in various courses. This application is built using Python and utilizes FastAPI for the backend and Tkinter for the GUI.

## Main Functions

- **Add Student**: Users can input a student's name and email to add them to the system.
- **Course Management**: The system supports a many-to-many relationship between students and courses, allowing students to enroll in multiple courses.
- **Data Persistence**: All student and course data is stored in a SQLite database, ensuring data is preserved across sessions.

## Installation Instructions

To set up the environment and run the application, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

Install the required Python packages using pip. You can create a virtual environment for better dependency management:

```bash
# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install fastapi[all] sqlalchemy pydantic requests
```

### Step 3: Run Database Migrations

Before running the application, ensure that the database schema is set up correctly. Run the migration script to create the necessary tables:

```bash
python migration.py
```

### Step 4: Start the Application

Run the FastAPI application using the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### Step 5: Launch the GUI

To interact with the application through the GUI, run the following command in a separate terminal:

```bash
python gui.py
```

## How to Use the Application

1. **Add a Student**:
   - Open the GUI application.
   - Enter the student's name and email in the provided fields.
   - Click the "Add Student" button to submit the information.

2. **View Student Information**:
   - Currently, the GUI does not support viewing student information directly. This feature can be added in future iterations.

3. **Enroll in Courses**:
   - The current version does not include a GUI for course management. This functionality can be implemented in future updates.

## Future Enhancements

- Implement a feature to view and manage courses.
- Add functionality to enroll students in courses through the GUI.
- Enhance error handling and user feedback in the GUI.

## Conclusion

The Student Management System provides a foundational platform for managing student data and course enrollments. With further enhancements, it can evolve into a comprehensive educational management tool.

For any issues or feature requests, please reach out to the development team.

```

This manual provides a comprehensive overview of the software, installation steps, and usage instructions, ensuring users can effectively utilize the Student Management System.