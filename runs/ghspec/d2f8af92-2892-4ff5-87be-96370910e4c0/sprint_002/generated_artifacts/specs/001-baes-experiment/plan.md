# Implementation Plan: Add Email Field to Student Entity

---

## Version
1.1.0

## Purpose
This implementation plan outlines the necessary steps to enhance the existing Student entity by adding an email field. The plan will detail the architecture, technology stack, module boundaries, data models, API contracts, and implementation approach for accommodating this change, ensuring backward compatibility and maintaining existing functionalities.

## Architecture Overview
The application continues to follow a Microservices architecture with modular components handling different responsibilities. The updates will ensure that the new email field integration does not disrupt existing functionalities and maintains the overall performance of the application.

1. **API Layer**: Exposes RESTful endpoints for CRUD operations, with modifications to handle the new email field.
2. **Service Layer**: Contains business logic for managing student entities, including validations for new email input.
3. **Data Access Layer**: Utilizes the SQLite database through SQLAlchemy for data persistence, now including handling of the email attribute.

## Technology Stack
- **Language**: Python 3.11+
- **Web Framework**: Flask
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Testing Framework**: Pytest
- **Dependency Management**: Poetry

## Module Boundaries and Responsibilities

### 1. API Layer
- **Module Name**: `api`
- **Responsibilities**:
  - Update existing RESTful endpoints and define new behaviors for creating, retrieving, and updating students.
  - Handle request/response formatting (JSON) including the new email field.

### 2. Service Layer
- **Module Name**: `services`
- **Responsibilities**:
  - Modify business logic for handling student information to include email.
  - Implement validation logic for email formats upon student record creation and updates.

### 3. Data Access Layer
- **Module Name**: `models`
- **Responsibilities**:
  - Update the SQLAlchemy Student model to include the new email field.
  - Manage database schema updates and run migration scripts.

## Data Models

### Student Model
```python
# models/student.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """
    Represents a student in the database.

    Attributes:
        id (int): The unique identifier for the student.
        name (str): The name of the student. Must not be null.
        email (str): The email of the student. Must not be null and validated for correct format.
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New field added
```

## API Contracts

### Endpoints
1. **Create Student**
   - **Method**: POST
   - **Endpoint**: `/api/v1/students`
   - **Request Body**: 
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Responses**:
     - `201 Created`: Student successfully created.
     - `400 Bad Request`: Invalid request body (including invalid email).

2. **Retrieve Students**
   - **Method**: GET
   - **Endpoint**: `/api/v1/students`
   - **Responses**:
     - `200 OK`: List of student records with email addresses.
     - `500 Internal Server Error`: Failed to retrieve records.

3. **Update Student**
   - **Method**: PUT
   - **Endpoint**: `/api/v1/students/{id}`
   - **Request Body**:
     ```json
     {
       "name": "Jane Doe",
       "email": "jane.doe@example.com"
     }
     ```
   - **Responses**:
     - `200 OK`: Student updated successfully.
     - `404 Not Found`: Student with specified ID not found.
     - `400 Bad Request`: Invalid request body.

4. **Delete Student**
   - **Method**: DELETE
   - **Endpoint**: `/api/v1/students/{id}`
   - **Responses**:
     - `204 No Content`: Student deleted successfully.
     - `404 Not Found`: Student with specified ID not found.

## Implementation Approach

### Step 1: Database Migration
- Create a migration script to add the new `email` column to the `students` table while preserving existing data.
- Use SQLAlchemy’s migration framework (Alembic) to automate this migration.

### Step 2: Modify Data Access Layer
- Update the `Student` model to include the new email field requiring the following changes to `models/student.py`.
- Ensure email is mandatory during student creation and updates.

### Step 3: Update Service Layer Logic
- Enhance the service layer’s business logic to accommodate changes in the student model.
- Implement validation logic for emails, ensuring they conform to basic formatting requirements.

### Step 4: Update API Layer Endpoints
- Modify API endpoint definitions to support email field handling in both creation and update requests.

### Step 5: Testing
- Create unit tests for the new email-related functionalities using Pytest.
- Ensure at least 70% coverage for business logic with appropriate test cases for email validations.

### Step 6: Documentation
- Update the README.md to reflect the new required fields and database migration instructions.
- Document assumptions and limitations regarding email handling.

## Scalability, Security, and Maintainability
- **Scalability**: The current design remains scalable and flexible, suitable for user growth and possible future database migrations.
- **Security**: Input validation for email fields will be enforced. No sensitive data will be logged, and proper error messages will guide users.
- **Maintainability**: The modular approach continues, allowing easy updates and enhancements. Code will grow with clear responsibilities.

## Success Criteria
- The `Student` entity now includes an `email` field that is validated upon creation and updates.
- Modified API endpoints function correctly and return accurate JSON responses for the new data.
- Existing data remains intact post-migration.
- Comprehensive and automated test coverage is achieved as per requirements.

## Trade-offs and Decisions
- **Email Validation**: Basic format checking has been implemented without advanced verifications (such as domain existence) to maintain simplicity within the current scope.
- **SQLite**: Maintained due to its simplicity and ease of use but future considerations for scaling or concurrent handling may necessitate transition to a more robust solution (e.g., PostgreSQL).

By following this implementation plan, we ensure the successful enhancement of the Student entity without compromising the integrity of the existing functionality or data. 

### Modifications Needed to Existing Files
- `models/student.py`: Add the `email` attribute to the `Student` class.
- `api/student_api.py`: Update endpoint definitions to include handling for the `email` attribute.
- Migration script (new file): Create a script to add the `email` column to the existing `students` table.

### Database Migration Strategy
1. Create a new migration file utilizing Alembic.
2. Implement the migration logic to alter the existing `students` table, adding the `email` column.
3. Execute the migration as part of the application startup process or manually if preferred. 

With these steps outlined, the project can successfully integrate the new feature into the existing architecture, delivering an improved student management capability.
