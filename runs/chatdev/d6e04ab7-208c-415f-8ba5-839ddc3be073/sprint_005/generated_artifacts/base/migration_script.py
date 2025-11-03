'''
Migration script to add Course table and association table to the database.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with the actual revision ID
down_revision = 'yyyyyy'  # Replace with the actual down revision ID
def upgrade():
    # Check if the 'students' table exists before creating the 'courses' table
    if not op.get_bind().has_table('students'):
        raise Exception("The 'students' table does not exist. Migration cannot proceed.")
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')