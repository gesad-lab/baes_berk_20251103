'''
Contains functions for creating and retrieving Student records.
'''
from sqlalchemy.orm import Session
from models import Student
from schemas import StudentCreate
async def create_student(student: StudentCreate, db: Session):
    db_student = Student(name=student.name, email=student.email)  # Handle email field
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
async def get_students(db: Session):
    return db.query(Student).all()