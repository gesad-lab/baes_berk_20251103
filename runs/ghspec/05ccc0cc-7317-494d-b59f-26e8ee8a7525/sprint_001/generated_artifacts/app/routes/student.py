```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.models import Student  # Assuming Student model is implemented in app/models.py
from app.database import get_db  # Assuming this provides a function to get the database session

router = APIRouter()

@router.get("/students", response_model=list[Student])
def get_all_students(db: Session = next(get_db())):
    """
    Retrieve all student records from the database.

    Args:
        db (Session): The SQLAlchemy session to interact with the database.

    Returns:
        List[Student]: A list of student objects in JSON format.
    
    Raises:
        HTTPException: If there is an error accessing the database.
    """
    try:
        # Querying all student records
        students = db.query(Student).all()
        return students
    except Exception as e:
        # Log the error and raise an HTTP exception
        # Here we just print it; in a real application, use a logger
        print(f"Error retrieving students: {e}")
        raise HTTPException(status_code=500, detail="Unable to retrieve students.")
```