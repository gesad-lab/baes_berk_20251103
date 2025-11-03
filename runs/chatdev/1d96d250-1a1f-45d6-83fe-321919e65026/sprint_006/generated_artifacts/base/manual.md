```markdown
# Teacher Management Application

A simple application for managing students, courses, and teachers in an educational environment.

## Main Functions

The Teacher Management Application allows users to:

- **Add Students**: Create new student records with names and emails.
- **Add Courses**: Create new courses with names and levels.
- **Add Teachers**: Create new teacher records with names and emails.
- **View Records**: View existing students, courses, and teachers (functionality to be implemented).

## Installation

To run the Teacher Management Application, you need to set up your environment and install the necessary dependencies. Follow the steps below:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/teacher-management-app.git
cd teacher-management-app
```

### Step 2: Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

Make sure to include the following dependencies in your `requirements.txt`:

```
fastapi
uvicorn
sqlalchemy
pydantic
requests
tkinter
alembic
```

### Step 4: Initialize the Database

Run the following command to initialize the database and create the necessary tables:

```bash
python -c "from database import init_db; init_db()"
```

### Step 5: Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Then, run the GUI application:

```bash
python main.py
```

## How to Use the Application

1. **Adding a Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to submit the information.

2. **Adding a Course**:
   - Enter the course name and level in the respective fields.
   - Click the "Add Course" button to submit the information.

3. **Adding a Teacher**:
   - Enter the teacher's name and email in the respective fields.
   - Click the "Add Teacher" button to submit the information.

4. **Viewing Records**:
   - Currently, the application does not support viewing records. This feature will be implemented in future updates.

## Additional Information

For more detailed documentation on FastAPI and SQLAlchemy, please refer to their official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

If you encounter any issues or have questions, please reach out to the support team or check the GitHub repository for updates and issues.

Happy Teaching!
```