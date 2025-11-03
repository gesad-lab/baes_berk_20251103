'''
Database migration script to create Course and Teacher tables while preserving existing Student data.
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def migrate():
    inspector = inspect(engine)
    if 'courses' not in inspector.get_table_names() or 'teachers' not in inspector.get_table_names():
        Base.metadata.create_all(bind=engine)  # This will create the new Course and Teacher tables
if __name__ == "__main__":
    migrate()