```python
from fastapi import APIRouter, HTTPException
from src.models.teacher import Teacher  # Assuming the Teacher model is defined in this location
from src.database import get_teacher_by_id, delete_teacher  # Assuming these database methods exist

router = APIRouter()

@router.delete("/teachers/{id}", status_code=204)
async def delete_teacher_by_id(id: int):
    """
    Delete a Teacher by ID.

    Args:
        id (int): The ID of the Teacher to delete.

    Raises:
        HTTPException: If the Teacher with the given ID does not exist.
    
    Returns:
        None: Sends a 204 No Content response upon successful deletion.
    """
    teacher = await get_teacher_by_id(id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    await delete_teacher(id)  # Assuming this method deletes a teacher by ID
```
