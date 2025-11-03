'''
Teacher management functions for the application.
'''
from sqlalchemy.orm import Session
from models import Teacher
def create_teacher(db: Session, name: str, email: str):
    db_teacher = Teacher(name=name, email=email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher