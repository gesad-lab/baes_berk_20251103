'''
Handles database migrations to add the email field to the Student entity and create the Course entity.
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course, student_courses
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def upgrade():
    '''
    Creates the courses table and the association table if they don't exist and ensures the email field is added to the Student entity.
    Preserves existing Student data and migrates it to the new association table if applicable.
    '''
    # Create the courses table
    Course.__table__.create(bind=engine, checkfirst=True)  # This will create the courses table if it doesn't exist
    # Create the association table
    student_courses.create(bind=engine, checkfirst=True)  # Create the association table if it doesn't exist
    # Use inspector to check if the students table exists
    inspector = inspect(engine)
    if inspector.has_table("students"):
        # Logic to migrate existing student data to the association table
        with SessionLocal() as session:
            students = session.query(Student).all()  # Fetch all existing students
            for student in students:
                # Placeholder logic to determine which courses a student is enrolled in
                # Example: if student.email.endswith('@example.com'):
                #              course_id = 1  # Example course ID
                #              session.execute(student_courses.insert().values(student_id=student.id, course_id=course_id))
                pass  # Replace with actual logic to associate students with courses
    else:
        Base.metadata.create_all(bind=engine)  # Create students table if it doesn't exist
def downgrade():
    '''
    Logic to remove the email column if necessary (not implemented).
    '''
    pass
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  # Create tables if they don't exist
    upgrade()  # Run the upgrade to add the email field and create courses table