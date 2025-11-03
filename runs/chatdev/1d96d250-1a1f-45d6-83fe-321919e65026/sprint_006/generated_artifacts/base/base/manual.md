```markdown
# Student Management Application

A comprehensive application for managing students and their course enrollments.

## Main Functions

The Student Management Application allows users to:

- **Add Students**: Create new student profiles by entering their name and email.
- **Add Courses**: Create new courses by specifying the course name and level.
- **Manage Enrollments**: Associate students with courses through a many-to-many relationship.

## Installation Guide

To run the Student Management Application, you need to set up your environment and install the required dependencies. Follow the steps below:

### Prerequisites

- Python 3.7 or higher
- SQLite (comes pre-installed with Python)

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Create a Virtual Environment

It's recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required Python packages using pip:

```bash
pip install sqlalchemy pydantic fastapi uvicorn requests alembic
```

### Step 4: Initialize the Database

Run the following command to initialize the database and create the necessary tables:

```bash
python -c "from database import init_db; init_db()"
```

## How to Use the Application

### Running the Application

To start the application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server on `http://127.0.0.1:8000`.

### Using the GUI

1. **Launch the GUI**: The GUI will open automatically when you run the `main.py` file.
2. **Add a Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to create the student profile.
3. **Add a Course**:
   - Enter the course name and level in the respective fields.
   - Click the "Add Course" button to create the course profile.

### Enrolling Students in Courses

Once students and courses are created, you can enroll students in courses by modifying the backend logic to handle the association through the `student_courses` table.

## Additional Information

For more detailed documentation on how to extend the application, please refer to the code comments and the Pydantic schemas defined in `schemas.py`.

### Support

If you encounter any issues or have questions, please reach out to our support team via the contact form on our website.

Happy managing!
```