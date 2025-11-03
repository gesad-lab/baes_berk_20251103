# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Architecture Overview

### 1.1 Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite 
- **Serialization**: Marshmallow for JSON validation and serialization
- **Environment Management**: pipenv for virtual environment and dependency management
- **Testing Framework**: pytest 
- **API Documentation**: OpenAPI (Swagger) for documenting endpoints 

### 1.2 Module Structure
```
student_management/
│
├── src/
│   ├── app.py               # Application entry point
│   ├── models.py            # Database models (add Teacher relationship to Course here)
│   ├── schemas.py           # Marshmallow schemas (update Course schema here)
│   ├── routes.py            # API endpoint definitions (update course routes here)
│   ├── database.py          # Database configuration and initialization
│   └── config.py            # Configuration settings
│
├── tests/
│   ├── test_routes.py       # Unit and integration tests for API endpoints (update course tests here)
│   └── test_models.py       # Unit tests for database models (update course tests here)
│
├── .env                     # Environment variables for configuration
├── .env.example             # Example environment variables file
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## II. Database Design

### 2.1 Schema Definition
- **Course Table Update**:
  - Update the existing `courses` table to include:
    - `teacher_id`: Integer (Foreign Key referencing `teachers` entity; can be null)

### 2.2 Initialization
- Implement a migration strategy using Flask-Migrate to add the `teacher_id` column to the `courses` table while preserving existing `Student` and `Course` data.

## III. API Design

### 3.1 Endpoints Modification
- **POST /courses**
  - Request Body: 
    ```json
    {
      "course_name": "string",
      "teacher_id": "integer"  // Optional
    }
    ```
  - Success Response: 
    ```json
    {
      "message": "Course created successfully."
    }
    ```
  - Status Code: `201 Created`
  
- **PUT /courses/{id}**
  - Request Body: 
    ```json
    {
      "teacher_id": "integer" // Required to assign a teacher
    }
    ```
  - Success Response: 
    ```json
    {
      "message": "Course updated successfully."
    }
    ```
  - Status Code: `200 OK`
  
  - Error Response (non-existent teacher): 
    ```json
    {
      "error": {
        "code": "E003",
        "message": "Teacher does not exist."
      }
    }
    ```
  - Status Code: `400 Bad Request`

## IV. Implementation Plan

### 4.1 Step-by-step Implementation
1. **Setup Environment**
   - Ensure the `.env` file is updated with any necessary configuration settings.

2. **Update the Model**
   - Update the `Course` model in `models.py` to include a foreign key to the `Teacher`.
   ```python
   class Course(db.Model):
       __tablename__ = 'courses'
       id = db.Column(db.Integer, primary_key=True)
       course_name = db.Column(db.String, nullable=False)
       teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)  # New field
   ```

3. **Database Migration**
   - Use Flask-Migrate to create a migration script for adding the `teacher_id` column to the `courses` table:
   ```bash
   flask db migrate -m "Add teacher_id to courses table"
   flask db upgrade
   ```

4. **Update Marshmallow Schemas**
   - Update the existing `CourseSchema` in `schemas.py` to include `teacher_id`.
   ```python
   class CourseSchema(ma.SQLAlchemyAutoSchema):
       class Meta:
           model = Course
           include_fk = True  # To include foreign key fields in the serialized output
   ```

5. **Add API Endpoint Logic**
   - Update the `POST /courses` and `PUT /courses/{id}` endpoints in `routes.py`.
   ```python
   @app.route('/courses', methods=['POST'])
   def create_course():
       data = request.get_json()
       # Validate input
       if not data.get('course_name'):
           return {"error": {"code": "E001", "message": "Course name is required."}}, 400

       new_course = Course(course_name=data['course_name'], teacher_id=data.get('teacher_id'))
       db.session.add(new_course)
       db.session.commit()
       
       return {"message": "Course created successfully."}, 201

   @app.route('/courses/<int:id>', methods=['PUT'])
   def update_course(id):
       data = request.get_json()
       teacher_id = data.get('teacher_id')
       if teacher_id and not Teacher.query.get(teacher_id):
           return {"error": {"code": "E003", "message": "Teacher does not exist."}}, 400

       course = Course.query.get_or_404(id)
       course.teacher_id = teacher_id  # Set the teacher ID
       db.session.commit()
       return {"message": "Course updated successfully."}, 200
   ```

6. **Implement Error Handling and Validation**
   - Ensure error responses are properly structured, especially for undefined teacher assignments.

7. **Testing**
   - Write new unit tests for the updated `Course` model and API endpoints in the `tests` folder.
   - Ensure tests cover all scenarios including valid teacher assignments and handling errors with non-existent teachers.
   - Aim for a minimum of 70% coverage on the new business logic.

8. **Documentation**
   - Update the README.md file to include details about the new functionality involving teacher assignments to courses.
   - Ensure that API documentation reflects the changes for new endpoint requirements.

## V. Testing Strategy

### 5.1 Types of Tests
- **Unit Tests**: Validate the updated `Course` model and its schema functionality.
- **Integration Tests**: Verify the modified API endpoints for course creation and updates.
- **Contract Tests**: Ensure that API responses match defined specifications.

### 5.2 Coverage Requirements
- Minimum coverage target: 70% for all new business logic, with critical paths targeting 90%.

## VI. Deployment Considerations

### 6.1 Environment Management
- Confirm that any new environment configuration related to the course entity is documented.

### 6.2 Deployment Steps
- Run migrations to ensure the `teacher_id` column is created properly without risking existing data integrity.
- Verify that the application starts without errors post-deployment.

### 6.3 Monitoring & Logging
- Implement monitoring mechanisms for API performance and error rates after deployment.

## VII. Conclusion

This implementation plan outlines the steps required to establish a `Teacher` relationship within the `Course` entity of our application. By adhering to this structured plan, we will ensure robust data management and user-friendly API capabilities for course and teacher integration.

### Modifications to Existing Files:
- **models.py**: Added a `teacher_id` foreign key in the `Course` class.
- **schemas.py**: Updated `CourseSchema` to include foreign key relationships.
- **routes.py**: Enhanced `POST /courses` and `PUT /courses/{id}` endpoints to support teacher assignments.
- **tests/test_routes.py**: Created tests for updated `POST /courses` and `PUT /courses/{id}`.
- **tests/test_models.py**: Created tests to ensure model behaviors including relationships with teachers.

### Database Migration Strategy:
- Use Flask-Migrate to generate a migration script to add the `teacher_id` column, ensuring the existing records remain intact with `null` values.

This comprehensive plan ensures that educators can be effectively linked to courses, thereby improving the overall functionality and data handling within the application.