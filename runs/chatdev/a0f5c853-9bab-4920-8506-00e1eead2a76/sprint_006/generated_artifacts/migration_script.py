'''
Migration script to add Course and Teacher entities and their fields.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with actual revision ID
down_revision = 'yyyyyy'  # Replace with actual down revision ID
def upgrade():
    # Create temporary tables to hold existing data
    op.create_table(
        'temp_courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'))
    )
    op.create_table(
        'temp_teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Copy existing data into temporary tables
    op.execute("INSERT INTO temp_courses (id, name, level) SELECT id, name, level FROM courses")
    op.execute("INSERT INTO temp_teachers (id, name, email) SELECT id, name, email FROM teachers")
    # Drop old tables
    op.drop_table('courses')
    op.drop_table('teachers')
    # Create new tables
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'))
    )
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Restore data from temporary tables
    op.execute("INSERT INTO courses (id, name, level, teacher_id) SELECT id, name, level, teacher_id FROM temp_courses")
    op.execute("INSERT INTO teachers (id, name, email) SELECT id, name, email FROM temp_teachers")
    # Drop temporary tables
    op.drop_table('temp_courses')
    op.drop_table('temp_teachers')
def downgrade():
    # Drop association table
    op.drop_table('student_course')
    # Drop courses table
    op.drop_table('courses')
    # Drop teachers table
    op.drop_table('teachers')