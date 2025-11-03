```python
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models.student_courses import StudentCourses
from schemas.course_association_schema import CourseAssociationRequestSchema
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.post("/students/{student_id}/courses")
def associate_course(student_id: int, course: CourseAssociationRequestSchema, db: Session = Depends(get_db)):
    """
    Associate a course with a student by their IDs.
    
    :param student_id: ID of the student to associate with a course.
    :param course: Object containing course ID to associate.
    :param db: Database session dependency.
    :raises HTTPException: If the student or course does not exist.
    :return: Success message indicating the association.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Student does not exist"}})

    # Check if the course exists
    course_record = db.query(Course).filter(Course.id == course.course_id).first()
    if not course_record:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Course does not exist"}})

    # Create the association
    student_course_association = StudentCourses(student_id=student_id, course_id=course.course_id)
    
    db.add(student_course_association)
    db.commit()
    return {"message": "Course associated successfully"}

@router.get("/students/{student_id}/courses", response_model=List[CourseResponseSchema])
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all courses associated with a specific student.

    :param student_id: ID of the student whose courses to retrieve.
    :param db: Database session dependency.
    :return: List of courses associated with the student.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Student does not exist"}})

    # Retrieve courses associated with the student
    courses = db.query(Course).join(StudentCourses).filter(StudentCourses.student_id == student_id).all()
    return courses

@router.delete("/students/{student_id}/courses/{course_id}")
def remove_course_association(student_id: int, course_id: int, db: Session = Depends(get_db)):
    """
    Remove a specific course association from a student.

    :param student_id: ID of the student to disassociate the course from.
    :param course_id: ID of the course to remove from the student.
    :param db: Database session dependency.
    :raises HTTPException: If the association does not exist.
    :return: Success message confirming the removal.
    """
    # Check if the association exists
    association = db.query(StudentCourses).filter(
        StudentCourses.student_id == student_id,
        StudentCourses.course_id == course_id
    ).first()

    if not association:
        raise HTTPException(status_code=404, detail={"error": {"code": "E003", "message": "Association does not exist"}})

    db.delete(association)
    db.commit()
    return {"message": "Course association removed successfully"}
```