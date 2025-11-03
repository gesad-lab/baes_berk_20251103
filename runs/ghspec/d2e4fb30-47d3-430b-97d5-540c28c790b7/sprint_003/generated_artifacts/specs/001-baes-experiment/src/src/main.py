```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.course import router as course_router

app = FastAPI()

# CORS middleware configuration to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust according to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the Course API router
app.include_router(course_router, prefix="/api/v1", tags=["courses"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Educational API!"}
```