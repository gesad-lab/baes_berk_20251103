Here's the `manual.md` file that provides a detailed user manual for the software, including an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Course Management System

A simple application for managing students and courses.

## Overview

This application allows users to manage student information and courses. Users can add students and courses, ensuring that the data is stored in a structured manner. The application is built using FastAPI for the backend and Tkinter for the GUI.

## Main Functions

- **Add Student**: Users can input student names and emails to add them to the database.
- **Add Course**: Users can create courses with a name and level, which are stored in the database.
- **Data Preservation**: The application ensures that existing student data is preserved during database migrations.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/course-management-system.git
   cd course-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure that you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   ```

## Usage

1. **Run the FastAPI Server**:
   Start the FastAPI server to handle backend requests:
   ```bash
   uvicorn main:app --reload
   ```

2. **Launch the GUI**:
   Run the GUI application to interact with the backend:
   ```bash
   python gui.py
   ```

3. **Adding Students**:
   - Open the GUI application.
   - Enter the student's name and email in the provided fields.
   - Click the "Add Student" button to submit the information.

4. **Adding Courses**:
   - The course addition functionality can be implemented similarly to the student addition. You can create a separate GUI for course management or extend the existing one.

## Database Migration

The application includes a migration script (`migration.py`) that creates the `Course` table while preserving existing student data. To run the migration, execute:
```bash
python migration.py
```

## Additional Information

For more detailed documentation on FastAPI and SQLAlchemy, please refer to the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

## Support

If you encounter any issues or have questions, please reach out to our support team or check the GitHub repository for issues and discussions.

```

This manual provides a comprehensive guide for users to understand the application, install it, and use its features effectively.