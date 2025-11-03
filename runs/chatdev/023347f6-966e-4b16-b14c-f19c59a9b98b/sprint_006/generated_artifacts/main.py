'''
Migration script to add Teacher table to the database while preserving existing data.
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import NoSuchTableError
from models import Base
DATABASE_URL = "sqlite:///./students.db"
def upgrade():
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    inspector = inspect(engine)
    try:
        # Check if the 'teachers' table already exists
        if 'teachers' not in inspector.get_table_names():
            Base.metadata.create_all(engine)  # Create the Teacher table
            # Logic to associate existing courses with teachers
            # This is a placeholder for actual logic to associate courses with teachers
            # You might want to prompt the user or set a default teacher
            # Example: Assigning a default teacher_id to all existing courses
            default_teacher_id = 1  # Assuming a default teacher with ID 1 exists
            connection.execute("UPDATE courses SET teacher_id = :teacher_id", {"teacher_id": default_teacher_id})
    except NoSuchTableError:
        print("Error: The 'teachers' table does not exist.")
    finally:
        connection.close()
if __name__ == "__main__":
    upgrade()