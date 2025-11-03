'''
Migration script to add teacher_id column to courses table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teacher_id_to_courses'
down_revision = 'add_student_courses_table'
branch_labels = None
depends_on = None
def upgrade():
    # Add the teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))
def downgrade():
    op.drop_column('courses', 'teacher_id')