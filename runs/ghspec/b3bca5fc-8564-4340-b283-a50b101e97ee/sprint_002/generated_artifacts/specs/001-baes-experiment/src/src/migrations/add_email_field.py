from sqlalchemy import Column, String, Integer, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New field

def upgrade(engine_url: str):
    """
    Upgrade the database schema to include the 'email' field in the 'students' table.
    
    Parameters:
        engine_url (str): The database connection string.
    """
    # Create an engine and bind it to the metadata
    engine = create_engine(engine_url)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)  # Create tables if they do not exist

    # Import existing data and modify the column
    connection = engine.connect()
    trans = connection.begin()  # Start a transaction
    try:
        # Add the 'email' column if it doesn't exist already
        connection.execute("ALTER TABLE students ADD COLUMN email TEXT NOT NULL DEFAULT '';")
        trans.commit()  # Commit the transaction
    except Exception as e:
        trans.rollback()  # Rollback on failure
        print(f"Error occurred during migration: {e}")
    finally:
        connection.close()  # Ensure connection is closed after migration

def downgrade(engine_url: str):
    """
    Downgrade the database schema by removing the 'email' field from the 'students' table.
    
    Parameters:
        engine_url (str): The database connection string.
    """
    # Downgrade logic if needed in future migrations
    pass

# If this script is executed directly, we will perform the upgrade
if __name__ == "__main__":
    DATABASE_URL = "sqlite:///./test.db"  # Example connection string for SQLite
    upgrade(DATABASE_URL)  # Upgrade the database with the new schema