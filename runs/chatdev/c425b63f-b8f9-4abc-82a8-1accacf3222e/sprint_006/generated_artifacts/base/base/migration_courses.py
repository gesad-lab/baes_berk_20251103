'''
Migration script to create courses table and association table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Update with a new revision ID
down_revision = 'xxxxxx'  # Update with the previous migration revision ID
branch_labels = None
depends_on = None
def upgrade():
    '''
    Create courses table and association table for students and courses.
    '''
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True),
    )
def downgrade():
    '''
    Drop courses table and association table.
    '''
    op.drop_table('student_courses')
    op.drop_table('courses')