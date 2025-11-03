```python
import aiosqlite
from typing import List

DATABASE = "students.db"


async def initialize_db() -> None:
    """Initialize the database and create the Student table if it doesn't exist."""
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """
        )
        await db.commit()


async def add_student(name: str) -> int:
    """Insert a new student into the database.

    Args:
        name (str): The name of the student to be added.

    Returns:
        int: The id of the newly created student.
    """
    async with aiosqlite.connect(DATABASE) as db:
        cursor = await db.execute(
            "INSERT INTO student (name) VALUES (?)", (name,)
        )
        await db.commit()
        return cursor.lastrowid


async def get_all_students() -> List[dict]:
    """Retrieve all students from the database.

    Returns:
        List[dict]: A list of dictionaries containing student data.
    """
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT id, name FROM student") as cursor:
            students = await cursor.fetchall()
            return [{"id": row[0], "name": row[1]} for row in students]
```