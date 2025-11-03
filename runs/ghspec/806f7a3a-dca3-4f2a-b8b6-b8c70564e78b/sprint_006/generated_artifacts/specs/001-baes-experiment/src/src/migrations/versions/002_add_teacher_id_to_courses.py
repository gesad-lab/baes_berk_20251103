```python
"""Add teacher_id column to Course table

Revision ID: 002
Revises: 001
Create Date: 2023-10-04 12:00:00
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade():
    """Upgrade the database schema by adding the teacher_id column to the courses table."""
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Create a foreign key constraint linking teacher_id to the Teacher table
    op.create_foreign_key(
        'fk_courses_teacher_id',  # Constraint name
        'courses',                 # Source table
        'teachers',                # Destination table
        ['teacher_id'],            # Source columns
        ['id'],                    # Destination columns
        ondelete='SET NULL'        # Handle deletion: set teacher_id to NULL if teacher is deleted
    )


def downgrade():
    """Downgrade the database schema by removing the teacher_id column from the courses table."""
    op.drop_constraint('fk_courses_teacher_id', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```