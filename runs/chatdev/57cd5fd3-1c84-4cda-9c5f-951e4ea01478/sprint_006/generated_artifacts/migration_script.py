'''
Alembic migration script to add Teacher table and update Course table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the Teacher table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
    )
    # Update the courses table to add teacher_id
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id')))  # Added teacher_id column
def downgrade():
    op.drop_column('courses', 'teacher_id')  # Drop the teacher_id column
    op.drop_table('teachers')