```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from alembic import op
import sqlalchemy as sa

# This is the migration file to add a foreign key column 'teacher_id' to the 'courses' table
# It links to the 'id' column in 'teachers' table while preserving existing data.

# revision identifiers, used by Alembic.
revision = '<timestamp>'  # Please replace <timestamp> with the current timestamp
down_revision = None  # Define the down_revision ID based on the previous migration
branch_labels = None
depends_on = None

def upgrade():
    """Add teacher_id column to courses table."""
    # Add 'teacher_id' column to the existing 'courses' table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Create a foreign key constraint linking 'teacher_id' to 'id' of 'teachers'
    op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    """Remove teacher_id column from courses table."""
    # Drop the foreign key constraint first to ensure safe deletion
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    
    # Remove 'teacher_id' column from 'courses' table
    op.drop_column('courses', 'teacher_id')
```