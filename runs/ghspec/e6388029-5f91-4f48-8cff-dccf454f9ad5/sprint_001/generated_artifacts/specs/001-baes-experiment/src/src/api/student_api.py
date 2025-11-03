from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import get_db, Base, engine
from .models import Student
from .schemas import StudentCreate, StudentResponse

app = FastAPI()

# Create the database tables on startup
@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

@app.delete("/students/{student_id}", response_model=StudentResponse)
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    """
    Delete a student by their ID.

    Parameters:
    - student_id: ID of the student to delete.
    - db: Database session.

    Returns:
    - StudentResponse: The deleted student record.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    db.delete(student)
    db.commit()
    return StudentResponse(id=student.id, name=student.name)