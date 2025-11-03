```python
from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr

# Assuming data is stored in a database and we have appropriate methods for data access
from src.database import get_students_from_db  # Assume this function fetches student data

router = APIRouter()

class Student(BaseModel):
    id: int
    name: str
    email: EmailStr

def list_students() -> List[Student]:
    """
    Fetch all students from the database and return them.
    
    Returns:
        List[Student]: A list of Student objects containing id, name, and email.
    
    Raises:
        HTTPException: If there is an error retrieving student data.
    """
    try:
        # Fetch data from the database; assuming this returns dicts or proper Student objects
        students_data = get_students_from_db()
        # Transform dictionary data into Student list
        return [Student(**student) for student in students_data]  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching students: {str(e)}")

@router.get("/students", response_model=List[Student])
async def get_students():
    """
    Get a list of all students with their details including email.

    Returns:
        List[Student]: A list of students.
    """
    return list_students()
```