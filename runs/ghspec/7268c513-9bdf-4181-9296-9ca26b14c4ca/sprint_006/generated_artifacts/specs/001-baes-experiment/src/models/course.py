```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    """Add teacher_id foreign key column to the courses table."""
    # Adding the teacher_id column which refers to the id of the teachers table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id')))

def downgrade():
    """Remove teacher_id column from the courses table."""
    # Dropping the teacher_id column if we need to downgrade the migration
    op.drop_column('courses', 'teacher_id')
```