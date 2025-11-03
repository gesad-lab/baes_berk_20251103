```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Student, Course, StudentCourses
from pydantic import BaseModel, conlist
from typing import List

router = APIRouter()

class RemoveCourseAssociation(BaseModel):
    course_ids: conlist(int, min_items=1)  # List of course IDs to disassociate

@router.delete("/students/{student_id}/courses", response_model=dict)
def remove_course_association(student_id: int, course_data: RemoveCourseAssociation, db: Session = Depends(get_db)):
    """
    Remove one or more course associations from a student.
    
    Args:
        student_id (int): The ID of the student from whom courses will be disassociated.
        course_data (RemoveCourseAssociation): Contains a list of course IDs to be removed.
        db (Session): The database session.
    
    Returns:
        dict: Confirmation message if successful.
    
    Raises:
        HTTPException: If the student or course does not exist.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")

    # Validate course IDs and remove associations
    for course_id in course_data.course_ids:
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail=f"Course with ID {course_id} does not exist.")

        # Remove the association from the `student_courses` table
        association = db.query(StudentCourses).filter(StudentCourses.student_id == student_id, StudentCourses.course_id == course_id).first()
        if association:
            db.delete(association)  # Remove the association
            
    db.commit()  # Commit the changes to the database

    return {"message": "Course associations removed successfully."}
```