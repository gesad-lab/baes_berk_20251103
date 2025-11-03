'''
Migration script for adding the Teacher table and updating Course table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the Teacher table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False)
    )
    # Add teacher_id column to courses
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id')))  # Add this line
def downgrade():
    # Drop the Teacher table
    op.drop_table('teachers')
    # Drop teacher_id column from courses
    op.drop_column('courses', 'teacher_id')  # Add this line