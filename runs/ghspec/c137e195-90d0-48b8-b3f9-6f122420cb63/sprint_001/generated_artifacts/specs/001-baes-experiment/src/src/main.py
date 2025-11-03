```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Centralized error handling

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Handles HTTP exceptions and formats them into a consistent JSON response.

    Args:
        request (Request): The original request that raised the exception.
        exc (HTTPException): The exception that was raised.

    Returns:
        JSONResponse: A JSON response containing the error code and message.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {"code": str(exc.status_code), "message": exc.detail}}
    )

@app.post("/students", status_code=201)
async def create_student(name: str):
    """
    Creates a new student entry with the provided name.
    
    Args:
        name (str): The name of the student to create.

    Raises:
        HTTPException: If the name is empty, a 400 Bad Request is raised.

    Returns:
        dict: A dictionary containing the created student's data.
    """
    if not name:
        raise HTTPException(status_code=400, detail="E001: Student name must be provided")
    
    # Code to create the student in the database goes here (not included)
    
    return {"name": name}  # Placeholder for the created student's data

@app.get("/students")
async def get_students():
    """
    Retrieves a list of all students in the system.

    Returns:
        List[dict]: A list of all students.
    """
    # Code to retrieve students from the database goes here (not included)
    
    return []  # Placeholder for the list of students
```