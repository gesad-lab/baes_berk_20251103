```python
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'add_teacher_id_to_courses'
down_revision = None  # Replace with the actual down_revision if necessary.
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration to add teacher_id to the courses table."""
    # Add the new column `teacher_id` to the `courses` table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    """Revert the migration by removing teacher_id from the courses table."""
    # Remove the `teacher_id` column in the downgrade
    op.drop_column('courses', 'teacher_id')
```