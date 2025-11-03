from pydantic import BaseModel, constr

class StudentCreate(BaseModel):
    name: constr(min_length=1)  # Name must not be empty

class StudentResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True