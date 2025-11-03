```python
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import aiosqlite

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///students.db')

# Pydantic model for student data validation
class Student(BaseModel):
    name: str = Field(..., max_length=100)

# FastAPI application instance
app = FastAPI()

# Database initialization
async def init_db():
    async with aiosqlite.connect(DATABASE_URL) as db:
        # Create the students table if it doesn't exist
        await db.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        await db.commit()

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.post("/students", response_model=Student)
async def create_student(student: Student):
    async with aiosqlite.connect(DATABASE_URL) as db:
        await db.execute('INSERT INTO students (name) VALUES (?)', (student.name,))
        await db.commit()
        return student

@app.get("/students", response_model=list[Student])
async def get_students():
    async with aiosqlite.connect(DATABASE_URL) as db:
        async with db.execute('SELECT * FROM students') as cursor:
            rows = await cursor.fetchall()
            return [{"id": row[0], "name": row[1]} for row in rows]

# Error handling for invalid input
@app.exception_handler(ValueError)
async def validation_exception_handler(request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"error": {"code": "E001", "message": str(exc)}}
    )
```