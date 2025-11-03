from pydantic import BaseModel, Field

class CourseCreateSchema(BaseModel):
    """
    Pydantic Schema for Course creation.

    Attributes:
    - name (str): The name of the course, required field.
    - level (str): The level of the course, required field.
    """
    name: str = Field(..., description="The name of the course")
    level: str = Field(..., description="The level of the course")

    class Config:
        schema_extra = {
            "example": {
                "name": "Introduction to Programming",
                "level": "Beginner"
            }
        }