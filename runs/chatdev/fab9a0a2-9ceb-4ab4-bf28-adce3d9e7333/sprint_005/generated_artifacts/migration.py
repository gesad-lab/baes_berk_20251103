'''
Database migration script to add Teacher table and Course table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teacher_table'
down_revision = 'add_course_table'
branch_labels = None
depends_on = None
def upgrade():
    # Create the 'teachers' table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
    )
    # Existing upgrade logic for courses
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
def downgrade():
    # Drop the association table if needed
    op.drop_table('student_courses')
    # Drop the 'courses' table if needed
    op.drop_table('courses')
    # Drop the 'teachers' table if needed
    op.drop_table('teachers')