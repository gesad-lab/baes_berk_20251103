# README.md

# Teacher Management API

This project now includes a *Teacher Management API* that allows you to create and retrieve teacher records through designated endpoints. Below are the details on how to set up, migrate the database, and utilize the API.

## Introduction

The Teacher Management feature enables the management of teacher data within the application. Users can create new teacher records and retrieve existing ones through a RESTful API.

## Setup Project Structure

Ensure that the following directory structure is created:

```
models/
    teacher.py
schemas/
    teacher_schema.py
controllers/
    teacher_controller.py
```

## Database Migration

To accommodate the new teacher data, you will need to migrate the database. The `teachers` table can be created by applying the following migration:

```python
def upgrade():
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )

def downgrade():
    op.drop_table('teachers')
```

To run the migration, use the following command:

```bash
flask db migrate -m "Add teachers table"
flask db upgrade
```

## API Endpoints

### Create Teacher

**Endpoint:** `POST /api/teachers`  
**Request Body:**
```json
{
    "name": "John Doe",
    "email": "johndoe@example.com"
}
```
**Response:**  
Returns the created teacher object with a unique ID.

### Retrieve Teacher

**Endpoint:** `GET /api/teachers/<id>`  
**Response:**  
Returns the teacher object with the specified ID if found or returns a 404 error if not found.

## Request Validation

The input for creating a teacher is validated to ensure that both `name` and `email` are present and valid. Make sure your requests comply with these requirements to avoid validation errors.

## Testing

To test the teacher functionality, run the tests defined in `tests/test_teacher.py`. Ensure your testing environment is set up correctly. 

To run the tests, use the following command:

```bash
pytest tests/test_teacher.py
```

## Conclusion

With these updates, the Teacher Management API is now integrated into the application, providing essential functionality for managing teacher data. For additional information and updates, refer to the project documentation.