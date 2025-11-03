'''
Create a new migration script using Alembic to add email field to students and create the Teacher table while preserving existing data.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Add email column as nullable initially
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Ensure that all existing records have valid email values before making it non-nullable
    # (This step may require manual intervention to set valid emails for existing records)
    # Change the column to be non-nullable after ensuring all records have valid emails
    op.alter_column('students', 'email', nullable=False)
    # Create Teacher table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Add teacher_id column to courses
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))
def downgrade():
    op.drop_table('teachers')
    op.drop_column('courses', 'teacher_id')
    op.drop_column('students', 'email')