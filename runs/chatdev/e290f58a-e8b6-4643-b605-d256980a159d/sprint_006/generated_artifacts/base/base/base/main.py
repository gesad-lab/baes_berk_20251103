'''
Migration script to create the Course table.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Student, Course  # Importing the Student and Course models
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def upgrade():
    """Create the courses table."""
    Base.metadata.create_all(bind=engine)  # This will create both students and courses tables
def downgrade():
    """Remove courses table if needed."""
    # Note: SQLite does not support dropping tables directly.
    # This would require creating a new table without the courses table,
    # copying the data, and then dropping the old table.
    pass
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)