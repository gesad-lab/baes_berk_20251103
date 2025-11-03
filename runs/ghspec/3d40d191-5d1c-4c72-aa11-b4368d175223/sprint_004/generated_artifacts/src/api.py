from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Assuming EnrollStudent and data access functions are defined elsewhere
class EnrollStudent(BaseModel):
    course_id: Optional[int]

@app.post("/students/{student_id}/courses")
def enroll_student(student_id: int, enrollment: EnrollStudent):
    """
    Enroll a student in a specific course.

    Parameters:
    - student_id: The unique identifier for the student.
    - enrollment: Enrollment details containing 'course_id'.

    Returns:
    - Success message and enrollment details if successful.
    - HTTPException if course_id is missing or student_id is invalid.
    """
    if enrollment.course_id is None:
        raise HTTPException(status_code=400, detail="Course ID is required.")
    
    # Here you would typically check if the student exists and if the course_id is valid
    # This is simply a placeholder for the actual business logic
    # Example: if not student_exists(student_id): 
    #              raise HTTPException(status_code=404, detail="Student not found.")

    # Call the service layer to handle enrollment
    return enroll_student_service(student_id, enrollment.course_id)

@app.get("/students/{student_id}/courses")
def get_student_courses(student_id: int) -> List[dict]:
    """
    Retrieve all courses for a specific student.

    Parameters:
    - student_id: The unique identifier for the student.

    Returns:
    - List of courses the student is enrolled in.
    - HTTPException if the student does not exist.
    """
    # Check if student exists first
    if not student_exists(student_id):
        raise HTTPException(status_code=404, detail="Student not found.")
    
    # Retrieve student courses using the service layer
    return get_student_courses_service(student_id)