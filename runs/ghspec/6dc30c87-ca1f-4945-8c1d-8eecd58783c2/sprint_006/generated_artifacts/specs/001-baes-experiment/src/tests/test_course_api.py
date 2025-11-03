```python
"""Add teacher_id to courses table

Revision ID: 23456789def0
Revises: 123456789abc
Create Date: 2023-10-02 12:30:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '23456789def0'
down_revision = '123456789abc'
branch_labels = None
depends_on = None


def upgrade():
    """Add the teacher_id column to the courses table as a foreign key."""
    # Adding the 'teacher_id' column to 'courses' table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id')))

    
def downgrade():
    """Remove the teacher_id column from the courses table."""
    # Dropping the 'teacher_id' column from 'courses' table if necessary
    op.drop_column('courses', 'teacher_id')
```