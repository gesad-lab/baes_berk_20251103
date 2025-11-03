```python
# src/main.py

from fastapi import FastAPI
from src.services.student_service import app as student_app
from src.services.course_service import app as course_app  # Import course application

app = FastAPI()

# Include the student routers
app.include_router(student_app)
# Include the course routers for Course CRUD operations
app.include_router(course_app)  # Registering Course routes
```