```python
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '001_add_email_to_student'
down_revision = None  # Update to the previous migration if exists
branch_labels = None
depends_on = None

def upgrade():
    # Adding the 'email' column to the 'students' table.
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    # Dropping the 'email' column from the 'students' table.
    op.drop_column('students', 'email')
```