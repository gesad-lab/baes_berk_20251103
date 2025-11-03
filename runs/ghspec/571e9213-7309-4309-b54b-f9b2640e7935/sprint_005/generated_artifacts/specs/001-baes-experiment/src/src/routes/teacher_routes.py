from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.teacher import Teacher
from schemas.teacher_schema import CreateTeacherRequestSchema, TeacherSchema
from database import get_db

router = APIRouter()

@router.post("/teachers", response_model=TeacherSchema)
def create_teacher(teacher: CreateTeacherRequestSchema, db: Session = Depends(get_db)):
    """
    Create a new Teacher entry in the system.
    
    Parameters:
        teacher (CreateTeacherRequestSchema): The teacher data to create.
        db (Session): The database session dependency.

    Returns:
        TeacherSchema: The created Teacher object.
    
    Raises:
        HTTPException: If the Teacher could not be created.
    """
    # Check if a teacher with the same email already exists
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail="Teacher with this email already exists.")
    
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    
    try:
        db.commit()  # Commit the transaction
        db.refresh(new_teacher)  # Refresh to get the new state of the Teacher
    except Exception as e:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail="An error occurred while creating the teacher.")

    return new_teacher

@router.get("/teachers/{teacher_id}", response_model=TeacherSchema)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Retrieve details of a specific Teacher by ID.
    
    Parameters:
        teacher_id (int): The ID of the teacher to retrieve.
        db (Session): The database session dependency.
    
    Returns:
        TeacherSchema: The details of the Teacher.

    Raises:
        HTTPException: If the Teacher is not found.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found.")
    
    return teacher

@router.get("/teachers", response_model=list[TeacherSchema])
def list_teachers(db: Session = Depends(get_db)):
    """
    Retrieve all Teachers in the system.

    Parameters:
        db (Session): The database session dependency.

    Returns:
        list[TeacherSchema]: A list of Teacher objects.
    """
    teachers = db.query(Teacher).all()
    return teachers