# Implementation Plan: Add Email Field to Student Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

## Previous Sprint Plan:
# Implementation Plan: Student Web Application

## Overview
This implementation plan outlines the addition of an email field to the existing Student entity in the application. The goal is to enhance the model by incorporating an essential piece of information for communication and identification purposes. The implementation will involve modifying the existing API and database schema while ensuring that existing data remains intact and functional.

## Architecture
The architecture remains the same as the previous sprint, adhering to the Model-View-Controller (MVC) pattern, with the following components impacting the existing structure:

- **API Layer**: New endpoints for creating and retrieving Student entities now incorporate the email field.
- **Service Layer**: Logic for handling email integration added.
- **Data Access Layer (DAL)**: Updates to the data model and database interactions for the Student entity.
- **Database**: The SQLite database schema will be updated to include the email field.

### Module Boundaries
- **api.py**: Modify existing endpoints to incorporate the email field in request and response models.
- **models.py**: Update the Student model to add an email field.
- **services.py**: Adjust the business logic for creating and retrieving Students.
- **database.py**: Update schema management functions for migration support.

## Technology Stack
- **Programming Language**: Python 3.11+
- **Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Serialization/Validation**: Pydantic
- **Testing Framework**: pytest

## Implementation Steps

### 1. Environment Setup
- Ensure FastAPI and necessary dependencies are already installed based on the previous sprint. No new installations are necessary.

### 2. Define Data Models
- Update the `Student` model in `models.py` to include the `email` field:

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New required field
```

- Update the Pydantic schema for student creation:
```python
from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # New required field
```

### 3. Database Management
- To accommodate the new field, implement a migration using Alembic or modify the database schema directly using SQLAlchemy. Here’s an example migration script:

```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    op.drop_column('students', 'email')
```

### 4. Implement API Endpoints
- Modify the `POST /students` endpoint in `api.py` to include the email field:

```python
@app.post("/students", response_model=Student)
def add_student(student: StudentCreate):
    return create_student(session=SessionLocal(), name=student.name, email=student.email)
```

- The `GET /students` endpoint must also ensure that retrieved Student data includes the email field:

```python
@app.get("/students", response_model=List[Student])
def read_students():
    return get_students(session=SessionLocal())
```

### 5. Implement Business Logic
- Update functions in `services.py` to handle the addition of the email address:

```python
def create_student(session: Session, name: str, email: str):
    student = Student(name=name, email=email)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

def get_students(session: Session):
    return session.query(Student).all()
```

### 6. Error Handling
- Ensure proper error messages are set up for missing email fields in the `api.py` file:

```python
@app.post("/students", response_model=Student, status_code=201)
def add_student(student: StudentCreate):
    if not student.name:
        raise HTTPException(status_code=400, detail="Name field is required.")
    if not student.email:
        raise HTTPException(status_code=400, detail="Email field is required.")
    return create_student(session=SessionLocal(), name=student.name, email=student.email)
```

### 7. Testing
- Extend existing tests in `tests/test_api.py` to cover new cases, including email validation:

```python
def test_create_student_with_email(client):
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["email"] == "john@example.com"

def test_create_student_without_email(client):
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Email field is required."
```

### 8. Documentation
- Update `README.md` to reflect the new requirements for creating and retrieving Students, specifically mentioning the email field.

## Scalability and Security Considerations
- **Scalability**: The updated application remains stateless, allowing for horizontal scaling.
- **Security**: Ensure email inputs are validated to protect against injections.

## Deployment Considerations
- Migrate the database schema to include the new field during deployment using the migration scripts prepared. 
  Run the migration scripts using:
```bash
alembic upgrade head
```

## Conclusion
This implementation plan provides a structured approach to adding an email field to the existing Student entity, maintaining harmony with the existing application structure while allowing future enhancements. The approach ensures backward compatibility and includes extensive testing to verify correctness and stability. By following these steps, the enhancement can be implemented efficiently and cleanly.