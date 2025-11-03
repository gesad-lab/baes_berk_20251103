from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxxx'  # Replace with the new revision ID
down_revision = 'yyyyyyy'  # Adjust this to match the last migration
branch_labels = None
depends_on = None

def upgrade():
    # Create student_courses table for many-to-many relationship
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),  # Foreign key to Student
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)   # Foreign key to Course
    )

def downgrade():
    # Drop student_courses table
    op.drop_table('student_courses')