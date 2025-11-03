```python
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Teacher  # Ensure Teacher model is imported from models
from fastapi.middleware.cors import CORSMiddleware

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Configure CORS if necessary
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
DATABASE_URL = "sqlite:///./test.db"  # Update as necessary for your DB
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Pydantic model for Teacher
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

@app.post("/teachers")
async def create_teacher(teacher: TeacherCreate):
    db = SessionLocal()
    try:
        # Log new teacher creation request
        logger.info(f"Creating new teacher with name: {teacher.name}, email: {teacher.email}")

        # Check if teacher already exists
        existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
        if existing_teacher:
            logger.warning(f"Teacher with email {teacher.email} already exists.")
            raise HTTPException(status_code=400, detail="Teacher with this email already exists.")

        # Create and persist new teacher
        new_teacher = Teacher(name=teacher.name, email=teacher.email)
        db.add(new_teacher)
        db.commit()
        logger.info(f"Successfully created teacher: {new_teacher.name} with email: {new_teacher.email}")
        return {"message": "Teacher created successfully."}
    
    except Exception as e:
        logger.error(f"Error creating teacher: {str(e)}")
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail="Failed to create teacher.")
    
    finally:
        db.close()

@app.get("/teachers")
async def get_teachers():
    db = SessionLocal()
    try:
        # Log retrieval of teachers
        logger.info("Retrieving list of teachers.")
        
        teachers = db.query(Teacher).all()
        logger.info(f"Found {len(teachers)} teachers.")
        return teachers

    except Exception as e:
        logger.error(f"Error retrieving teachers: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve teachers.")
    
    finally:
        db.close()
```