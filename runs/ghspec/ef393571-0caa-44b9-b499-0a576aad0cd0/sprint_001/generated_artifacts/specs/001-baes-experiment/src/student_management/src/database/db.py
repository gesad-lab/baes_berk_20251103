```python
import aiosqlite
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

# Pydantic model for Student
class Student(BaseModel):
    name: str = Field(..., description="The name of the student, required.")

# Initialize FastAPI application
app = FastAPI()

DATABASE = "students.db"

# Function to initialize the database and create the Student table
async def initialize_db():
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        await db.commit()

@app.on_event("startup")
async def startup_event():
    await initialize_db()

@app.post("/students", response_model=Student)
async def create_student(student: Student):
    async with aiosqlite.connect(DATABASE) as db:
        # Insert student into the database
        await db.execute('INSERT INTO students (name) VALUES (?)', (student.name,))
        await db.commit()
    return student

@app.get("/students", response_model=List[Student])
async def get_students():
    async with aiosqlite.connect(DATABASE) as db:
        cursor = await db.execute('SELECT name FROM students')
        rows = await cursor.fetchall()
        
    # Construct the list of students from the rows retrieved
    return [Student(name=row[0]) for row in rows]
```