'''
Handles database connection and session management.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Migration script to add Teacher and Course tables
def upgrade():
    from alembic import op
    import sqlalchemy as sa
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Create a temporary courses table with the new teacher_id column
    op.create_table(
        'temp_courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'))  # Add this line
    )
    # Copy existing data from courses to temp_courses
    op.execute('INSERT INTO temp_courses (id, name, level) SELECT id, name, level FROM courses')
    # Drop the old courses table
    op.drop_table('courses')
    # Rename temp_courses to courses
    op.rename_table('temp_courses', 'courses')
    # Create the association table for students and courses
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    from alembic import op
    op.drop_table('student_courses')  # Drop the association table
    op.drop_table('courses')  # Drop the courses table
    op.drop_table('teachers')  # Drop the teachers table