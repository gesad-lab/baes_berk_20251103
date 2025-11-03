```python
import pytest
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, validator
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


# Create the database tables
Base.metadata.create_all(bind=engine)


class StudentCreate(BaseModel):
    name: str

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v or v.strip() == "":
            raise ValueError("Name field is required.")
        return v


app = FastAPI()


@app.post("/students", response_model=StudentCreate, status_code=201)
async def create_student(student: StudentCreate):
    # Here, normally you would check for duplicates, handle DB operations, etc.
    db = SessionLocal()
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    db.close()
    return JSONResponse(content={"id": db_student.id, "name": db_student.name}, status_code=201)


@app.get("/students", response_model=List[StudentCreate])
async def get_students():
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return JSONResponse(content=[{"id": student.id, "name": student.name} for student in students], status_code=200)


@app.exception_handler(ValueError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"error": {"code": "E001", "message": str(exc), "details": {}}},
    )


@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    return TestClient(app)


def test_create_student(client):
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe"}


def test_create_student_missing_name(client):
    response = client.post("/students", json={})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name field is required.", "details": {}}}


def test_get_students(client):
    client.post("/students", json={"name": "Jane Doe"})
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) > 0
```