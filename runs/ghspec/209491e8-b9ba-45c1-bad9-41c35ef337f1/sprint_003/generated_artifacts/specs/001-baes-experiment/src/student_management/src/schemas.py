from pydantic import BaseModel, constr, validator

class CourseBase(BaseModel):
    name: constr(min_length=1, max_length=100)  # Course name must be between 1 and 100 characters
    level: constr(min_length=1, max_length=50)  # Course level must be between 1 and 50 characters

    @validator('name')
    def validate_name(cls, value):
        if not value.strip():  # Ensure the name is not just whitespace
            raise ValueError("Course name cannot be empty or whitespace only")
        return value

    @validator('level')
    def validate_level(cls, value):
        if not value.strip():  # Ensure the level is not just whitespace
            raise ValueError("Course level cannot be empty or whitespace only")
        return value
    

class CourseCreate(CourseBase):
    """Schema for creating a new Course."""
    pass


class Course(CourseBase):
    id: int  # Assuming the ID will be provided in the response

    class Config:
        orm_mode = True  # To read data as dict from ORM objects
