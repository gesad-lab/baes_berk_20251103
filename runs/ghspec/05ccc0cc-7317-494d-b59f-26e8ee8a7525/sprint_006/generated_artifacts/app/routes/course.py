```python
# app/routes/course.py

from fastapi import APIRouter, HTTPException
from app.models import Course, Teacher  # Import needed models
from app.schemas import CourseResponse, TeacherAssignmentRequest  # Import request/response schemas
from app.database import SessionLocal

router = APIRouter()

# Create a new database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/courses/{course_id}/assign-teacher", response_description="Assign a teacher to a course")
def assign_teacher(course_id: int, teacher_assignment: TeacherAssignmentRequest, db: Session = next(get_db())):
    """
    Assign a teacher to a specific course.

    :param course_id: ID of the course to assign a teacher to
    :param teacher_assignment: Request body containing the teacher's ID to assign
    :param db: Database session
    :return: Confirmation message
    :raises HTTPException if the course or teacher does not exist
    """
    # Retrieve the course by course_id
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Retrieve the teacher using the provided teacher_id
    teacher = db.query(Teacher).filter(Teacher.id == teacher_assignment.teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    # Assign the teacher to the course
    course.teacher_id = teacher.id
    db.commit()  # Save changes to the database
    return {"message": f"Teacher {teacher.id} assigned to course {course.id}"}

@router.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = next(get_db())):
    """
    Retrieve details about a specific course, including assigned teacher.

    :param course_id: ID of the course to retrieve
    :param db: Database session
    :return: Course details along with teacher’s name if assigned
    :raises HTTPException if the course does not exist
    """
    # Retrieve the course from the database
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Prepare response data
    response_data = {
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "teacher_name": course.teacher.name if course.teacher else None  # Include teacher name if exists
    }
    return response_data

```