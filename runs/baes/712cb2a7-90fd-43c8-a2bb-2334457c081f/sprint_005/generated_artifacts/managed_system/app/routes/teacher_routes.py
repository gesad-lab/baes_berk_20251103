from fastapi import APIRouter, HTTPException, Depends, status, Response
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from contextlib import contextmanager
import sqlite3
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/teachers", tags=["Teachers"])

class TeacherCreate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

class TeacherUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

class TeacherResponse(BaseModel):
    id: int
    name: Optional[str] = None
    email: Optional[str] = None

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

@router.post("/", response_model=TeacherResponse, status_code=status.HTTP_201_CREATED)
def create_teacher(data: TeacherCreate) -> TeacherResponse:
    """Create a new teacher in the database.

    Args:
        data (TeacherCreate): The teacher data to create.

    Returns:
        TeacherResponse: The created teacher with its ID.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO teachers (name, email) VALUES (?, ?)", (data.name, data.email))
            db.commit()
            teacher_id = cursor.lastrowid
            return TeacherResponse(id=teacher_id, name=data.name, email=data.email)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/", response_model=List[TeacherResponse])
def list_teachers() -> List[TeacherResponse]:
    """Retrieve a list of all teachers from the database.

    Returns:
        List[TeacherResponse]: A list of teachers.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM teachers")
            teachers = cursor.fetchall()
            return [TeacherResponse(id=teacher["id"], name=teacher["name"], email=teacher["email"]) for teacher in teachers]
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/{id}", response_model=TeacherResponse)
def get_teacher(id: int) -> TeacherResponse:
    """Retrieve a teacher by ID from the database.

    Args:
        id (int): The ID of the teacher to retrieve.

    Returns:
        TeacherResponse: The teacher with the specified ID.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM teachers WHERE id = ?", (id,))
            teacher = cursor.fetchone()
            if teacher is None:
                raise HTTPException(status_code=404, detail="Teacher not found")
            return TeacherResponse(id=teacher["id"], name=teacher["name"], email=teacher["email"])
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.put("/{id}", response_model=TeacherResponse)
def update_teacher(id: int, data: TeacherUpdate) -> TeacherResponse:
    """Update a teacher by ID in the database.

    Args:
        id (int): The ID of the teacher to update.
        data (TeacherUpdate): The new data for the teacher.

    Returns:
        TeacherResponse: The updated teacher.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("UPDATE teachers SET name = ?, email = ? WHERE id = ?", (data.name, data.email, id))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Teacher not found")
            db.commit()
            return TeacherResponse(id=id, name=data.name, email=data.email)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/{id}", response_class=Response)
def delete_teacher(id: int) -> Response:
    """Delete a teacher by ID from the database.

    Args:
        id (int): The ID of the teacher to delete.

    Returns:
        Response: HTTP 204 No Content.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM teachers WHERE id = ?", (id,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Teacher not found")
            db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")