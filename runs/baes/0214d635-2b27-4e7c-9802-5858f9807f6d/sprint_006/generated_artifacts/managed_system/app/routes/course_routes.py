from fastapi import APIRouter, HTTPException, Depends, status, Response
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from contextlib import contextmanager
import sqlite3
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/courses", tags=["Courses"])

class CourseCreate(BaseModel):
    name: Optional[str] = None
    teacher_id: Optional[int] = None

class CourseUpdate(BaseModel):
    name: Optional[str] = None
    teacher_id: Optional[int] = None

class CourseResponse(BaseModel):
    id: int
    name: Optional[str] = None
    teacher_id: Optional[int] = None

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

@router.post("/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course(data: CourseCreate) -> CourseResponse:
    """Create a new course in the database.

    Args:
        data (CourseCreate): The course data to create.

    Returns:
        CourseResponse: The created course with its ID.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO courses (name, teacher_id) VALUES (?, ?)", (data.name, data.teacher_id))
            db.commit()
            course_id = cursor.lastrowid
            return CourseResponse(id=course_id, name=data.name, teacher_id=data.teacher_id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/", response_model=List[CourseResponse])
def list_courses() -> List[CourseResponse]:
    """Retrieve a list of all courses from the database.

    Returns:
        List[CourseResponse]: A list of courses.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM courses")
            courses = cursor.fetchall()
            return [CourseResponse(id=row['id'], name=row['name'], teacher_id=row['teacher_id']) for row in courses]
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/{id}", response_model=CourseResponse)
def get_course(id: int) -> CourseResponse:
    """Retrieve a course by its ID.

    Args:
        id (int): The ID of the course to retrieve.

    Returns:
        CourseResponse: The course with the specified ID.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM courses WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row is None:
                raise HTTPException(status_code=404, detail="Course not found")
            return CourseResponse(id=row['id'], name=row['name'], teacher_id=row['teacher_id'])
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.put("/{id}", response_model=CourseResponse)
def update_course(id: int, data: CourseUpdate) -> CourseResponse:
    """Update a course by its ID.

    Args:
        id (int): The ID of the course to update.
        data (CourseUpdate): The new data for the course.

    Returns:
        CourseResponse: The updated course.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("UPDATE courses SET name = ?, teacher_id = ? WHERE id = ?", (data.name, data.teacher_id, id))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Course not found")
            db.commit()
            return CourseResponse(id=id, name=data.name, teacher_id=data.teacher_id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/{id}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
def delete_course(id: int) -> Response:
    """Delete a course by its ID.

    Args:
        id (int): The ID of the course to delete.

    Returns:
        Response: HTTP 204 No Content if successful.
    """
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM courses WHERE id = ?", (id,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Course not found")
            db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")