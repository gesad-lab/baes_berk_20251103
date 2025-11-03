'''
Migration script to add Teacher table and update Course table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Add teacher_id column to courses table with a default value (if applicable)
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))
    # Optionally, you can set a default value for existing courses if necessary
    # op.execute("UPDATE courses SET teacher_id = NULL")  # Or set to a specific teacher ID if applicable
def downgrade():
    op.drop_column('courses', 'teacher_id')
    op.drop_table('teachers')