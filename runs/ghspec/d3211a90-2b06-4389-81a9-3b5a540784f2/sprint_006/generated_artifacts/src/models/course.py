from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Course model with a foreign key for the Teacher
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # New foreign key

    # Establishes a relationship to the Teacher model
    teacher = relationship('Teacher')  # One-to-many relationship

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

# Database initialization code
def initialize_database():
    engine = create_engine('sqlite:///database.db')  # Database connection
    Base.metadata.create_all(engine)  # Create tables if they do not exist

# Migration function to add the 'teacher_id' foreign key to an existing Course table
def upgrade():
    # Adding foreign key relationship to the existing Course table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_course_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    # Dropping foreign key relationship and the column during rollback
    op.drop_constraint('fk_course_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')