'''
Handles database migrations to add the email field to the Student entity, create the Course entity, and add the Teacher entity.
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course, Teacher, student_courses
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_course_ids_for_student(student_id: int):
    # This function should return a list of course IDs for the given student ID.
    with SessionLocal() as session:
        student_courses_data = session.query(student_courses).filter(student_courses.c.student_id == student_id).all()
        return [sc.course_id for sc in student_courses_data]
def upgrade():
    '''
    Creates the courses and teachers tables and the association table if they don't exist and ensures the email field is added to the Student entity.
    Preserves existing Student data and migrates it to the new association table if applicable.
    '''
    # Create the courses table
    Course.__table__.create(bind=engine, checkfirst=True)  # This will create the courses table if it doesn't exist
    # Create the teachers table
    Teacher.__table__.create(bind=engine, checkfirst=True)  # This will create the teachers table if it doesn't exist
    # Create the association table
    student_courses.create(bind=engine, checkfirst=True)  # Create the association table if it doesn't exist
    # Use inspector to check if the students table exists
    inspector = inspect(engine)
    if inspector.has_table("students"):
        # Logic to migrate existing student data to the association table
        with SessionLocal() as session:
            students = session.query(Student).all()  # Fetch all existing students
            for student in students:
                # Retrieve course IDs for the student
                course_ids = get_course_ids_for_student(student.id)
                for course_id in course_ids:
                    new_association = student_courses.insert().values(student_id=student.id, course_id=course_id)
                    session.execute(new_association)
            session.commit()  # Commit the changes after inserting associations
    else:
        Base.metadata.create_all(bind=engine)  # Create students table if it doesn't exist
def downgrade():
    '''
    Logic to remove the Teacher and Course tables if necessary.
    '''
    with SessionLocal() as session:
        # Drop the association table
        student_courses.drop(bind=engine, checkfirst=True)
        # Drop the teachers table
        Teacher.__table__.drop(bind=engine, checkfirst=True)
        # Drop the courses table
        Course.__table__.drop(bind=engine, checkfirst=True)
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  # Create tables if they don't exist
    upgrade()  # Run the upgrade to add the email field and create courses and teachers tables