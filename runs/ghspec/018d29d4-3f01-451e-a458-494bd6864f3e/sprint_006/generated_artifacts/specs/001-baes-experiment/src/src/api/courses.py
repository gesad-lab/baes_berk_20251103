from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Course, Teacher, get_db  # Import relevant models and database session
from schemas import TeacherAssignment  # Assuming this schema exists for request body validation

router = APIRouter()

@router.post("/courses/{course_id}/assign_teacher")
async def assign_teacher_to_course(course_id: int, assignment: TeacherAssignment, db: Session = Depends(get_db)):
    """
    Assign a teacher to a specific course.

    Parameters:
    - course_id: The ID of the course to which the teacher will be assigned.
    - assignment: Request body containing teacher_id.

    Returns:
    - A message confirming the assignment of the teacher to the course.
    
    Raises:
    - 404: If the course or teacher does not exist.
    """
    # Fetch the course by ID
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found.")

    # Fetch the teacher by ID
    teacher = db.query(Teacher).filter(Teacher.id == assignment.teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found.")

    # Assign the teacher to the course
    course.teacher_id = assignment.teacher_id
    
    # Commit the changes to the database
    db.commit()

    return {"detail": "Teacher assigned to course successfully."}