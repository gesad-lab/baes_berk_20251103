```markdown
# Student Management Application

A simple application for managing student records, including adding and viewing student information.

## Main Functions

- **Add Student**: Allows users to enter a student's name and email address, which are then stored in the database.
- **View Students**: Displays a list of all students along with their IDs and email addresses.

## Installation

To run the Student Management Application, you need to set up your environment and install the required dependencies. Follow the steps below:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Install Dependencies

Install the required Python packages using pip. You can create a virtual environment to keep your dependencies organized:

```bash
# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install fastapi sqlalchemy pydantic requests alembic
```

### Step 3: Set Up the Database

Before running the application, you need to create the database and tables. You can do this by running the following command in a Python shell:

```python
from database import create_database
create_database()
```

### Step 4: Run the Application

Start the FastAPI server by running the following command:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

### Step 5: Run the GUI

To run the graphical user interface (GUI), execute the following command:

```bash
python gui.py
```

## How to Use the Application

1. **Adding a Student**:
   - Open the GUI.
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to save the information.
   - If successful, a confirmation message will appear.

2. **Viewing Students**:
   - Click the "View Students" button to retrieve and display a list of all students.
   - The list will show each student's ID, name, and email address.

## Migration

If you need to update the database schema to include the new email field, you can run the migration script. Ensure you have Alembic installed and configured. Run the following command to apply the migration:

```bash
alembic upgrade head
```

This will add the email column to the existing Student table while preserving existing data.

## Conclusion

This Student Management Application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily add and view student information. For further customization or enhancements, feel free to modify the code as needed.

For any issues or feature requests, please reach out to the development team.
```