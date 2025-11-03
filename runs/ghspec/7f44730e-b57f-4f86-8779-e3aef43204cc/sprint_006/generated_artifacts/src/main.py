from fastapi import FastAPI, HTTPException
from db.database import init_db
import api.courses
import api.teachers

app = FastAPI()

@app.on_event("startup")
def startup_event():
    """Initialize the database at startup."""
    init_db()

# Include updated courses and new teachers routes
app.include_router(api.courses.router)
app.include_router(api.teachers.router)

# New API Endpoints for teacher assignments to courses

@app.post("/courses/{course_id}/assign_teacher")
async def assign_teacher(course_id: str, teacher_id: str):
    """Assign a teacher to a specific course.

    Args:
        course_id: The ID of the course to which the teacher is being assigned.
        teacher_id: The ID of the teacher to assign.

    Returns:
        JSON response indicating success or error.
    """
    # Validate existence of course and teacher here (pseudo-representative)
    # Assuming course_service and teacher_service have been defined elsewhere
    course = await course_service.get_course_by_id(course_id)
    teacher = await teacher_service.get_teacher_by_id(teacher_id)

    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Course not found"}})
    
    if not teacher:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Teacher not found"}})

    # If validation passes, assign the teacher to the course
    await course_service.assign_teacher(course_id, teacher_id)

    return {"message": "Teacher assigned to course successfully"}

@app.get("/courses/{course_id}")
async def get_course_details(course_id: str):
    """Retrieve course details including assigned teacher information.

    Args:
        course_id: The ID of the course to retrieve.

    Returns:
        JSON response containing course information and teacher.
    """
    course = await course_service.get_course_by_id(course_id)

    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Course not found"}})

    # Assuming 'teacher' is a relationship already established in the course model
    return {
        "course": {
            "name": course.name,
            "teacher": {
                "name": course.teacher.name,
                "email": course.teacher.email
            }
        }
    }