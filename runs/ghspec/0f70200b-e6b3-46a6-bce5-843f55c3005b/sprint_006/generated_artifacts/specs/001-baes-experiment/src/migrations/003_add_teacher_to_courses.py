```python
# migrations/003_add_teacher_to_courses.py

from sqlalchemy import create_engine, Column, Integer, ForeignKey
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '003'
down_revision = None  # Replace with the appropriate previous revision if multiple migrations exist
branch_labels = None
depends_on = None

def upgrade():
    """Add teacher_id column to courses table."""
    # Add the teacher_id column, which is a foreign key referencing the id of the teachers table
    op.add_column('courses', 
        Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True)
    )
    
def downgrade():
    """Remove teacher_id column from courses table."""
    # Drop the teacher_id column if we need to revert the migration
    op.drop_column('courses', 'teacher_id')
```