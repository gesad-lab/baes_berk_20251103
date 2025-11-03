```python
from fastapi import FastAPI, HTTPException
import logging
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Sample student data in memory for demonstration
students = {}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Student Entity Web Application"}

@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify that the application is running.
    """
    return {"status": "healthy"}

@app.post("/students/{student_id}")
async def create_student(student_id: int, name: str):
    """
    Create a student entry.

    :param student_id: The ID of the student to be created.
    :param name: The name of the student.
    :returns: A confirmation message with student details.
    """
    if student_id in students:
        logger.warning(f"Attempted to create student with existing id: {student_id}")
        raise HTTPException(status_code=400, detail="Student ID already exists")
    
    students[student_id] = {"name": name}
    logger.info(f"Created student {student_id}: {name}")
    return {"message": "Student created", "student_id": student_id, "name": name}

@app.get("/students/{student_id}")
async def read_student(student_id: int):
    """
    Retrieve a student entry.

    :param student_id: The ID of the student to be retrieved.
    :returns: The details of the requested student.
    """
    student = students.get(student_id)
    if not student:
        logger.error(f"Student not found with id: {student_id}")
        raise HTTPException(status_code=404, detail="Student not found")
    
    logger.info(f"Retrieved student {student_id}: {student}")
    return {"student_id": student_id, "name": student["name"]}

def shutdown():
    """
    Handle the application shutdown gracefully.
    """
    logger.info("Shutting down the application...")

if __name__ == "__main__":
    # Enable graceful shutdown and start the application
    uvicorn.run(app, host="0.0.0.0", port=8000, lifespan="on_startup", shutdown=shutdown)
```