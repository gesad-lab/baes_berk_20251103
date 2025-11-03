from fastapi import APIRouter, HTTPException, Depends, status, Response
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from contextlib import contextmanager
import sqlite3
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/students", tags=["Students"])

class StudentCreate(BaseModel):
    name: Optional[str] = None

class StudentUpdate(BaseModel):
    name: Optional[str] = None

class StudentResponse(BaseModel):
    id: int
    name: Optional[str] = None

@contextmanager
def get_db_connection():
    """Database connection context manager with proper error handling"""
    db_path = Path("app/database/baes_system.db")
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(data: StudentCreate) -> StudentResponse:
    """Create a new student in the database.

    Args:
        data (StudentCreate): The student data to create.

    Returns:
        StudentResponse: The created student with its ID.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO students (name) VALUES (?)", (data.name,))
            db.commit()
            student_id = cursor.lastrowid
            return StudentResponse(id=student_id, name=data.name)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/", response_model=List[StudentResponse])
def list_students() -> List[StudentResponse]:
    """Retrieve a list of all students from the database.

    Returns:
        List[StudentResponse]: A list of students.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()
            return [StudentResponse(id=student['id'], name=student['name']) for student in students]
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/{id}", response_model=StudentResponse)
def get_student(id: int) -> StudentResponse:
    """Retrieve a student by ID from the database.

    Args:
        id (int): The ID of the student to retrieve.

    Returns:
        StudentResponse: The student with the specified ID.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
            student = cursor.fetchone()
            if student is None:
                raise HTTPException(status_code=404, detail="Student not found")
            return StudentResponse(id=student['id'], name=student['name'])
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.put("/{id}", response_model=StudentResponse)
def update_student(id: int, data: StudentUpdate) -> StudentResponse:
    """Update a student by ID in the database.

    Args:
        id (int): The ID of the student to update.
        data (StudentUpdate): The new data for the student.

    Returns:
        StudentResponse: The updated student.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("UPDATE students SET name = ? WHERE id = ?", (data.name, id))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Student not found")
            db.commit()
            return StudentResponse(id=id, name=data.name)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/{id}", response_class=Response)
def delete_student(id: int) -> Response:
    """Delete a student by ID from the database.

    Args:
        id (int): The ID of the student to delete.

    Returns:
        Response: A response indicating the deletion was successful.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM students WHERE id = ?", (id,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Student not found")
            db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")