```python
"""Add teacher relationship to courses table

Revision ID: 2023_add_teacher_relationship_to_course
Revises: previous_revision_id
Create Date: 2023-10-01 12:00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2023_add_teacher_relationship_to_course'
down_revision = 'previous_revision_id'  # Replace with actual previous revision id
branch_labels = None
depends_on = None


def upgrade():
    """Upgrade the database schema to add a foreign key relationship for teacher_id in courses table."""
    # Add a new nullable column `teacher_id` to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Create a foreign key constraint linking `teacher_id` to `teachers.id`
    op.create_foreign_key('fk_teacher_id', 'courses', 'teachers', ['teacher_id'], ['id'])


def downgrade():
    """Downgrade the database schema by removing the teacher_id relationship."""
    # Drop the foreign key constraint
    op.drop_constraint('fk_teacher_id', 'courses', type_='foreignkey')
    
    # Remove the teacher_id column from the courses table
    op.drop_column('courses', 'teacher_id')
```