```python
# migrations/versions/xxxx_create_courses_table.py
from alembic import op
import sqlalchemy as sa

# Migration script to create the courses table
def upgrade():
    # Create the courses table with the specified columns
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )

def downgrade():
    # Drop the courses table in case of a rollback
    op.drop_table('courses')
```