'''
Migration script to create student_courses association table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'unique_revision_id_2'  # Replace with a unique revision ID
down_revision = 'unique_revision_id'  # Replace with the last applied migration ID for courses
branch_labels = None
depends_on = None
def upgrade():
    # Create the student_courses association table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    # Drop the student_courses association table
    op.drop_table('student_courses')