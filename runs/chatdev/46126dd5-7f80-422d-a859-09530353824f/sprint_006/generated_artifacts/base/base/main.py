'''
Handles database migrations for adding Course entity and email field to Student entity.
'''
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def upgrade():
    # Create all tables if they do not exist
    Base.metadata.create_all(engine)
    # Check if the email column exists before adding it
    with engine.connect() as connection:
        result = connection.execute(text("PRAGMA table_info(students)"))
        columns = [row[1] for row in result]
        if 'email' not in columns:
            # Add the email column as nullable first
            connection.execute(text('ALTER TABLE students ADD COLUMN email TEXT'))
            # Update existing records to set a default value for email
            connection.execute(text('UPDATE students SET email = "" WHERE email IS NULL'))
def downgrade():
    # Downgrade logic if needed
    pass
if __name__ == "__main__":
    upgrade()