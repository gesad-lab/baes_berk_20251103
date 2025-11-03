```python
# src/main.py

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from alembic.config import Config
from alembic import command

app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Teacher model
class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

# Create necessary tables
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup():
    """Run migrations on application startup to ensure the database is up-to-date."""
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")  # Ensure latest migrations run on startup

@app.post("/teachers", response_model=dict, status_code=201)
async def create_teacher(name: str, email: str):
    """Create a new teacher with name and email."""
    if not name:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Name field is required."}})

    if not email or "@" not in email:
        raise HTTPException(status_code=400, detail={"error": {"code": "E002", "message": "Email format is invalid."}})

    new_teacher = Teacher(name=name, email=email)

    db = SessionLocal()
    try:
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
        return JSONResponse(status_code=201, content={"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email})
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail={"error": {"code": "E003", "message": "Email already exists."}})
    finally:
        db.close()
```