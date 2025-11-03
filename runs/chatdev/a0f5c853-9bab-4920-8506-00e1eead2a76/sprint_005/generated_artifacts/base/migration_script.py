'''
Migration script to add Course entity and its fields.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with actual revision ID
down_revision = 'yyyyyy'  # Replace with actual down revision ID
def upgrade():
    # Create courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
    # Create association table
    op.create_table(
        'student_course',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    # Drop association table
    op.drop_table('student_course')
    # Drop courses table
    op.drop_table('courses')