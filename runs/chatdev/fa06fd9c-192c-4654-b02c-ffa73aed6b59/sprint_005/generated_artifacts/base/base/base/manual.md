Here's the `manual.md` file that provides a detailed user manual for the Student Management software, including installation instructions and usage guidelines.

```markdown
# Student Management Application

A simple application for managing student records, including adding and viewing students with their names and email addresses.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address, which are then stored in the database.
- **Show Students**: Displays a list of all students currently stored in the database, showing both names and email addresses.

## Quick Install

To run the Student Management Application, you need to set up your environment and install the necessary dependencies.

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure you have `pip` installed, then run:
   ```bash
   pip install fastapi[all] sqlalchemy requests
   ```

4. **Initialize the Database**:
   Before running the application, you need to initialize the database. Open a Python shell and run:
   ```python
   from database import init_db
   init_db()
   ```

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI server by running:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the GUI**:
   The application will be available at `http://127.0.0.1:8000`. Open this URL in your web browser.

3. **Add a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to save the student record.

4. **View Students**:
   - Click the "Show Students" button to display a list of all students. Each entry will show the student's name and email address.

## Additional Information

- **Database**: The application uses SQLite as the database to store student records.
- **Dependencies**: Ensure you have the required dependencies installed as mentioned in the Quick Install section.
- **Error Handling**: If there are issues adding a student, an error message will be displayed.

## Support

For any issues or questions, please reach out to the development team or refer to the documentation for further assistance.

```

This manual provides a comprehensive overview of the application, installation steps, and usage instructions, ensuring that users can effectively utilize the Student Management Application.