```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CourseCreate(BaseModel):
    name: str
    level: str

@app.post("/courses", response_model=CourseCreate, status_code=201)
def create_course(course: CourseCreate):
    # Validate that the 'name' field is provided
    if not course.name:
        raise HTTPException(status_code=400, detail="Name field is required.")
    # Validate that the 'level' field is provided
    if not course.level:
        raise HTTPException(status_code=400, detail="Level field is required.")
    
    # Ideally, call a service to handle the creation logic
    return create_course_service(course.name, course.level)

# The function `create_course_service` should be defined elsewhere in your code
```