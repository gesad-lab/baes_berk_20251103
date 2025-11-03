```python
# migrations/20231011123000_add_teacher_id_to_courses.py

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '20231011123000'
down_revision = 'previous_revision_id'  # Replace with the last migration's revision ID
branch_labels = None
depends_on = None

def upgrade():
    """Add teacher_id column to the courses table to establish relationship with teachers."""
    # Add a new column 'teacher_id' which will be a foreign key referencing the teachers table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_course_teacher', 'courses', 'teachers', ['teacher_id'], ['id'], ondelete='SET NULL')

def downgrade():
    """Remove teacher_id column from the courses table."""
    # Drop the foreign key constraint first, then remove the column
    op.drop_constraint('fk_course_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```