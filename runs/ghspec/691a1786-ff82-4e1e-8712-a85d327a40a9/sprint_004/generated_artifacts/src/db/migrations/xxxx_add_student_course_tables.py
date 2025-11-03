from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'xxxx_add_student_course_tables'
down_revision = None  # Update based on your previous migration file
branch_labels = None
depends_on = None

def upgrade():
    # Create the courses table
    op.create_table('courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id', name='pk_courses_id'))

    # Create the student_course join table
    op.create_table('student_course',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], name='fk_student_course_student_id'),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name='fk_student_course_course_id'),
        sa.PrimaryKeyConstraint('student_id', 'course_id', name='pk_student_course'))

def downgrade():
    # Drop the join table first to avoid foreign key constraint issues
    op.drop_table('student_course')
    # Then drop the courses table
    op.drop_table('courses')