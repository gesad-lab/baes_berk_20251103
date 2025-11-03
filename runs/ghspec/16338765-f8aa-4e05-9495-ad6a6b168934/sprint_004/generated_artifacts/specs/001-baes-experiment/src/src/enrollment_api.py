from fastapi import APIRouter, HTTPException
from models import StudentCourse, Course, CourseEnrollment, EnrollmentResponse
from db_setup import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/students/{student_id}/courses", response_model=EnrollmentResponse, status_code=201)
def enroll_student_in_course(student_id: int, enrollment: CourseEnrollment):
    """
    Enroll a student in a course.
    
    Parameters:
    - student_id (int): The ID of the student to enroll.
    - enrollment (CourseEnrollment): The enrollment data containing course_id.
    
    Raises:
    - HTTPException: If the course does not exist.
    - HTTPException: If the student ID is invalid.
    """
    with SessionLocal() as session:
        # Check if the student ID is valid
        student_exists = session.query(StudentCourse).filter(StudentCourse.student_id == student_id).first()
        if not student_exists:
            raise HTTPException(status_code=404, detail=f"Student with ID {student_id} does not exist.")

        # Check if the course exists
        course = session.query(Course).filter(Course.id == enrollment.course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail=f"Course with ID {enrollment.course_id} does not exist.")

        # Create the enrollment
        student_course = StudentCourse(student_id=student_id, course_id=enrollment.course_id)
        session.add(student_course)
        session.commit()
        
        return EnrollmentResponse(student_id=student_id, course_id=enrollment.course_id)

@router.get("/students/{student_id}/courses", response_model=list[EnrollmentResponse])
def get_courses_for_student(student_id: int):
    """
    Get all courses enrolled by a student.
    
    Parameters:
    - student_id (int): The ID of the student.
    
    Raises:
    - HTTPException: If the student ID is invalid.
    """
    with SessionLocal() as session:
        # Check if the student ID is valid
        student_exists = session.query(StudentCourse).filter(StudentCourse.student_id == student_id).first()
        if not student_exists:
            raise HTTPException(status_code=404, detail=f"Student with ID {student_id} does not exist.")

        # Retrieve the courses for the student
        enrollments = session.query(StudentCourse).filter(StudentCourse.student_id == student_id).all()
        return [{"student_id": enrollment.student_id, "course_id": enrollment.course_id} for enrollment in enrollments]

@router.put("/students/{student_id}/courses/{course_id}", response_model=EnrollmentResponse)
def update_course_enrollment(student_id: int, course_id: int, enrollment: CourseEnrollment):
    """
    Update an existing course enrollment for a student.
    
    Parameters:
    - student_id (int): The student's ID.
    - course_id (int): The current course ID to be updated.
    - enrollment (CourseEnrollment): The new enrollment data.
    
    Raises:
    - HTTPException: If the student or course does not exist.
    """
    with SessionLocal() as session:
        # Validate student
        student_exists = session.query(StudentCourse).filter(StudentCourse.student_id == student_id).first()
        if not student_exists:
            raise HTTPException(status_code=404, detail=f"Student with ID {student_id} does not exist.")

        # Check if the course exists
        course = session.query(Course).filter(Course.id == enrollment.course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail=f"Course with ID {enrollment.course_id} does not exist.")

        # Update the enrollment
        student_course = session.query(StudentCourse).filter(StudentCourse.student_id == student_id, StudentCourse.course_id == course_id).first()
        if not student_course:
            raise HTTPException(status_code=404, detail="Enrollment record not found.")

        student_course.course_id = enrollment.course_id
        session.commit()
        
        return EnrollmentResponse(student_id=student_id, course_id=enrollment.course_id)

# Ensure to include the router in the main application file for it to be recognized
# app.include_router(router)