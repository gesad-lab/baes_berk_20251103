from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# In-memory student storage for this example
students = []

class Student(BaseModel):
    """Model representing a student."""
    name: str = Field(..., title="The name of the student", max_length=100)

@app.post("/students", status_code=201)
async def create_student(student: Student):
    """Create a new student.
    
    Args:
        student (Student): The student information being created.
    
    Returns:
        dict: A message confirming the student creation.
        
    Raises:
        HTTPException: If the student creation fails.
    """
    # Validate that name is provided through Pydantic
    students.append(student)
    return {"message": "Student created successfully."}

@app.get("/students", response_model=List[Student])
async def get_students():
    """Retrieve a list of all students.

    Returns:
        List[Student]: A list of students.
        
    Raises:
        HTTPException: If an error occurs while retrieving students.
    """
    return students

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    """Custom error handler for HTTP exceptions.

    Args:
        request: The request object.
        exc (HTTPException): The exception instance.

    Returns:
        JSONResponse: The error response formatted in a consistent structure.
    """
    if exc.status_code == 400:
        return {
            "error": {
                "code": "E001",
                "message": "Name field is required."
            }
        }
    return await request.app.default_exception_handler(request, exc)

# Documentation of API responses and error formats
@app.get("/api-docs")
async def api_docs():
    """API Documentation."""
    return {
        "POST /students": {
            "description": "Create a new student",
            "request": {
                "body": {
                    "name": "string (required)"
                }
            },
            "responses": {
                "201": {
                    "description": "Student created successfully",
                    "body": {
                        "message": "string"
                    }
                },
                "400": {
                    "description": "Validation error",
                    "body": {
                        "error": {
                            "code": "E001",
                            "message": "Name field is required."
                        }
                    }
                }
            }
        },
        "GET /students": {
            "description": "Retrieve a list of all students",
            "responses": {
                "200": {
                    "description": "A list of students",
                    "body": List[Student]
                },
                "500": {
                    "description": "Internal server error"
                }
            }
        }
    }