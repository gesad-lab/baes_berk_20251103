# README.md

# Project Title

## Overview

This project is designed to manage courses and students efficiently while providing a robust API for interaction. This document outlines how to set up the environment, details the API endpoints, and provides instructions for usage.

## Table of Contents
- [Set Up Environment](#set-up-environment)
- [API Endpoints](#api-endpoints)
  - [Students](#students)
  - [Teachers](#teachers)
- [Testing](#testing)
- [Contributing](#contributing)

## Set Up Environment

1. Ensure the virtual environment is active.
2. Install all dependencies:
   ```bash
   pip install Flask SQLAlchemy Marshmallow pytest
   ```

## Database Schema Migration

### Teachers Table

A new table `teachers` has been created to store Teacher entities. The migration script is as follows:

```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False, unique=True)
    )

def downgrade():
    op.drop_table('teachers')
```

## API Endpoints

### Students

- **POST /students**
  - Create a new student record.
  - **Required Parameters**: 
    - `name`: Name of the student.
    - `email`: Email of the student (must be unique).
  - **Request Body**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created student record with an ID.

- **GET /students**
  - Retrieve all student records.
  - **Response**: Returns a list of all students.

### Teachers

- **POST /teachers**
  - Create a new teacher record.
  - **Required Parameters**: 
    - `name`: Name of the teacher.
    - `email`: Email of the teacher (must be unique).
  - **Request Body**:
    ```json
    {
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }
    ```
  - **Response**: Returns the created teacher record with an ID.

- **GET /teachers**
  - Retrieve all teacher records.
  - **Response**: Returns a list of all teachers.

## Testing

- Unit and integration tests for the new Teacher functionality have been written.
- Ensure at least 70% coverage for business logic and 90% for validation routes.

## Contributing

For contributions, please fork the repository and submit a pull request. Ensure that your code adheres to the coding standards and passes all tests.

--- 

This README file has been updated to include the new Teachers endpoints, reflecting the recent changes in the API operation and database schema. Please follow these instructions carefully to set up the environment and utilize the new features available through the API.