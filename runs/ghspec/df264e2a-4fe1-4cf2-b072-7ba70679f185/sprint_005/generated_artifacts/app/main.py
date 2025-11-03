import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from app.models.teacher import Teacher  # Assuming this is where the Teacher model is defined
from app.database import db  # Assuming db is your database session or connection setup

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('api_logger')

app = FastAPI()

# Define the request model for creating a teacher
class TeacherCreateRequest(BaseModel):
    name: str
    email: EmailStr

# Define the response model upon successful creation
class TeacherCreateResponse(BaseModel):
    message: str

# Define the response for retrieving teacher details
class TeacherDetailResponse(BaseModel):
    name: str
    email: EmailStr

@app.post("/teachers", response_model=TeacherCreateResponse)
async def create_teacher(teacher_request: TeacherCreateRequest):
    """
    Create a new teacher in the system.

    :param teacher_request: The details of the teacher to create.
    :return: A success message upon the successful creation of a teacher.
    """
    # Log incoming request data
    logger.info("Received request to create teacher: %s", teacher_request.dict())
    
    # Validate inputs
    if not teacher_request.name or not teacher_request.email:
        error_message = "Missing required fields: name and email are required."
        logger.error(error_message)
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": error_message}})

    # Create teacher object and save to the database
    new_teacher = Teacher(name=teacher_request.name, email=teacher_request.email)
    db.add(new_teacher)  # Assuming db is your database session
    db.commit()  # Save changes to the database
    db.refresh(new_teacher)  # Get the updated data including any auto-generated fields

    # Log success message
    logger.info("Successfully created teacher: %s", new_teacher.id)

    return TeacherCreateResponse(message="Teacher added successfully.")

@app.get("/teachers/{teacher_id}", response_model=TeacherDetailResponse)
async def get_teacher(teacher_id: int):
    """
    Retrieve details of a specific teacher by their ID.

    :param teacher_id: The ID of the teacher to retrieve.
    :return: The details of the teacher or a 404 error if not found.
    """
    logger.info("Received request to retrieve teacher with ID: %d", teacher_id)

    # Retrieve teacher from the database
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()  # Assuming SQLAlchemy ORM

    if teacher is None:
        error_message = f"Teacher with ID {teacher_id} not found."
        logger.error(error_message)
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": error_message}})

    # Log successful retrieval
    logger.info("Successfully retrieved teacher: %s", teacher.name)

    return TeacherDetailResponse(name=teacher.name, email=teacher.email)