Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses.

## Overview

The Teacher Management System allows users to create and manage records of teachers, students, and courses. It provides a user-friendly interface to add new teachers and students, along with their associated information.

## Main Functions

- **Add Teacher**: Create a new teacher record with a name and email.
- **Add Student**: Create a new student record with a name, email, and associated courses.
- **View Teachers**: Retrieve a list of all teachers.
- **View Students**: Retrieve a list of all students.

## Installation

To set up the environment and run the application, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 3: Set Up the Database

Run the migration script to set up the database schema:

```bash
alembic upgrade head
```

This command will create the necessary tables for students, courses, and teachers while preserving existing data.

## Usage

### Running the Application

To start the application, run the following command:

```bash
python main.py
```

This will launch the GUI for the Teacher Management System.

### Adding a Teacher

1. Enter the teacher's name in the "Enter Teacher Name" field.
2. Enter the teacher's email in the "Enter Teacher Email" field.
3. Click the "Submit Teacher" button.
4. A success message will appear if the teacher is added successfully.

### Adding a Student

1. Enter the student's name in the "Enter Student Name" field.
2. Enter the student's email in the "Enter Student Email" field.
3. Enter the course IDs (comma-separated) in the "Enter Course IDs (comma-separated)" field.
4. Click the "Submit Student" button.
5. A success message will appear if the student is added successfully.

### Viewing Records

Currently, the application does not have a dedicated view for displaying records directly in the GUI. However, you can implement additional functions to retrieve and display the list of teachers and students as needed.

## Conclusion

The Teacher Management System is a straightforward application designed to help manage educational records efficiently. For further enhancements, consider adding features such as editing and deleting records, as well as improved data visualization.

For any issues or feature requests, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.