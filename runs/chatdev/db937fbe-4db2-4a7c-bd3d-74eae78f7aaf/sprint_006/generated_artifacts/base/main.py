'''
Database migration script to create Course and Teacher tables, establish relationships, and create association table.
'''
from sqlalchemy import create_engine, text  # Import text from SQLAlchemy
from models import Base, Course, Teacher  # Import Base, Course, and Teacher to create tables
from models import student_course_association  # Import association table
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
def create_tables():
    '''
    Create the database tables if they do not exist.
    '''
    Base.metadata.create_all(bind=engine)
def create_association_table():
    '''
    Create the association table for the many-to-many relationship.
    '''
    student_course_association.create(bind=engine, checkfirst=True)
if __name__ == "__main__":
    create_tables()  # Ensure tables are created
    create_association_table()  # Ensure the association table is created