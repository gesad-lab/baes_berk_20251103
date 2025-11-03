from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from models import Base

DATABASE_URL = "sqlite:///./students.db"
# Create a new database engine instance
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initialize the database by creating the tables defined in the models.
    """
    try:
        # Create all tables in the database
        Base.metadata.create_all(bind=engine)
        print("Database initialized successfully.")

    except SQLAlchemyError as e:
        # Log the error for debugging
        print("Error occurred during database initialization:", str(e))


if __name__ == "__main__":
    init_db()