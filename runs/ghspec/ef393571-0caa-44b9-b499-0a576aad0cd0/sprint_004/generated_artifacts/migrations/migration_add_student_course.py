```python
import aiosqlite

async def migrate():
    """Apply database migration to add the student_course junction table."""
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS student_course (
                student_id INTEGER,
                course_id INTEGER,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY (student_id) REFERENCES student(id),
                FOREIGN KEY (course_id) REFERENCES course(id)
            )
        """)
        await db.commit()

# To be executed during the application startup or migration process
if __name__ == "__main__":
    import asyncio

    asyncio.run(migrate())
```