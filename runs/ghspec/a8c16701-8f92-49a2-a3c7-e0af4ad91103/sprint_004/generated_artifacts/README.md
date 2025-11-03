# README.md

# FastAPI Project Documentation

## Overview

This FastAPI project serves as a backend application for managing student and course information. It allows users to create, read, update, and delete records pertaining to students and courses. Additionally, it includes functionality for associating students with courses through a join table.

## Project Structure

The project follows a standard FastAPI framework structure:

```
src/
    app.py               # Main application entry point
    db.py                # Database connection and session management
    models/              # Contains all database models
        __init__.py
        student.py       # Student model definition
        course.py        # Course model definition
    api.py               # API endpoint definitions
    errors.py            # Centralized error handling
tests/
    test_api.py          # Test cases for API endpoints
    test_course.py       # Test cases for Course model
```

## Setup Instructions

1. **Clone the Repository**  
   Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**  
   Ensure all required dependencies are installed. The project requires:
   - FastAPI
   - SQLAlchemy
   - Alembic

   Install the dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**  
   The project uses SQLAlchemy for database interactions and Alembic for migrations. The database connection settings can be found in the `db.py` file.

## Database Models

### Student Model

The `Student` model has been modified to include a relationship with courses via a join table called `student_courses`.

### Course Model

The `Course` model represents courses available for students. 

### Join Table

The `student_courses` join table facilitates many-to-many associations between students and courses. The following migration script should be executed to create this table:

```bash
alembic revision --autogenerate -m "Add StudentCourse join table"
```

Edit the migration script to include the join table creation as follows:

```python
def upgrade():
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('student_id', 'course_id'),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'])
    )

def downgrade():
    op.drop_table('student_courses')
```

Finally, apply the migration:

```bash
alembic upgrade head
```

## API Endpoints

The application provides several API endpoints for managing students and courses. Key functionalities include:

- Associating courses with students.
- Retrieving courses associated with a particular student.
  
Ensure that validation is in place for checking the existence of courses when creating associations.

## Testing

The project includes tests implemented using pytest. To run the tests, use the following command:

```bash
pytest
```

Tests verify database interactions and API endpoint functionalities.

## Error Handling

Centralized error handling is implemented within the `errors.py` module. It includes structured error responses for various scenarios, including invalid course IDs during student and course associations.

## Additional Notes

- The project may be extended with additional features in future sprints.
- Refer to the individual model and module files for further details on functionality.

---

This documentation provides a high-level overview of the FastAPI project, its structure, and how to set it up and use it effectively. Further enhancements and features may lead to additional changes in models and endpoints.