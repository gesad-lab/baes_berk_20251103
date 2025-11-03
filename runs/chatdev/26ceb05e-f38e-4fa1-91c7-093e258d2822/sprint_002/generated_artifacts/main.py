'''
Entry point of the application that initializes the FastAPI app and sets up the routes.
'''
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import create_student, get_students
from schemas import StudentCreate, StudentResponse
app = FastAPI()
@app.post("/students/", response_model=StudentResponse)
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db=db, student=student)
@app.get("/students/", response_model=list[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return get_students(db=db)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)