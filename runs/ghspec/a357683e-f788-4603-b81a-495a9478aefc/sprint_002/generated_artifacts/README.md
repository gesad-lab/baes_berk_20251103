# Updated README.md

# Student Management API

## Overview

This API allows for the management of student records, including creating, listing, and updating students.

## Migration Documentation

### Database Schema Changes

1. **New Column**: The `students` table has been updated to include a new column:
   - `email`: string (required, valid email format)

### Migration Steps

To apply these updates without data loss, follow the steps below:

1. **Prepare Migration Script**:
   Ensure you have Alembic installed in your environment. You can do this by running:
   ```bash
   pip install alembic
   ```

2. **Generate Migration**:
   Use Alembic to generate a new migration:
   ```bash
   alembic revision --autogenerate -m "Add email column to students table"
   ```

3. **Modify Migration Script**:
   In the generated migration script, add a command to alter the `students` table to include the `email` column:
   ```python
   from alembic import op
   import sqlalchemy as sa

   # Add email column to student table
   op.add_column('students', sa.Column('email', sa.String(), nullable=False))
   ```

   Ensure that this new column does not violate the existing data by introducing a NOT NULL constraint.

4. **Run the Migration**:
   Apply the migration with:
   ```bash
   alembic upgrade head
   ```

5. **Verify Migration**:
   After running the migration, confirm that the email column has been successfully added without any data loss.

### API Endpoints

#### 1. Create a Student
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
  - **Status**: 201 Created
  - **Body**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

#### 2. List All Students
- **Method**: GET
- **Endpoint**: `/students`
- **Response**:
  - **Status**: 200 OK
  - **Body**:
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      },
      ...
    ]
    ```

#### 3. Update a Student's Email
- **Method**: PUT
- **Endpoint**: `/students/{id}`
- **Request Body**:
  ```json
  {
    "email": "new.email@example.com"
  }
  ```
- **Response**:
  - **Status**: 200 OK
  - **Body**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "new.email@example.com"
    }
    ```

### Validation
All endpoints require that the email provides a valid format. Invalid email formats will result in appropriate error messages being returned.

## Setup Instructions

1. **Install Dependencies**:
   Ensure the virtual environment is active and install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   Start the Flask application:
   ```bash
   flask run
   ```

3. **Testing**:
   Use the test suite to ensure all functionalities and migrations are correct:
   ```bash
   pytest
   ``` 

Make sure to review all parts of the application post-migration to ensure everything works as expected.