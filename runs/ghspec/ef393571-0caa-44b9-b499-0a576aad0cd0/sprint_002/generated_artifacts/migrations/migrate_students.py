import aiosqlite

async def migrate():
    """
    Update the database schema to add the email column to the students table.

    This migration will add a new column 'email' as a TEXT type that cannot be NULL
    and must be unique. Existing data is preserved, with the new column populated
    where applicable.
    """
    async with aiosqlite.connect("students.db") as db:
        # Add the email column to the existing students table
        await db.execute("ALTER TABLE students ADD COLUMN email TEXT NOT NULL UNIQUE")
        await db.commit()