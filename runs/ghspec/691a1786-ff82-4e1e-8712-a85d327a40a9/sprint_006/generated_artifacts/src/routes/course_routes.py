```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.models.course import Course
from src.models.teacher import Teacher

router = APIRouter()

@router.post("/courses/{course_id}/teachers")
async def associate_teacher_to_course(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    """
    Associate a Teacher with a Course.
    
    Parameters:
    - course_id: ID of the course to associate the teacher with.
    - teacher_id: ID of the teacher to be associated.

    Returns:
    - Updated course details including Teacher's name.
    
    Raises:
    - HTTPException: If the course or teacher does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    course.teacher_id = teacher_id
    db.commit()
    db.refresh(course)
    
    return {"data": course}

@router.get("/courses/{course_id}")
async def get_course(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve details of a specific Course using the course identifier.

    Parameters:
    - course_id: ID of the course to retrieve.

    Returns:
    - Full course details including associated Teacher information.
    
    Raises:
    - HTTPException: If the Course does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return {"data": course}

@router.put("/courses/{course_id}/teachers")
async def update_teacher_for_course(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    """
    Update the Teacher assigned to a Course.

    Parameters:
    - course_id: ID of the course to update.
    - teacher_id: New teacher ID to be assigned.

    Returns:
    - Updated course details including the newly assigned Teacher.
    
    Raises:
    - HTTPException: If the Course or Teacher does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    course.teacher_id = teacher_id
    db.commit()
    db.refresh(course)

    return {"data": course}

@router.delete("/courses/{course_id}/teachers")
async def remove_teacher_from_course(course_id: int, db: Session = Depends(get_db)):
    """
    Disassociate a Teacher from a Course.

    Parameters:
    - course_id: ID of the course to disassociate the teacher from.

    Returns:
    - Updated course state upon confirmation.
    
    Raises:
    - HTTPException: If the Course does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Clear the teacher_id to disassociate the teacher
    course.teacher_id = None
    db.commit()
    db.refresh(course)

    return {"data": course}
```