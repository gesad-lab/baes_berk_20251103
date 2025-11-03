'''
Migration script to add Teacher table to the database and update Course table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with the actual revision ID
down_revision = 'yyyyyy'  # Replace with the actual down revision ID
def upgrade():
    # Check if the 'students' and 'courses' tables exist before creating the 'teachers' table
    if not op.get_bind().has_table('students'):
        raise Exception("The 'students' table does not exist. Migration cannot proceed.")
    if not op.get_bind().has_table('courses'):
        raise Exception("The 'courses' table does not exist. Migration cannot proceed.")
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Add teacher_id column to courses table with a default value of NULL
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True, server_default=None))
def downgrade():
    op.drop_column('courses', 'teacher_id')
    op.drop_table('teachers')