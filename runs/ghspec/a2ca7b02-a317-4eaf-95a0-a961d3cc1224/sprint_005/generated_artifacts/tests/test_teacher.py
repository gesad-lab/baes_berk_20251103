```python
# validators/teacher_validator.py

from fastapi import HTTPException
from models.teacher import Teacher  # Assuming a Teacher model exists
from db.database import Session

class TeacherValidator:
    @staticmethod
    def validate_teacher_data(data: dict):
        """
        Validate incoming teacher data. 

        Parameters:
        - data (dict): The teacher data containing 'name' and 'email'.

        Raises:
        - HTTPException: If validation fails, with a specific status code and detail message.
        """
        # Check if 'name' is provided and not empty
        if not data.get("name"):
            raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Name is required."}})

        # Check if 'email' is provided and not empty
        if not data.get("email"):
            raise HTTPException(status_code=400, detail={"error": {"code": "E002", "message": "Email is required."}})

        # Check for email uniqueness
        with Session() as session:
            existing_teacher = session.query(Teacher).filter_by(email=data["email"]).first()
            if existing_teacher:
                raise HTTPException(status_code=400, detail={"error": {"code": "E003", "message": "Email is already in use."}})

```