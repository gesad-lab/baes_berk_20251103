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
    # Create a temporary table to hold existing course data including teacher_id
    op.create_table(
        'temp_courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.Column('teacher_id', sa.Integer)  # Added teacher_id field
    )
    # Copy existing data from courses to temp_courses
    op.execute('INSERT INTO temp_courses (id, name, level, teacher_id) SELECT id, name, level, teacher_id FROM courses')
    # Drop the existing courses table
    op.drop_table('courses')
    # Recreate the courses table with the new teacher_id column
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'))  # Added this line
    )
    # Copy data back from temp_courses to courses
    op.execute('INSERT INTO courses (id, name, level, teacher_id) SELECT id, name, level, teacher_id FROM temp_courses')
    # Drop the temporary table
    op.drop_table('temp_courses')
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