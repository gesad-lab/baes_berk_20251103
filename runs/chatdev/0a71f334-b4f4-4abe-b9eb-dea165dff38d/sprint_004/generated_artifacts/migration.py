'''
Database migration script for adding Course table and student_courses association table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = None  # Replace with the previous revision ID if applicable
branch_labels = None
depends_on = None
def upgrade():
    # Create the Course table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
    # Create the association table for Student and Course
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    # Drop the association table if needed
    op.drop_table('student_courses')
    # Drop the Course table if needed
    op.drop_table('courses')