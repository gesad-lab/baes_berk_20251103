'''
Alembic migration script to add Course table and association table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the Course table if it doesn't exist
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
    # Create the association table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True),
    )
    # Optionally, you can add logic here to migrate existing relationships if needed
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')