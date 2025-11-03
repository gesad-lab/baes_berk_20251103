'''
Migration script to add the association table for Student and Course.
'''
from alembic import op
import sqlalchemy as sa
revision = 'xxxx_add_student_courses_table'
down_revision = 'xxxx_add_teacher_id_to_course'  # Ensure this is the last migration
branch_labels = None
depends_on = None
def upgrade():
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    op.drop_table('student_courses')