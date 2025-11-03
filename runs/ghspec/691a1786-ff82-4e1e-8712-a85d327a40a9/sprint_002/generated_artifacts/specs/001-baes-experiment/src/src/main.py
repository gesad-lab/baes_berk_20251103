from fastapi import FastAPI, HTTPException
from loguru import logger
from routes.student_routes import student_router
from db.database import init_db

app = FastAPI()

# Initialize logging
logger.add("email_operations.log", rotation="1 week", level="INFO")

@app.on_event("startup")
async def startup_event():
    # Initialize database connections
    await init_db()

@app.post("/students/", response_model=dict)
async def create_student(student: dict):
    """
    Create a new student with name and email.

    :param student: Dictionary containing name and email of the student
    :return: The created student's information
    """
    logger.info("Creating a new student: {}", student)
    # Presumed function to handle student creation
    new_student = await student_router.create_student(student)
    logger.info("Successfully created student: {}", new_student)
    return new_student

@app.get("/students/{student_id}", response_model=dict)
async def get_student(student_id: int):
    """
    Retrieve student information by ID.

    :param student_id: ID of the student to retrieve
    :return: The student's information
    """
    logger.info("Retrieving student with ID: {}", student_id)
    student = await student_router.get_student(student_id)
    if student:
        logger.info("Found student: {}", student)
        return student
    logger.error("Student with ID: {} not found", student_id)
    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{student_id}", response_model=dict)
async def update_student(student_id: int, student: dict):
    """
    Update a student's email.

    :param student_id: ID of the student to update
    :param student: Dictionary containing updated email
    :return: The updated student's information
    """
    logger.info("Updating student with ID: {}. New data: {}", student_id, student)
    updated_student = await student_router.update_student(student_id, student)
    logger.info("Successfully updated student: {}", updated_student)
    return updated_student

# Include the student routes
app.include_router(student_router)