```python
# migrations/001_add_email_to_students.py

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '001_add_email_to_students'
down_revision = None  # Set this to the previous migration's identifier if applicable
branch_labels = None
depends_on = None

def upgrade():
    """Add the email column to the students table."""
    # Adding a new column 'email' that cannot be null
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    """Remove the email column from the students table."""
    # Dropping the 'email' column in case of a rollback
    op.drop_column('students', 'email')
```