'''
Migration script to add student_courses association table to the database.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_student_courses_table'
down_revision = 'add_course_table'
branch_labels = None
depends_on = None
def upgrade():
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True),
    )
def downgrade():
    op.drop_table('student_courses')