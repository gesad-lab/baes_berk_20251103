```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from database import get_db
from models import Student
from repository import save_student, get_student_by_id

app = FastAPI()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Use Pydantic to validate email format

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/students/", response_model=StudentResponse)
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    # Call repository layer to save the new student
    new_student = await save_student(db=db, student=student)
    return new_student  # Return the created student object

@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int, db: Session = Depends(get_db)):
    student = await get_student_by_id(db=db, student_id=student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student  # Return the student data including email
```