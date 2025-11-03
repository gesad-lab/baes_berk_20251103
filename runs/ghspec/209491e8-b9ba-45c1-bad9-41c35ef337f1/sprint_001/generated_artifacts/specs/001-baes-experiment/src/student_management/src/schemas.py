from pydantic import BaseModel, constr, validator

class StudentCreateSchema(BaseModel):
    """
    Schema for creating a new student. Validates input data.
    
    Attributes:
        name (str): The name of the student, which is required.
    """
    name: constr(min_length=1)  # Ensures that the name is a non-empty string

    @validator('name')
    def validate_name(cls, value):
        """
        Validate the student name to ensure it contains only alphabetic characters.
        
        Args:
            cls (Type[StudentCreateSchema]): The class itself.
            value (str): The provided student name.
        
        Returns:
            str: The validated name.
        
        Raises:
            ValueError: If the name is not alphabetic or is empty.
        """
        if not value.isalpha():
            raise ValueError('Name must contain only alphabetic characters.')
        return value

class StudentResponseSchema(BaseModel):
    """
    Schema for returning student details after creation.

    Attributes:
        id (int): The unique identifier for the student.
        name (str): The name of the student.
    """
    id: int
    name: str

    class Config:
        orm_mode = True  # Needed to work correctly with SQLAlchemy models in FastAPI
