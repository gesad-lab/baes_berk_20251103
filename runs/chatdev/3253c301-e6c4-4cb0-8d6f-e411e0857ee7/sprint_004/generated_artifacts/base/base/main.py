'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import create_student, get_students  # Ensure this line is included
from schemas import StudentCreate, StudentResponse
app = FastAPI()
@app.post("/students/", response_model=StudentResponse)
def create_student_endpoint(student: StudentCreate, db: Session = Depends(get_db)):
    try:
        return create_student(db=db, student=student)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@app.get("/students/", response_model=list[StudentResponse])
def get_students_endpoint(db: Session = Depends(get_db)):
    students = get_students(db=db)
    if not students:
        raise HTTPException(status_code=404, detail="No students found")
    return students
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)