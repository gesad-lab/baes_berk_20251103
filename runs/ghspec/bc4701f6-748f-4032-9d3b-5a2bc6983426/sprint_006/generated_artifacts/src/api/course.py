```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.models import Course, Teacher
from src.database import get_db

router = APIRouter()

class CourseWithTeacher(BaseModel):
    id: int
    name: str
    description: str
    teacher_name: str = None
    teacher_email: str = None

@router.get("/courses/{course_id}", response_model=CourseWithTeacher)
def get_course_details(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve details for a specific course, including associated teacher information.

    Parameters:
        course_id (int): The ID of the course to retrieve.

    Returns:
        CourseWithTeacher: A course object that includes teacher details if assigned.

    Raises:
        HTTPException: If the course does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    teacher = db.query(Teacher).filter(Teacher.id == course.teacher_id).first()
    
    return CourseWithTeacher(
        id=course.id,
        name=course.name,
        description=course.description,
        teacher_name=teacher.name if teacher else None,
        teacher_email=teacher.email if teacher else None,
    )

@router.patch("/courses/{course_id}")
def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    """
    Assign a teacher to a specific course.

    Parameters:
        course_id (int): The ID of the course to which the teacher will be assigned.
        teacher_id (int): The ID of the teacher to assign to the course.

    Returns:
        JSON: Updated course details if successful.

    Raises:
        HTTPException: If the course or teacher does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    course.teacher_id = teacher_id
    db.commit()
    db.refresh(course)
    
    return {"course_id": course.id, "teacher_id": teacher_id}
```