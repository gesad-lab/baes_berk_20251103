Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course and Student Management System

A simple GUI application for managing students and courses using a RESTful API.

## Main Functions

This software allows users to perform the following functions:

- **Add Students**: Users can input student names and emails to add them to the database.
- **View Students**: Users can retrieve and view the list of all registered students.
- **Add Courses**: Users can input course names and levels to add them to the database.
- **View Courses**: Users can retrieve and view the list of all available courses.

## Installation

To run this application, you need to set up your environment and install the necessary dependencies. Follow the steps below:

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required packages using pip:

```bash
pip install fastapi[all] sqlalchemy pydantic requests
```

### Step 4: Run the Database Migration

Before running the application, ensure that the database is set up correctly. Run the migration script to create the necessary tables:

```bash
python main.py
```

## How to Use the Application

### Starting the Application

To start the GUI application, run the following command:

```bash
python gui.py
```

This will open a window where you can manage students and courses.

### Adding a Student

1. Enter the student's name in the "Student Name" field.
2. Enter the student's email in the "Student Email" field.
3. Click the "Add Student" button to add the student to the database.
4. A confirmation message will appear indicating whether the student was added successfully.

### Viewing Students

1. Click the "Get Students" button to retrieve the list of all registered students.
2. The list will be displayed below the button.

### Adding a Course

1. Enter the course name in the "Course Name" field.
2. Enter the course level in the "Course Level" field.
3. Click the "Add Course" button to add the course to the database.
4. A confirmation message will appear indicating whether the course was added successfully.

### Viewing Courses

1. Click the "Get Courses" button to retrieve the list of all available courses.
2. The list will be displayed below the button.

## Conclusion

This Course and Student Management System provides a simple interface for managing students and courses. By following the installation and usage instructions, you can easily set up and interact with the application.

For further assistance, please refer to the code comments or reach out to the development team.
```

This manual provides a comprehensive overview of the software, its functions, installation instructions, and usage guidelines. Let me know if you need any modifications or additional information!