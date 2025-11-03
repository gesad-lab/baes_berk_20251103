'''
Migration script for adding Teacher table and preserving existing data.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teacher_table'
down_revision = 'add_course_table'  # Update this based on your last migration
def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True),
    )
    # Add teacher_id column to courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))
def downgrade():
    # Drop the teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')
    # Drop the teachers table
    op.drop_table('teachers')