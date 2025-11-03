```python
from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import student

app = FastAPI()

# Create database tables at startup
@app.on_event("startup")
async def startup_event():
    # This will create all tables
    Base.metadata.create_all(bind=engine)

# Include the student routes
app.include_router(student.router, prefix="/students")
```