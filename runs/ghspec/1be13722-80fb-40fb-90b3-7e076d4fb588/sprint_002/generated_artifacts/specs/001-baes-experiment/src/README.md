# README.md

# Student Entity Management

## Overview
This application provides an API for managing student entities, allowing for the creation and retrieval of students in the system.

## Setup Environment

### Prerequisites
Before running the application or database migrations, ensure that your development environment is prepared with the following:

1. **Python Environment**: Make sure you have Python installed on your machine.

2. **Virtual Environment**: 
   - Create a virtual environment for the project using Poetry:

   ```bash
   poetry install
   ```

3. **Dependencies**: Verify that all existing dependencies are installed for the project. You can install them by running:

   ```bash
   poetry install
   ```

4. **Database Setup**: Ensure that your existing database is set up correctly and accessible by the application. The database structure must be compatible with the new field addition for student entities.

## Database Migration

To include the new `email` field in the student entity, a migration will be performed. This migration will ensure that the existing data remains intact during the schema update:

### Migration Script
Create a new migration script using Alembic to add the `email` field:

```python
# Migration Script (using Alembic)
def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    op.drop_column('students', 'email')
```

Make sure to run the migration command to apply these changes to your database:

```bash
alembic upgrade head
```

## API Endpoints

### Create Student Endpoint
- **Method**: POST
- **Endpoint**: `/students`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  - 201 Created on successful creation
  - 400 Bad Request for validation errors

### Retrieve Students Endpoint
- **Method**: GET
- **Endpoint**: `/students`
- **Response**:
  - 200 OK with a JSON array of student objects containing names and emails.

## Business Logic Updates

To support the new email functionality, the following business logic updates will be implemented:

1. **Validate Email**: The application will include functions to validate the format of the provided email addresses.

2. **Testing**: Ensure that the test coverage for all functionalities, especially the new email validation, meets the required standards.

## Testing

- Update existing tests in `test_student.py` and `test_student_service.py` to accommodate the new email functionality.
- Aim for at least 70% test coverage across new features and ensure critical paths like email validation achieve 90% coverage.

## Documentation Updates

Finally, update the API documentation to reflect the changes, especially the inclusion of the `email` field in requests and responses. Ensure that the application generates accurate OpenAPI specifications reflecting the new email requirement.