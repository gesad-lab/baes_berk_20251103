```python
"""007_create_teacher_table.py

This script defines a database migration for creating a new table 'teachers'
to store teacher information, including their names and emails while ensuring
the existing data in the Student and Course tables are preserved.
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '007_create_teacher_table'
down_revision = '006_previous_migration'  # Update this to the correct previous migration ID
branch_labels = None
depends_on = None


def upgrade():
    """Create the 'teachers' table."""
    # Create the teachers table with an auto-incrementing primary key
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )


def downgrade():
    """Drop the 'teachers' table."""
    # Drop the teachers table when downgrading the migration
    op.drop_table('teachers')
```