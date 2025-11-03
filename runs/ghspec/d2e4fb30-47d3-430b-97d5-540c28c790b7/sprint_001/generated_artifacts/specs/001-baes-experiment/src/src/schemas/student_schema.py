from pydantic import BaseModel, constr

class StudentCreate(BaseModel):
    """
    Schema for creating a student. 

    Attributes:
        name (str): The name of the student, must be a non-empty string.
    """
    name: constr(min_length=1)  # Ensures that name is a non-empty string

class StudentResponse(BaseModel):
    """
    Schema for representing a student response.

    Attributes:
        id (int): The unique identifier for the student.
        name (str): The name of the student.
    """
    id: int
    name: str

class StudentListResponse(BaseModel):
    """
    Schema for representing a list of students response.

    Attributes:
        students (list[StudentResponse]): A list of student responses.
    """
    students: list[StudentResponse]