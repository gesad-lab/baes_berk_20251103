```python
import sqlalchemy as sa
from alembic import op

# Revision identifiers, used by Alembic.
revision = 'xxxxxxx'  # Replace with a unique identifier
down_revision = None   # Replace with the previous migration ID if it exists
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration to add teacher_id column to the courses table."""
    # Use migrations to add the `teacher_id` column to the `courses` table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    """Revert the migration, dropping teacher_id column from the courses table."""
    op.drop_column('courses', 'teacher_id')
```