from pydantic import BaseModel
from typing import List

class EnrollmentRequest(BaseModel):
    """
    Schema for enrolling students in courses.

    Attributes:
        course_ids (List[int]): A list of course IDs that the student wants to enroll in.
    """
    course_ids: List[int]

class CourseInfo(BaseModel):
    """
    Schema for course information.

    Attributes:
        name (str): The name of the course.
        level (str): The academic level of the course.
    """
    name: str
    level: str