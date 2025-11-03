'''
Migration script to add Student-Course relationship.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'unique_revision_id_for_student_course'  # Replace with actual unique revision ID
down_revision = 'unique_revision_id_for_course'  # Replace with the actual revision ID from xxxx_add_course_table.py
branch_labels = None
depends_on = None
def upgrade():
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True),
    )
def downgrade():
    op.drop_table('student_courses')