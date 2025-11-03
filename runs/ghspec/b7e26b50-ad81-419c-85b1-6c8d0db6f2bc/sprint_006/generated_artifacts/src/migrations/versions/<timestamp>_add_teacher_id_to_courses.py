```python
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'XXXXXXXXXXXXX'  # Replace with a unique revision identifier
down_revision = None  # Set to the previous migration's revision id, if any
branch_labels = None
depends_on = None

def upgrade():
    """Add teacher_id column to courses table."""
    # Adding the teacher_id column with foreign key reference to Teachers table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key(
        'fk_teacher_id',  # the name of the foreign key constraint
        'courses',  # the source table
        'teachers',  # the target table
        ['teacher_id'],  # source column(s)
        ['id'],  # target column(s)
        ondelete='SET NULL'  # behavior on deletion
    )

def downgrade():
    """Remove teacher_id column from courses table."""
    # Dropping the foreign key constraint and the column
    op.drop_constraint('fk_teacher_id', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```