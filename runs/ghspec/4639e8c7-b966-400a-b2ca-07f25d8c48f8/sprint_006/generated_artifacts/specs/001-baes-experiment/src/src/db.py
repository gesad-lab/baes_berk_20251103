```python
from sqlalchemy import Column, Integer, ForeignKey
from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = 'xxxx_add_teacher_id_to_courses'
down_revision = 'previous_revision_id'  # Replace with the actual previous revision ID
branch_labels = None
depends_on = None


def upgrade():
    """Add teacher_id column to courses table."""
    # Add the new teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Create a foreign key constraint on the teacher_id column
    op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'])


def downgrade():
    """Remove teacher_id column from courses table."""
    # Drop the foreign key constraint first
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    
    # Remove the teacher_id column
    op.drop_column('courses', 'teacher_id')
```