```python
"""CreateTeacherIdInCourse

Revision ID: abc123def456
Revises: previous_revision_id  # Update with actual previous revision ID
Create Date: 2023-10-05 12:34:56.789012  # Use the current date and time

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abc123def456'  # Update with actual revision ID
down_revision = 'previous_revision_id'  # Update with actual previous revision ID
branch_labels = None
depends_on = None


def upgrade():
    """Upgrade the database schema.

    This function adds the 'teacher_id' foreign key to the 'courses' table. 
    The 'teacher_id' column links to the 'id' column in the 'teachers' table.
    """
    # Add teacher_id column to courses table with foreign key constraint
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'])

    
def downgrade():
    """Downgrade the database schema.

    This function reverses the changes made in the upgrade function by
    dropping the 'teacher_id' foreign key and column from the 'courses' table.
    """
    # Drop foreign key constraint
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    # Drop teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')
```