```python
"""
main.py

This module serves as the entry point for the FastAPI application, defining the 
API endpoints and their functionality, including the management of teacher 
records. The following endpoints are available for teacher management:

1. **Create a Teacher**:
   - **Method**: POST
   - **URL**: `/teachers`
   - **Request Body**: 
     - `name`: String (required) - Name of the teacher.
     - `email`: String (required) - Email of the teacher.
   - **Response**:
     - `201 Created` along with the teacher's details in JSON format upon successful creation.
   - **Error Responses**:
     - `400 Bad Request` if required fields are missing, with a message indicating the specific errors.

2. **Retrieve a Teacher's Information**:
   - **Method**: GET
   - **URL**: `/teachers/{teacher_id}`
   - **Response**:
     - `200 OK` along with the teacher's data if found.
     - `404 Not Found` if the teacher does not exist.

3. **Schema Update**:
   - On application startup, the database schema is updated to include a new Teacher table.

4. **Error Handling**:
   - The API responds with clear and actionable messages for validation errors.

By utilizing these endpoints, users can manage teacher records effectively within the system.

This documentation remains a living document and may be updated as further enhancements are made to the teacher management API.
"""

from fastapi import FastAPI
from src.api.teacher import router as teacher_router

app = FastAPI()

# Include the teacher management router
app.include_router(teacher_router, prefix="/api/v1", tags=["teachers"])

# Additional app setup code as necessary...
```