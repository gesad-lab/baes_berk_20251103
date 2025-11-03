from pydantic import BaseModel

# Pydantic model for request validation when enrolling a student in a course
class EnrollRequest(BaseModel):
    course_id: int  # The ID of the course the student wishes to enroll in

# Pydantic model for request validation when unenrolling a student from a course
class UnenrollRequest(BaseModel):
    course_id: int  # The ID of the course the student wishes to unenroll from