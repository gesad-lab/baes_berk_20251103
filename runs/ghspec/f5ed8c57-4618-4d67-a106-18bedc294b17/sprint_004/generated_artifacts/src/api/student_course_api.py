from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Student, Course, StudentCourse  # Assuming these models are defined appropriately

router = APIRouter()

@router.post("/students/{student_id}/courses", status_code=201)
async def assign_course_to_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    """
    Assign a course to a student by creating an entry in the student_courses association table.
    
    Parameters:
    - student_id: ID of the student to whom the course is assigned.
    - course_id: ID of the course to be assigned.
    
    Returns:
    - A message confirming the course assignment along with student_id and course_id.
    
    Raises:
    - HTTPException: If either the student or course does not exist.
    """
    # Check if student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Check if course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Create student-course association
    student_course = StudentCourse(student_id=student_id, course_id=course_id)
    db.add(student_course)
    db.commit()
    db.refresh(student_course)

    return {
        "message": "Course assigned successfully",
        "student_id": student_course.student_id,
        "course_id": student_course.course_id
    }

@router.get("/students/{student_id}/courses")
async def retrieve_student_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a list of courses associated with a specific student.
    
    Parameters:
    - student_id: ID of the student whose courses are to be retrieved.
    
    Returns:
    - A list of courses associated with the student including course IDs, names, and levels.
    
    Raises:
    - HTTPException: If the student does not exist.
    """
    # Check if student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Retrieve courses for the student
    courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    
    return [{
        "id": course.id,
        "name": course.name,
        "level": course.level
    } for course in courses]

@router.get("/courses/{course_id}/students")
async def list_students_in_course(course_id: int, db: Session = Depends(get_db)):
    """
    List all students enrolled in a particular course.
    
    Parameters:
    - course_id: ID of the course whose students are to be listed.
    
    Returns:
    - A list of students enrolled in the course including student IDs and names.
    
    Raises:
    - HTTPException: If the course does not exist.
    """
    # Check if course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    # Retrieve students for the course
    students = db.query(Student).join(StudentCourse).filter(StudentCourse.course_id == course_id).all()
    
    return [{
        "id": student.id,
        "name": student.name
    } for student in students]