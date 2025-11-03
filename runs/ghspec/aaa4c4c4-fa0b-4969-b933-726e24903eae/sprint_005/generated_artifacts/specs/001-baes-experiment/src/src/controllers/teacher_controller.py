```python
from fastapi import HTTPException
from app.models.teacher import Teacher  # Assuming the Teacher model is defined here
from sqlalchemy.orm import Session

def create_teacher(teacher_data: dict, db: Session):
    """Create a new teacher with the provided data.

    Args:
        teacher_data (dict): A dictionary containing the teacher's data.
        db (Session): The database session to use for creating the teacher.
    
    Raises:
        HTTPException: If required fields are missing or email is not unique.
    
    Returns:
        Teacher: The newly created teacher object.
    """
    # Validate required fields
    if "name" not in teacher_data or "email" not in teacher_data:
        missing_fields = []
        if "name" not in teacher_data:
            missing_fields.append("name")
        if "email" not in teacher_data:
            missing_fields.append("email")
        raise HTTPException(status_code=400, detail={
            "error": {
                "code": "E001",
                "message": "Required fields are missing.",
                "details": {"fields": missing_fields}
            }
        })

    # Check for unique email
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher_data["email"]).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail={
            "error": {
                "code": "E002",
                "message": "Email is already in use.",
                "details": {"email": teacher_data["email"]}
            }
        })

    # Create a new teacher instance and add to the database
    new_teacher = Teacher(name=teacher_data["name"], email=teacher_data["email"])
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return new_teacher
```