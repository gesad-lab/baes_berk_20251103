from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
from sqlite3 import Error

app = FastAPI()

# Database connection setup
DATABASE = "students.db"

def create_connection():
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except Error as e:
        print(f"Error creating database connection: {e}")
    return conn

def create_table():
    """Create a table for students if it doesn't exist."""
    conn = create_connection()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
        ''')
        
create_table()  # Ensure the database and table are created on startup

class Student(BaseModel):
    name: str

class StudentInDB(Student):
    id: int

students_db: List[StudentInDB] = []

@app.post("/students/", response_model=StudentInDB)
async def create_student(student: Student):
    """Create a new student record."""
    if not student.name:
        raise HTTPException(status_code=400, detail="Name field is required.")
    
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name) VALUES (?);", (student.name,))
    conn.commit()
    student_id = cursor.lastrowid
    return StudentInDB(id=student_id, name=student.name)

@app.get("/students/{student_id}", response_model=StudentInDB)
async def get_student(student_id: int):
    """Retrieve a student record by ID."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?;", (student_id,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Student not found.")
    return StudentInDB(id=row[0], name=row[1])

@app.put("/students/{student_id}", response_model=StudentInDB)
async def update_student(student_id: int, student: Student):
    """Update an existing student's name."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?;", (student_id,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    if not student.name:
        raise HTTPException(status_code=400, detail="Name field is required.")

    cursor.execute("UPDATE students SET name = ? WHERE id = ?;", (student.name, student_id))
    conn.commit()
    return StudentInDB(id=student_id, name=student.name)

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    """Delete a student record by ID."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?;", (student_id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    conn.commit()
    return {"detail": "Student deleted successfully."}