'''
Database migration script to create Course and Teacher tables, establish relationships, and create association table.
'''
from sqlalchemy import create_engine, text  # Import text from SQLAlchemy
from models import Base, Course, Teacher  # Import Base, Course, and Teacher to create tables
from models import student_course_association  # Import association table
from alembic import command
from alembic.config import Config
import os  # Import os to check for directory existence
DATABASE_URL = "sqlite:///./students.db"
def create_tables():
    '''
    Create the database tables if they do not exist.
    '''
    Base.metadata.create_all(bind=engine)  # This will now include the updated Course and Teacher models
def create_association_table():
    '''
    Create the association table for the many-to-many relationship.
    '''
    student_course_association.create(bind=engine, checkfirst=True)
def run_migrations():
    '''
    Run database migrations to ensure schema is up to date.
    '''
    alembic_cfg = Config("alembic.ini")
    if not os.path.exists('alembic'):  # Check if the alembic directory exists
        print("Alembic directory does not exist. Please run 'alembic init alembic' to create it.")
        return
    command.upgrade(alembic_cfg, "head")
if __name__ == "__main__":
    create_tables()  # Ensure tables are created
    create_association_table()  # Ensure the association table is created
    run_migrations()  # Run migrations to apply any schema changes