```python
# app/database.py

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'xxxxxx_create_teachers_table'  # Replace with the generated revision ID
down_revision = 'xxxxxx_previous_revision'  # Replace with the previous revision ID
branch_labels = None
depends_on = None


def upgrade():
    """Create Teachers table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.UniqueConstraint('email', name='uq_teachers_email')  # Ensure email uniqueness
    )


def downgrade():
    """Drop Teachers table."""
    op.drop_table('teachers')
```