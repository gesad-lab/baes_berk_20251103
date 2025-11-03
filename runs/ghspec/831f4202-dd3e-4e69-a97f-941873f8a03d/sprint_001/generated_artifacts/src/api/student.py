```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from typing import List
import sqlite3

app = FastAPI()

# Database setup
def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Model for incoming student data
class Student(BaseModel):
    name: constr(min_length=1)  # Ensure name is not empty

# Initialize an in-memory store for testing (if needed) - comment out for production
# students_store = []

@app.post("/students", response_description="Add a new student", response_model=Student)
async def create_student(student: Student):
    # Validate the name input
    if not student.name:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Name is required"}})

    # Database insertion
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name) VALUES (?)', (student.name,))
    conn.commit()
    conn.close()

    # Return the newly added student
    return student

@app.get("/students", response_description="Retrieve the list of students", response_model=List[Student])
async def get_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM students')
    students_data = cursor.fetchall()
    conn.close()

    # Map the results to the Student model
    students = [Student(name=row[0]) for row in students_data]

    # Return JSON response with the list of students
    return students
```