'''
Migration script to add Teacher table and update Course table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxx_add_teacher_table'
down_revision = 'xxxx_add_course_table'  # Ensure this is the last migration
branch_labels = None
depends_on = None
def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Update the courses table to include teacher_id foreign key
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id')))  # Add teacher_id column
def downgrade():
    # Drop the teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')
    # Drop the teachers table
    op.drop_table('teachers')