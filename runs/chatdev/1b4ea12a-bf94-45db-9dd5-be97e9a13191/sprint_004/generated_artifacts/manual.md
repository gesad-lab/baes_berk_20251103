Here is the `manual.md` file that outlines the main functions of the software, installation instructions, and usage guidelines:

```markdown
# Student Course Management System

A comprehensive application for managing students and their associated courses.

## Overview

The Student Course Management System allows users to manage student records and their course enrollments. This application provides functionalities to create, read, update, and delete student and course information, as well as manage the relationships between them.

## Main Functions

- **Student Management**: Create and manage student records, including their names and email addresses.
- **Course Management**: Create and manage courses, including course names and levels.
- **Course Enrollment**: Associate students with multiple courses and manage these relationships effectively.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-course-management.git
   cd student-course-management
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

4. **Run Database Migration**:
   Ensure that the database schema is up to date by running the migration script:
   ```bash
   alembic upgrade head
   ```

## Usage

To start using the application, follow these steps:

1. **Run the Application**:
   Execute the main application file:
   ```bash
   python main.py
   ```

2. **Access the Dashboard**:
   Open your web browser and navigate to `http://localhost:8000` to access the dashboard interface.

3. **Managing Students**:
   - **Add a Student**: Fill in the required fields (name and email) in the provided form.
   - **View Students**: A list of all registered students will be displayed.
   - **Edit/Delete Students**: Select a student to edit their details or remove them from the system.

4. **Managing Courses**:
   - **Add a Course**: Fill in the course name and level in the provided form.
   - **View Courses**: A list of all available courses will be displayed.
   - **Edit/Delete Courses**: Select a course to edit its details or remove it from the system.

5. **Enroll Students in Courses**:
   - Navigate to the student management section and select a student.
   - Choose the courses you want to enroll the student in from the available list.

## Additional Information

For further documentation and detailed API references, please refer to the [API Documentation](https://your-api-docs-link.com).

For support and inquiries, please contact our support team at support@chatdev.com.

```

This manual provides a comprehensive guide for users to understand the software's functionalities, installation process, and how to effectively use the application.