'''
Migration script to create the Course table and ensure the existing Student table is intact.
'''
from sqlalchemy import create_engine
from models import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Create the tables in the database
Base.metadata.create_all(engine)  # This will create both students and courses tables if they don't exist
if __name__ == "__main__":
    print("Database migration completed.")