"""Add teacher_id column to courses table

Revision ID: 2023_10_01_0002
Revises: 2023_10_01_0001
Create Date: 2023-10-01 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2023_10_01_0002'
down_revision = '2023_10_01_0001'  # Previous migration ID
branch_labels = None
depends_on = None

def upgrade():
    """Add teacher_id column to courses table"""
    # Add the teacher_id column that will serve as a foreign key to the teachers table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Create a foreign key constraint linking teacher_id to teachers.id
    op.create_foreign_key(
        'fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'], ondelete='SET NULL'
    )

def downgrade():
    """Remove teacher_id column from courses table"""
    # Drop the foreign key constraint
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    # Remove the teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')
"""