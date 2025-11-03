# database_migrations.py

from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine import reflection

# Revision identifiers, used by Alembic.
revision = 'add_courses_table'
down_revision = None  # Specify the previous revision here if any
branch_labels = None
depends_on = None

def upgrade():
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('level', sa.String(length=100), nullable=False)
    )

    # Create the students table
    op.create_table(
        'students',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True)
    )

    # Create the student_courses junction table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True),
    )

def downgrade():
    # Drop the student_courses junction table first due to its dependencies
    op.drop_table('student_courses')
    # Drop the students table
    op.drop_table('students')
    # Drop the courses table
    op.drop_table('courses')