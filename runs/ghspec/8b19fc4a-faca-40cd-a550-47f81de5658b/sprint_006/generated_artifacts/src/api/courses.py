from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.course import Course
from models.teacher import Teacher
from db import get_db  # Assuming this provides the database session
from api.errors import CourseErrors  # Importing existing error handling

router = APIRouter()

@router.post('/courses/{course_id}/assign-teacher')
async def assign_teacher(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    """Assign a Teacher to a Course by course_id.

    Args:
        course_id (int): The ID of the Course.
        teacher_id (int): The ID of the Teacher to assign.
        db (Session): Database session dependency.

    Returns:
        JSON: Confirmation message of the assignment.

    Raises:
        HTTPException: If the course does not exist or a Teacher is already assigned.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail=CourseErrors.COURSE_NOT_FOUND[1])

    if course.teacher_id is not None:
        raise HTTPException(status_code=400, detail="A Teacher is already assigned to this Course.")

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.commit()
    
    return {"message": "Teacher successfully assigned to the Course."}

@router.get('/courses/{course_id}')
async def get_course(course_id: int, db: Session = Depends(get_db)):
    """Retrieve details for a specific Course including assigned Teacher.

    Args:
        course_id (int): The ID of the Course.
        db (Session): Database session dependency.

    Returns:
        JSON: Details of the Course including Teacher information.

    Raises:
        HTTPException: If the course does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail=CourseErrors.COURSE_NOT_FOUND[1])
    
    # Prepare response data
    course_info = {
        "id": course.id,
        "teacher_id": course.teacher_id,
        "name": course.name,
        # Include any other course details if needed
    }
    
    # Fetch teacher details if assigned
    if course.teacher_id:
        teacher = db.query(Teacher).filter(Teacher.id == course.teacher_id).first()
        if teacher:
            course_info["teacher"] = {"id": teacher.id, "name": teacher.name, "email": teacher.email}
    
    return course_info