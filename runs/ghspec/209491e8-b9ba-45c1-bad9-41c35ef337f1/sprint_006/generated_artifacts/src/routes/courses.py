```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Course, Teacher
from src.schemas import CourseResponse, TeacherAssignment
from sqlalchemy.exc import NoResultFound

router = APIRouter()

@router.post("/{course_id}/assign-teacher", response_model=dict)
def assign_teacher_to_course(course_id: int, teacher_assignment: TeacherAssignment, db: Session = Depends(get_db)):
    """
    Assign a teacher to a specified course.

    Args:
        course_id (int): The ID of the course to which a teacher will be assigned.
        teacher_assignment (TeacherAssignment): The request body containing the teacher_id.
        db (Session): The database session.

    Returns:
        dict: A message confirming the assignment of the teacher to the course.

    Raises:
        HTTPException: If the course does not exist or if any other error occurs.
    """
    # Retrieve the course
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Course not found."}})

    # Assign the teacher
    course.teacher_id = teacher_assignment.teacher_id
    db.commit()
    
    return {"message": "Teacher assigned successfully."}

@router.get("/{course_id}", response_model=CourseResponse)
def get_course_with_teacher(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve information for a specific course, including the associated teacher’s name.

    Args:
        course_id (int): The ID of the course to retrieve.
        db (Session): The database session.

    Returns:
        CourseResponse: Course details including teacher information.

    Raises:
        HTTPException: If the course does not exist.
    """
    # Retrieve the course with teacher info
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Course not found."}})

    # Prepare the response including teacher information
    course_response = CourseResponse(
        id=course.id,
        name=course.name,
        teacher_name=course.teacher.name if course.teacher else None  # Safely accessing teacher's name
    )

    return course_response
```