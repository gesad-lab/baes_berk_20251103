from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Course(Base):
    """Course model to store information about courses."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # course name cannot be null
    level = Column(String, nullable=False)  # course level cannot be null

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}')>"

def initialize_database(db_url: str):
    """Initializes the database, creating all tables."""
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)  # This handles the creation of the courses table

# Migration script to create courses table
def migrate_create_courses_table():
    """Migration function to create the courses table in the database."""
    engine = create_engine('sqlite:///path_to_your_database.db')  # Replace with your database path
    Base.metadata.create_all(bind=engine)  # Creates the courses table if it doesn't exist

# Execute migration
if __name__ == "__main__":
    migrate_create_courses_table()