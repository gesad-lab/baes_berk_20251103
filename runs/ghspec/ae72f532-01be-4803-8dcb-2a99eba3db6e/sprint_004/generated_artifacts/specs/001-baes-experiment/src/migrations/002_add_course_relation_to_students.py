```python
"""Migration to add a course_ids field to the students table."""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_add_course_relation_to_students'
down_revision = '001_previous_migration'
branch_labels = None
depends_on = None


def upgrade():
    """Add the course_ids field to the students table."""
    op.add_column('students',
                  sa.Column('course_ids', sa.PickleType(), default=[]))  # Using PickleType for list of integers


def downgrade():
    """Remove the course_ids field from the students table."""
    op.drop_column('students', 'course_ids')
```