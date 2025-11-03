'''
Migration script to add email field to the Student table.
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def add_email_column():
    inspector = inspect(engine)
    if 'students' in inspector.get_table_names():
        if 'email' not in [column['name'] for column in inspector.get_columns('students')]:
            with engine.connect() as connection:
                connection.execute('ALTER TABLE students ADD COLUMN email TEXT NOT NULL')
# Run this function to apply the migration
add_email_column()
Base.metadata.create_all(bind=engine)