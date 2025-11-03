'''
Migration script to add Course entity and update the database schema.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = 'previous_revision_id'  # Set to the last migration ID
branch_labels = None
depends_on = None
def upgrade():
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
    # Create the student_courses association table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
    )
    # Optionally, if you have existing data to migrate, you can add logic here to populate the student_courses table
    # For example, if you have a way to determine existing enrollments, you can insert them here.
    # This part is left for implementation based on your existing data structure.
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')