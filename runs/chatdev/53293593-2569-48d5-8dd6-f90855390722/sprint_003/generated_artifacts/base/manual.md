```markdown
# Student Management System

A simple application for managing student records, including the ability to add and update student information.

## Main Functions

- **Add Student**: Allows you to add a new student with their name and email address.
- **Update Student**: Enables updating existing student records, including their email.
- **Database Management**: Handles the SQLite database connection and schema updates.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
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
   Make sure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. **Run the Application**:
   Start the application by executing the following command:
   ```bash
   python main.py
   ```

2. **Database Migration**:
   The application will automatically handle the migration to add the new email field to the Student entity. Existing student data will be preserved during this process.

3. **Interacting with the Application**:
   - You can use the application to add new students by providing their name and email.
   - Update existing student records as needed.

## Example Usage

To add a new student, you can use the following command in your application interface:
```python
new_student = StudentSchema(name="John Doe", email="john.doe@example.com")
```

To update an existing student's email:
```python
existing_student.email = "new.email@example.com"
```

## Documentation

For more detailed information on how to use the application, please refer to the following resources:

- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

## Support

If you encounter any issues or have questions, please reach out to our support team through the provided contact methods.

Thank you for using the Student Management System!
```