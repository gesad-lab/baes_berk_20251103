from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create the 'enrollments' table to establish a relationship between Students and Courses
    op.create_table('enrollments',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), nullable=False),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), nullable=False)
    )

def downgrade():
    # Drop the 'enrollments' table if we need to rollback this migration
    op.drop_table('enrollments')