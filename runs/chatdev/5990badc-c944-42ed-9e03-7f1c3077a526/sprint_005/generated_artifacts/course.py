'''
Course management functions for the application.
'''
from sqlalchemy.orm import Session
from models import Course
def create_course(db: Session, name: str, level: str):
    db_course = Course(name=name, level=level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course