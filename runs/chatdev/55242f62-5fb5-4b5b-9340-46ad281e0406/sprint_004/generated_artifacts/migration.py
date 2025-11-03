'''
Migration script to add Course entity and email field to Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '20231001_001'  # Unique revision ID
down_revision = None  # Set to the previous revision ID if applicable
branch_labels = None
depends_on = None
def upgrade():
    # Add email column to students
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))  # Add email column
    # Create courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
    # Create association table for many-to-many relationship
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    # Remove association table
    op.drop_table('student_courses')
    # Remove courses table
    op.drop_table('courses')
    # Remove email column if needed
    op.drop_column('students', 'email')