Here's a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses in an educational environment.

## Overview

The Teacher Management System allows users to create and manage entities for teachers, students, and courses. The main features include:

- **Teacher Management**: Create and manage teacher profiles with required fields such as name and email.
- **Student Management**: Manage student profiles and their associated courses.
- **Course Management**: Create and manage courses and associate them with students.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

The application uses SQLite as the database. To set up the database and create the necessary tables, run the following command:

```bash
python main.py
```

This command will create the `students`, `courses`, and `teachers` tables in the `students.db` database file.

## Usage

### Running the Application

To run the application, execute the following command:

```bash
python gui.py
```

This will launch the graphical user interface (GUI) for the Teacher Management System.

### Creating a Teacher

1. Navigate to the "Teachers" section in the GUI.
2. Fill in the required fields:
   - **Name**: Enter the teacher's name.
   - **Email**: Enter the teacher's email address.
3. Click on the "Create Teacher" button to save the new teacher profile.

### Creating a Student

1. Navigate to the "Students" section in the GUI.
2. Fill in the required fields:
   - **Name**: Enter the student's name.
   - **Email**: Enter the student's email address (optional).
3. Click on the "Create Student" button to save the new student profile.

### Creating a Course

1. Navigate to the "Courses" section in the GUI.
2. Fill in the required fields:
   - **Name**: Enter the course name.
   - **Level**: Enter the course level.
3. Click on the "Create Course" button to save the new course profile.

### Associating Students with Courses

1. Navigate to the "Courses" section.
2. Select a course from the list.
3. Choose students to associate with the selected course.
4. Click on the "Associate Students" button to save the associations.

## Documentation

For more detailed information on the API and usage, please refer to the following sections:

- **Getting Started**: Installation, setting up the environment, and simple examples.
- **How-To Examples**: Demos, integrations, and helper functions.
- **Reference**: Full API documentation.
- **Resources**: High-level explanations of core concepts.

## Support

If you encounter any issues or have questions, please reach out to our support team via the contact form on our website.

```

This manual provides a comprehensive guide for users to understand the functionalities of the Teacher Management System, how to set it up, and how to use it effectively.