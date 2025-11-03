```python
# main.py

from fastapi import FastAPI, HTTPException
import logging

app = FastAPI()

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@app.post("/teachers")
async def create_teacher(name: str, email: str):
    """
    Create a new Teacher entity with the given name and email.

    Args:
    - name (str): The name of the teacher.
    - email (str): The email of the teacher.

    Returns:
    - JSON response containing success message and teacher details.
    """
    if not name or not email:
        logger.warning("Missing required fields for teacher creation; name: '%s', email: '%s'", name, email)
        raise HTTPException(status_code=400, detail="Name and email are required.")

    # Logic to save teacher in the database goes here (pseudo-code)
    # teacher_id = await save_teacher_to_db(name, email)

    logger.info("Created teacher with name: '%s', email: '%s'", name, email)
    return {"message": "Teacher created successfully", "teacher_id": teacher_id}

@app.get("/teachers/{teacher_id}")
async def get_teacher(teacher_id: int):
    """
    Retrieve the details of a teacher by ID.

    Args:
    - teacher_id (int): The ID of the teacher to retrieve.

    Returns:
    - JSON response containing the teacher's details.
    """
    # Logic to retrieve teacher from the database goes here (pseudo-code)
    # teacher = await get_teacher_from_db(teacher_id)

    if not teacher:  # Assuming this check reflects if the teacher exists
        logger.error("Teacher with ID '%d' not found", teacher_id)
        raise HTTPException(status_code=404, detail="Teacher not found.")

    logger.info("Retrieved details for teacher with ID: '%d'", teacher_id)
    return {"name": teacher.name, "email": teacher.email}
```