'''
Migration script to add teacher_id column to Course table.
'''
from alembic import op
import sqlalchemy as sa
revision = 'xxxx_add_teacher_id_to_course'
down_revision = 'xxxx_add_course_table'  # Ensure this is the last migration
branch_labels = None
depends_on = None
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id')))  # Add foreign key
def downgrade():
    op.drop_column('courses', 'teacher_id')  # Remove foreign key