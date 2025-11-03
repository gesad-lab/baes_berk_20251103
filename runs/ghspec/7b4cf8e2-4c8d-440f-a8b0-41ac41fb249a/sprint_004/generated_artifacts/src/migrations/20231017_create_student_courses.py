from sqlalchemy import create_engine, Column, Integer, ForeignKey, MetaData, Table
from sqlalchemy.orm import sessionmaker

def upgrade(migrate_engine):
    """
    Upgrade the database by creating the student_courses junction table.
    
    The student_courses table establishes a many-to-many relationship 
    between students and courses while preserving existing student and 
    course data during the schema update.
    """
    meta = MetaData(bind=migrate_engine)
    
    # Define the student_courses table with foreign keys to students and courses
    student_courses = Table('student_courses', meta,
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True),
    )
    
    # Create the student_courses table in the database
    meta.create_all()

def downgrade(migrate_engine):
    """
    Downgrade the database by dropping the student_courses junction table.
    
    This function allows reverting the migration changes if necessary.
    """
    meta = MetaData(bind=migrate_engine)
    
    # Load the student_courses table and drop it
    student_courses = Table('student_courses', meta, autoload=True)
    student_courses.drop()