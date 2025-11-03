```python
# src/main.py
import logging
from fastapi import FastAPI

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Teacher-related events logging configuration
class TeacherLogger:
    @staticmethod
    def log_teacher_creation(name: str, email: str):
        logger.info(f"Teacher created: name={name}, email={email}")

    @staticmethod
    def log_teacher_retrieval(teacher_id: int):
        logger.info(f"Teacher retrieved: id={teacher_id}")

# Example usage of the logging for teaching-related events
@app.post("/teachers/")
async def create_teacher(name: str, email: str):
    # Validate and create teacher...
    TeacherLogger.log_teacher_creation(name, email)
    return {"msg": "Teacher created"}

@app.get("/teachers/{teacher_id}")
async def get_teacher(teacher_id: int):
    # Retrieve teacher from database...
    TeacherLogger.log_teacher_retrieval(teacher_id)
    return {"msg": "Teacher retrieved"}

# Rest of the FastAPI application...
```