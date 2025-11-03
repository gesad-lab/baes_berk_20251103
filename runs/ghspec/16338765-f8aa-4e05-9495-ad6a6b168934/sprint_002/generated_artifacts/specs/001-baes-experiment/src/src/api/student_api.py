from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import sqlite3

router = APIRouter()

# Database connection setup
DATABASE_NAME = "students.db"

class Student(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@router.post("/students/", response_model=Student)
def create_student(student: Student):
    """
    Create a new student record including email.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (student.name, student.email))
    connection.commit()
    student_id = cursor.lastrowid
    connection.close()
    return {**student.dict(), "id": student_id}

@router.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    """
    Retrieve a student's details including email by their ID.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student_row = cursor.fetchone()
    connection.close()
    
    if student_row is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return dict(student_row)

@router.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: Student):
    """
    Update the email of an existing student.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET name = ?, email = ? WHERE id = ?", (student.name, student.email, student_id))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    connection.commit()
    connection.close()
    return {**student.dict(), "id": student_id}

def alter_table_to_add_email():
    """
    Alter the students table to add an email column using SQLite's ALTER TABLE.
    This function should only be run once during the database setup/migration phase.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Check if the email column already exists
    cursor.execute("PRAGMA table_info(students)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if "email" not in columns:
        # Alter table to add email column
        cursor.execute("ALTER TABLE students ADD COLUMN email TEXT")
        connection.commit()
    
    connection.close()