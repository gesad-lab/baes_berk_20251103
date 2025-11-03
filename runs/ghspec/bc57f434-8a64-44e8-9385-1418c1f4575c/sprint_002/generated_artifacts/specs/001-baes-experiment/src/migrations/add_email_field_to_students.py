```python
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine import reflection

# revision identifiers, used by Alembic.
revision = 'add_email_field_to_students'  # Update with a unique revision identifier
down_revision = None  # Adjust if you have existing migrations
branch_labels = None
depends_on = None


def upgrade():
    """Add email field to the students table."""
    # Check if the 'students' table exists before adding the new column
    conn = op.get_bind()
    inspector = reflection.Inspector.from_engine(conn)
    
    if 'students' in inspector.get_table_names():
        # Add the 'email' column to the 'students' table
        op.add_column('students', sa.Column('email', sa.String(), nullable=False))
    else:
        raise Exception("Table 'students' does not exist!")


def downgrade():
    """Remove email field from the students table."""
    # Check if the 'students' table exists before removing the column
    conn = op.get_bind()
    inspector = reflection.Inspector.from_engine(conn)
    
    if 'students' in inspector.get_table_names():
        op.drop_column('students', 'email')
    else:
        raise Exception("Table 'students' does not exist!")
```