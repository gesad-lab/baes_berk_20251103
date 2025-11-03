from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.models import Student
from src.schemas import StudentCreate, StudentResponse
from src.database import get_db

router = APIRouter()

@router.post("/students", response_model=StudentResponse)
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student record with name and email.
    
    Args:
        student (StudentCreate): The student data containing name and email.
        db (Session): Database session for making database operations.
        
    Returns:
        StudentResponse: A response containing the success message and student ID.
        
    Raises:
        HTTPException: If the email is already in use or database operation fails.
    """
    
    # Check if the email already exists in the database and raise an error if it does
    existing_student = db.query(Student).filter(Student.email == student.email).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Email already in use.")
    
    new_student = Student(name=student.name, email=student.email)

    try:
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return {"message": "Student created successfully", "student_id": new_student.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create student.")


@router.get("/students", response_model=list[StudentResponse])
async def retrieve_all_students(db: Session = Depends(get_db)):
    """
    Retrieve a list of all students including their names and email addresses.

    Args:
        db (Session): Database session for making database operations.

    Returns:
        List[StudentResponse]: A list containing all students with their names and email.
    
    Raises:
        HTTPException: If database operation fails.
    """
    
    try:
        students = db.query(Student).all()
        return students
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve students.")