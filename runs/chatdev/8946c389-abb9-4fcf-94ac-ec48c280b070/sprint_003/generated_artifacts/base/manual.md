```markdown
# Student Management System

A simple application for managing student records, including adding and retrieving student information with email support.

## Main Functions

- **Add Student**: Allows users to input a student's name and email, which are then stored in the database.
- **Show Students**: Displays a list of all students currently stored in the database, including their names and emails.

## Quick Install

To set up the environment and run the application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-management.git
   cd student-management
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.7 or higher installed. Then, install the required packages using pip:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

3. **Set Up Database**:
   The application uses SQLite for the database. You can initialize the database by running:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

4. **Run the Application**:
   Start the FastAPI server and the GUI by running:
   ```bash
   python main.py
   ```

## How to Use the Application

1. **Adding a Student**:
   - Open the GUI window.
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to save the student record.

2. **Viewing Students**:
   - Click the "Show Students" button to retrieve and display the list of all students in the application.
   - The list will show each student's name along with their email.

## Database Migration

The application includes a migration script to add the email field to the existing Student entity. To apply the migration, follow these steps:

1. **Initialize Alembic**:
   ```bash
   alembic init alembic
   ```

2. **Create Migration**:
   ```bash
   alembic revision --autogenerate -m "Add email field to Student"
   ```

3. **Apply Migration**:
   ```bash
   alembic upgrade head
   ```

## Additional Information

For more detailed documentation and examples, please refer to the code comments and structure. The application is built using FastAPI for the backend and Tkinter for the GUI, ensuring a smooth user experience.

If you encounter any issues or have questions, feel free to reach out for support.
```
