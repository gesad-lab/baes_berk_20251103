'''
Migration script to add teacher_id to courses table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx_add_teacher_relationship'
down_revision = 'xxxxxx_add_teacher_table'  # Update to reflect the correct previous migration revision
branch_labels = None
depends_on = None
def upgrade():
    # Add the teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))
    # Check if there are any teachers in the database
    connection = op.get_bind()
    result = connection.execute("SELECT id FROM teachers LIMIT 1")
    teacher_id = result.fetchone()
    if teacher_id:
        # If a teacher exists, set the teacher_id for existing courses
        op.execute("UPDATE courses SET teacher_id = (SELECT id FROM teachers LIMIT 1) WHERE teacher_id IS NULL")
    else:
        # If no teachers exist, leave teacher_id as NULL
        pass
def downgrade():
    op.drop_column('courses', 'teacher_id')