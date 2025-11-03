```markdown
# Student Management Application

The Student Management Application is designed to help manage student records efficiently. It allows users to add students with their names and email addresses, as well as fetch and display the list of students.

## Main Functions

- **Add Student**: Users can input a student's name and email address to add them to the database.
- **Fetch Students**: Users can retrieve and display the list of all students stored in the database, including their names and email addresses.

## Quick Install

To set up the environment and install the required dependencies, follow these steps:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   SQLAlchemy
   alembic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Migration

Before running the application, ensure that the database schema is updated to include the new email field in the Student entity. You can use Alembic for this purpose:

1. **Run the Migration**:
   Make sure you have Alembic installed and then run the migration script:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Run the Application**:
   Start the application by executing the `main.py` file:
   ```bash
   python main.py
   ```

2. **Add a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to save the information.

3. **Fetch Students**:
   - Click the "Fetch Students" button to retrieve and display the list of all students in the application.

## Email Validation

The application includes basic email validation using regex to ensure that the email format is correct before adding a student.

## Troubleshooting

- If you encounter an error related to `tkinter`, ensure that it is installed. It is usually included with Python installations, but you can install it via your package manager if needed.
- If you face issues with database migrations, ensure that Alembic is properly configured and that you have run the migration commands.

## Conclusion

The Student Management Application provides a simple yet effective way to manage student records. By following the installation and usage instructions, you can easily set up and start using the application to manage your student data.
```