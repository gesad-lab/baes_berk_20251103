from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from models.course import Course  # Importing course model

# Create engine for SQLite database
engine = create_engine("sqlite:///./students.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def upgrade():
    """Create courses table."""
    from sqlalchemy import MetaData
    meta = MetaData(bind=engine)

    with engine.connect() as connection:
        # Execute SQL command to create the courses table
        connection.execute(
            """
            CREATE TABLE courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                level TEXT NOT NULL
            );
            """
        )

def downgrade():
    """Drop courses table."""
    with engine.connect() as connection:
        # Execute SQL command to drop the courses table if it exists
        connection.execute("DROP TABLE IF EXISTS courses;")

if __name__ == "__main__":
    upgrade()  # Run upgrade to apply the migration