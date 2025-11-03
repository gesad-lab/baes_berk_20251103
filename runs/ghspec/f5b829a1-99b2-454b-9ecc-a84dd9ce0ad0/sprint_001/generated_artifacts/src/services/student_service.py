```python
from fastapi import HTTPException, status
from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field(..., example="John Doe", description="The name of the student")

class StudentService:
    """Service layer for managing Student entities."""
    
    def create_student(self, student_data: Student):
        """
        Create a new student record.

        Parameters:
        - student_data: An instance of Student containing the details of the student.

        Returns:
        - Student: Created student object.

        Raises:
        - HTTPException: If the name is missing or invalid.
        """
        # Validate input
        if not student_data.name.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "error": {
                        "code": "E001",
                        "message": "Name field is required.",
                        "details": {}
                    }
                }
            )

        # Proceed with creating the student (dummy logic here, replace with actual saving logic)
        # For example, you might typically do something like:
        # new_student = YourORMModel(name=student_data.name)
        # db_session.add(new_student)
        # db_session.commit()
        # return new_student
        
        return {"name": student_data.name}  # This is a placeholder for the created student record

    # Additional methods for retrieving students can be implemented here
```