'''
Database migration script to add Course table and association table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_course_table'
down_revision = 'add_email_to_student'
branch_labels = None
depends_on = None
def upgrade():
    # Create the 'courses' table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
    # Create the association table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True),
    )
    # Optional: Add logic to migrate existing data if necessary
    # This is where you can add logic to handle existing data if needed
def downgrade():
    # Drop the association table if needed
    op.drop_table('student_courses')
    # Drop the 'courses' table if needed
    op.drop_table('courses')