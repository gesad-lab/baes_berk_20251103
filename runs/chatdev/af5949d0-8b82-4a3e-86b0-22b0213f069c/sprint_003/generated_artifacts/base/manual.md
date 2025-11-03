```markdown
# Student Management Application

A simple application for managing student records, including adding and retrieving student information with email support.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address to create a new student record.
- **View Students**: Displays a list of all students along with their names and email addresses.

## Quick Install

To set up the environment and run the application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student_management.git
   cd student_management
   ```

2. **Install Dependencies**:
   Make sure you have Python installed (version 3.7 or higher). Then, install the required packages using pip:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic alembic requests
   ```

3. **Set Up the Database**:
   Initialize the database by running the following command in Python:
   ```python
   from database import init_db
   init_db()
   ```

4. **Run the Application**:
   Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the GUI**:
   Run the GUI application:
   ```bash
   python gui.py
   ```

## How to Use the Application

1. **Adding a Student**:
   - Open the GUI application.
   - Enter the student's name in the provided field.
   - Enter the student's email in the corresponding field.
   - Click the "Add Student" button to submit the information.
   - If successful, the application will display a confirmation message with the added student's details.

2. **Viewing Students**:
   - The application will automatically display the list of students added, including their names and email addresses.

## Database Migration

To add the email field to the existing Student entity, a migration script is included. Ensure that you run the migration before starting the application:

1. **Run Migration**:
   Use Alembic to apply the migration:
   ```bash
   alembic upgrade head
   ```

This will add the email field to the Student entity while preserving existing data.

## Additional Information

For more detailed documentation and examples, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).

For any issues or support, feel free to reach out to the development team.

Happy coding!
```