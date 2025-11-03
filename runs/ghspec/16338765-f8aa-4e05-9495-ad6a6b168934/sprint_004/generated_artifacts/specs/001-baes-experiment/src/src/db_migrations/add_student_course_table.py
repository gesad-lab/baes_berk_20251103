from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for declarative model definitions
Base = declarative_base()

class StudentCourse(Base):
    """StudentCourse model defines the relationship between Students and Courses."""
    
    __tablename__ = 'StudentCourse'

    # Define the student_id column, which is a foreign key referencing the Student table
    student_id = Column(Integer, ForeignKey('Student.id'), primary_key=True, nullable=False)

    # Define the course_id column, which is a foreign key referencing the Course table
    course_id = Column(Integer, ForeignKey('Course.id'), primary_key=True, nullable=False)

    def __repr__(self):
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"


def upgrade():
    """Migration logic to create the StudentCourse table."""
    # This function will create the StudentCourse table in the database
    # It ensures the existing Student and Course data remain intact
    try:
        Base.metadata.create_all(bind=<engine>)  # Replace <engine> with your actual database engine
    except Exception as e:
        print(f"Error during migration: {e}")
        raise


def downgrade():
    """Migration logic to drop the StudentCourse table."""
    # This function will drop the StudentCourse table from the database
    try:
        Base.metadata.drop_all(bind=<engine>, tables=[StudentCourse.__table__])  # Only drop the StudentCourse table
    except Exception as e:
        print(f"Error during downgrade: {e}")
        raise