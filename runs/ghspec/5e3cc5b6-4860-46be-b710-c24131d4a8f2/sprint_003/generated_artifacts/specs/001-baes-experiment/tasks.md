# Tasks: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/main.py` (Size: 2048 bytes)
- `src/models/student.py` (Size: 1500 bytes)
- `tests/test_student.py` (Size: 2697 bytes)

### Task Breakdown

1. **Set up environment for Course Entity**
   - **Task**: Create a `poetry` project and install necessary dependencies.
     - **File**: `README.md`
     - **Description**: Document the installation steps for the project dependencies.
     - [ ] Update project setup instructions for using Poetry.
  
2. **Define Course Model**
   - **Task**: Create the Course entity model.
     - **File**: `src/models/course.py`
     - **Description**: Define the `Course` SQLAlchemy model with fields `id`, `name`, and `level`.
     ```python
     from sqlalchemy import Column, Integer, String
     from database.database import Base

     class Course(Base):
         __tablename__ = 'courses'
         id = Column(Integer, primary_key=True, autoincrement=True)
         name = Column(String, nullable=False)
         level = Column(String, nullable=False)
     ```
     - [ ] Implement `Course` model in `course.py`.

3. **Create Pydantic Schemas**
   - **Task**: Define Pydantic schemas for creating and retrieving course entities.
     - **File**: `src/schemas/course_schema.py`
     - **Description**: Create the `CourseCreate` and `CourseResponse` schemas.
     ```python
     from pydantic import BaseModel, constr

     class CourseCreate(BaseModel):
         name: constr(min_length=1, max_length=100)  # Required field
         level: constr(min_length=1, max_length=100)  # Required field

     class CourseResponse(BaseModel):
         id: int
         name: str
         level: str
     ```
     - [ ] Implement schemas in `course_schema.py`.

4. **Implement Course Routes**
   - **Task**: Create API routes for Course entity operations.
     - **File**: `src/routes/course_routes.py`
     - **Description**: Define endpoints for creating, retrieving, and updating courses.
     ```python
     from fastapi import APIRouter, HTTPException
     from models.course import Course
     from schemas.course_schema import CourseCreate, CourseResponse

     router = APIRouter()

     @router.post("/courses", response_model=CourseResponse)
     async def create_course(course: CourseCreate):
         # Logic to create course
         pass
     
     @router.get("/courses/{id}", response_model=CourseResponse)
     async def get_course(id: int):
         # Logic to retrieve course
         pass

     @router.put("/courses/{id}", response_model=CourseResponse)
     async def update_course(id: int, course: CourseCreate):
         # Logic to update course
         pass
     ```
     - [ ] Implement routes in `course_routes.py`.

5. **Update Main Application with Course Routes**
   - **Task**: Include the Course routes in the main FastAPI application.
     - **File**: `src/main.py`
     - **Description**: Import and include the course routes in the FastAPI app instance.
     - [ ] Modify `main.py` to import and use course routes.

6. **Database Migration for Courses Table**
   - **Task**: Create migration script to add Courses table.
     - **File**: `migrations/create_courses_table.py`
     - **Description**: Write the SQLAlchemy code for the migration script.
     ```python
     from sqlalchemy import create_engine, Column, Integer, String
     from database.database import Base

     engine = create_engine('sqlite:///./test.db')
     Base.metadata.create_all(bind=engine)
     ```
     - [ ] Implement migration script.

7. **Create Tests for Course API**
   - **Task**: Write unit tests for Course functionality.
     - **File**: `tests/test_course.py`
     - **Description**: Write tests for creating, retrieving, and updating courses to ensure coverage.
     ```python
     from fastapi.testclient import TestClient
     from main import app

     client = TestClient(app)

     def test_create_course():
         response = client.post("/courses", json={"name": "Mathematics 101", "level": "Beginner"})
         assert response.status_code == 201
         # Additional assertions...
     ```
     - [ ] Implement test cases for Course API in `test_course.py`.

8. **Documentation Updates for API Endpoints**
   - **Task**: Update FastAPI documentation to include newly created endpoints.
     - **File**: `README.md`
     - **Description**: Document the endpoints for the Course entity.
     - [ ] Update API documentation to reflect new Course endpoints.

9. **Testing Validation for Required Fields**
   - **Task**: Ensure error handling for missing fields is implemented.
     - **File**: `src/routes/course_routes.py`
     - **Description**: Add proper error response handling for missing `name` or `level` in the request.
     - [ ] Implement error handling logic for required fields.

---
With these tasks, the development team can independently implement and test each component of the Course entity feature in a structured manner. Each task is scoped to one file and can be executed and verified on its own.