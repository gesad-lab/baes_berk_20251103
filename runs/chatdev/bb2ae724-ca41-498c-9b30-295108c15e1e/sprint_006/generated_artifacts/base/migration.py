'''
Handles the database migration for adding the Course and Teacher tables.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Check if the 'students' table exists before creating the 'courses' and 'teachers' tables
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if 'students' in inspector.get_table_names():
        # Create courses table
        op.create_table(
            'courses',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('level', sa.String(), nullable=False)
        )
        # Create student_course association table
        op.create_table(
            'student_course',
            sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
            sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
        )
        # Create teachers table
        op.create_table(
            'teachers',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('email', sa.String(), nullable=False)
        )
        # Ensure existing data in students and courses is preserved
        # Additional logic can be added here if needed
def downgrade():
    op.drop_table('student_course')
    op.drop_table('courses')
    op.drop_table('teachers')