'''
Migration script to add teachers table to the database.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True),
    )
    # Add teacher_id column to courses table with a default value
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))
    # Optionally, you can set a default teacher_id for existing courses if applicable
    # For example, setting it to NULL or a specific teacher's ID if you have a default teacher
    # op.execute("UPDATE courses SET teacher_id = NULL")  # or set to a specific teacher ID
def downgrade():
    op.drop_column('courses', 'teacher_id')  # Remove teacher_id column from courses
    op.drop_table('teachers')  # Remove teachers table