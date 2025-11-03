'''
Migration script for adding the student_courses association table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the association table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    # Drop the association table
    op.drop_table('student_courses')