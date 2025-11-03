from pydantic import BaseModel, Field

class Student(BaseModel):
    """
    Represents a Student entity for request and response validation.

    Attributes:
    - id (int): The unique identifier of the student (automatically generated).
    - name (str): The name of the student, which is required.
    """
    id: int = Field(default=None, description="The unique identifier of the student.")
    name: str = Field(..., description="The name of the student, which is required.")