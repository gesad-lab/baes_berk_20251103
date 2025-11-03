```markdown
# Student Management Application

A simple application for managing student records, allowing users to add and display student information, including their names and email addresses.

## Main Functions

- **Add Student**: Users can input a student's name and email to add them to the database.
- **Display Students**: Users can view a list of all students stored in the database, including their names and email addresses.

## Installation

To run the Student Management Application, you need to set up your environment and install the required dependencies. Follow the steps below:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Install Dependencies

Install the required Python packages using pip:

```bash
pip install fastapi sqlalchemy pydantic requests
```

### Step 3: Run the Application

To run the application, execute the following command in your terminal:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the application at `http://127.0.0.1:8000`.

## How to Use the Application

1. **Open the GUI**: Once the server is running, the GUI will be available for interaction.
2. **Add a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to save the information.
3. **Display Students**: Click the "Display Students" button to view a list of all students along with their email addresses.

## Database Migration

The application includes a migration script to add the email field to the existing Student entity. This migration ensures that existing student data is preserved while adding the new email column.

### Migration Steps

1. **Upgrade**: The `upgrade` function in `migration.py` adds the email column to the Student table.
2. **Downgrade**: The `downgrade` function is provided for potential rollback scenarios.

## Conclusion

This Student Management Application provides a straightforward interface for managing student records. With the ability to add and display students, it serves as a useful tool for educational institutions or any organization needing to keep track of student information.

For further assistance or support, please reach out to the development team.
```