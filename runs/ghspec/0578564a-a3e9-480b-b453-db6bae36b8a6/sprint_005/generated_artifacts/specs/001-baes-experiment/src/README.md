# README.md

# Student Management System

This project is a student management system that allows for managing courses and teachers efficiently. It is built using Flask and SQLAlchemy.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Database Migration](#database-migration)
- [API Endpoints](#api-endpoints)
- [Application Structure](#application-structure)
- [Testing](#testing)

## Installation

1. Clone the repository:
   ```bash
   git clone https://your-repo-url.git
   cd student_management
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables as necessary.

## Usage

1. Run the application:
   ```bash
   python src/app.py
   ```

2. The application will be available at `http://localhost:5000`.

## Database Migration

To create the `teachers` table, follow these steps:

1. Generate the migration script using Alembic:
   ```bash
   alembic revision --autogenerate -m "Create teachers table"
   ```

2. The migration script should look like this:
   ```python
   def upgrade():
       op.create_table(
           'teachers',
           sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
           sa.Column('name', sa.String(length=255), nullable=False),
           sa.Column('email', sa.String(length=255), nullable=False, unique=True),
       )

   def downgrade():
       op.drop_table('teachers')
   ```

## API Endpoints

### Teachers

- **Create Teacher**
  - **POST** `/api/v1/teachers`
  - **Request Body**: 
    ```json
    {
      "name": "Teacher Name",
      "email": "teacher@example.com"
    }
    ```
  - **Responses**:
    - 201 Created: Teacher created successfully.
    - 400 Bad Request: Name and email are required.

- **Get Teacher**
  - **GET** `/api/v1/teachers/{teacher_id}`
  - **Responses**:
    - 200 OK: Returns the teacher details.
    - 404 Not Found: Teacher not found.

## Application Structure

```
/student_management
├── src/
│   ├── app.py
│   ├── models.py      # Add the Teacher model
│   ├── routes.py      # Add new routes for teacher management
│   ├── tests/
│   │   ├── test_routes.py  # Add tests for teacher endpoints
├── config.py
├── requirements.txt
├── README.md
```

## Testing

Make sure to run the tests after implementing your changes. You can run the tests using:
```bash
pytest
```

This documentation serves as a guide for developers interacting with the Student Management System and should be kept up to date with any changes in the application.