'''
Migration script to add Teacher table and preserve existing data.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teacher_table'
down_revision = 'add_student_courses_table'  # Assuming this is the last migration
branch_labels = None
depends_on = None
def upgrade():
    # Create the Teacher table
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Add teacher_id to courses with a default value of NULL
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True, server_default=None))
def downgrade():
    # Drop the teacher_id column from courses
    op.drop_column('courses', 'teacher_id')
    # Drop the Teacher table
    op.drop_table('teachers')