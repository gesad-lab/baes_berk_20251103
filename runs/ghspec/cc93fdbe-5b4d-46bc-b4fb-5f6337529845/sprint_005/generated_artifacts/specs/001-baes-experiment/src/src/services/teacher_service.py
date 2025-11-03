```python
from sqlalchemy.orm import Session
from models import Teacher  # Import the Teacher model
from fastapi import HTTPException, status

class TeacherService:
    @staticmethod
    def create_teacher(db: Session, name: str, email: str) -> Teacher:
        """
        Create a new teacher record in the database.

        Parameters:
        - db: Database session
        - name: Name of the teacher
        - email: Email of the teacher

        Returns:
        - Created Teacher object

        Raises:
        - HTTPException on validation errors (missing fields, duplicate email)
        """
        # Validate input
        if not name or not email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Name and email are required fields."
            )
        
        # Check if email already exists
        existing_teacher = db.query(Teacher).filter(Teacher.email == email).first()
        if existing_teacher:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email must be unique."
            )

        # Create and add the new teacher record to the session
        new_teacher = Teacher(name=name, email=email)
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
        
        return new_teacher  # Return the created Teacher object
```