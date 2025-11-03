# README.md

# Student Management System

## Overview
The Student Management System is designed to manage student records, including functionality for creating, updating, and retrieving student details. This system has now been enhanced to include email functionality, allowing for more comprehensive communication and management of student information.

## Setup Instructions

### Prerequisites
- Python 3.x
- Database (e.g., PostgreSQL, MySQL)

### Dependencies
Make sure to install the necessary packages specified in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Database Migration
To add the new `email` column to the existing `Students` table, you will need to run a migration script. Follow these steps to perform the migration:

1. **Create Migration Script**:
   Use Alembic to create a new revision:
   ```bash
   alembic revision --autogenerate -m "Add email field to Student entity"
   ```

2. **Update Migration Script**:
   Ensure your migration script includes the following:

   ```python
   def upgrade():
       op.add_column('students', sa.Column('email', sa.String(), nullable=False))

   def downgrade():
       op.drop_column('students', 'email')
   ```

3. **Apply Migration**:
   Run the migration to update the database schema:
   ```bash
   alembic upgrade head
   ```

### Application Structure
The application directory structure should look as follows:

```
/student_management
├── src/
│   ├── app.py
│   ├── models.py  # Updated to include email field
│   ├── routes.py  # Updated to handle email logic
│   ├── tests/
│   │   ├── test_routes.py  # Updated to validate email functionality
├── config.py
├── requirements.txt
├── README.md
```

### Student Creation and Retrieval
With the introduction of the `email` field, when creating a new student, ensure the request body includes the email. The structure should be like this:

```json
{
    "name": "John Doe",
    "email": "johndoe@example.com"
}
```

When retrieving students, the email field will now also be included in the responses.

### Running Tests
To ensure that all functionalities are working as expected, don't forget to run the automated tests, especially those validating the creation and retrieval of students including the new `email` field:

- `test_create_student_with_email_succeeds()`
- `test_get_all_students_includes_email()`

To execute the tests, use:

```bash
pytest
```

## Conclusion
With these updates, the Student Management System now supports email functionality, enhancing its capability to manage student records efficiently. Make sure to follow the migration steps and update routes and tests accordingly to ensure full functionality.