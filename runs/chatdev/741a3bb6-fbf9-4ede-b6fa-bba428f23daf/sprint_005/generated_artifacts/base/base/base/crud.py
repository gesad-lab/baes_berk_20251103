'''
Contains the CRUD operations for the Student entity.
'''
from sqlalchemy.orm import Session
from models import Student
from schemas import StudentCreate
def create_student(db: Session, student: StudentCreate):
    '''
    Creates a new student in the database.
    '''
    db_student = Student(name=student.name, email=student.email)  # Updated to include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
def get_students(db: Session, skip: int = 0, limit: int = 10):
    '''
    Retrieves a list of students from the database with pagination.
    '''
    return db.query(Student).offset(skip).limit(limit).all()