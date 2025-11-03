'''
Course management functions for the application.
'''
from sqlalchemy.orm import Session
from models import Course
def create_course(db: Session, name: str, level: str, teacher_id: int):
    db_course = Course(name=name, level=level, teacher_id=teacher_id)  # Update this line
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course