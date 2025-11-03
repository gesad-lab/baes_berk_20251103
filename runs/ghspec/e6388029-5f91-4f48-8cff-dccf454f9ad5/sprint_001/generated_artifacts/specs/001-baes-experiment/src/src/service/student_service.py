```python
from typing import List, Optional
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .models import Student
from .schemas import StudentCreate, StudentUpdate

class StudentService:
    def __init__(self, db: Session):
        self.db = db

    def create_student(self, student: StudentCreate) -> Student:
        """Create a new student in the database."""
        db_student = Student(name=student.name)
        self.db.add(db_student)
        self.db.commit()
        self.db.refresh(db_student)
        return db_student

    def get_all_students(self) -> List[Student]:
        """Retrieve all students from the database."""
        return self.db.query(Student).all()

    def update_student(self, student_id: int, student_update: StudentUpdate) -> Student:
        """Update an existing student's name."""
        db_student = self.db.query(Student).filter(Student.id == student_id).first()
        if not db_student:
            raise HTTPException(status_code=404, detail="Student not found.")
        
        if student_update.name and isinstance(student_update.name, str) and student_update.name.strip():
            db_student.name = student_update.name
            self.db.commit()
            self.db.refresh(db_student)
            return db_student
        
        raise HTTPException(status_code=400, detail="Invalid name provided.")

    def delete_student(self, student_id: int) -> None:
        """Delete a student by ID."""
        db_student = self.db.query(Student).filter(Student.id == student_id).first()
        if not db_student:
            raise HTTPException(status_code=404, detail="Student not found.")
        
        self.db.delete(db_student)
        self.db.commit()
```
