```markdown
# Student Management Application

A simple application for managing student records, including adding and listing students with their email addresses.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address, which will be stored in the database.
- **List Students**: Displays a list of all students in the database along with their names and email addresses.

## Installation

To run the Student Management Application, you need to set up your environment with the necessary dependencies. Follow the steps below:

### Prerequisites

- Python 3.7 or higher
- SQLite (comes pre-installed with Python)

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required Python packages using pip:

```bash
pip install fastapi sqlalchemy pydantic alembic requests
```

### Step 4: Initialize the Database

Run the following command to create the database tables:

```bash
python -c "from database import init_db; init_db()"
```

## How to Use the Application

### Running the Application

To start the application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the application at `http://127.0.0.1:8000`.

### Using the GUI

1. **Add Student**:
   - Open the GUI application.
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to save the student record.

2. **List Students**:
   - Click the "List Students" button to retrieve and display all students in the application.
   - The list will show each student's ID, name, and email.

### Database Migration

If you need to update the database schema (e.g., adding new fields), you can use Alembic for migrations. The migration script provided will add the email field to the Student entity while preserving existing data.

To run the migration, execute:

```bash
alembic upgrade head
```

## Conclusion

This Student Management Application provides a simple interface for managing student records. You can easily add new students and view existing records. For any issues or feature requests, please reach out to the development team.
```