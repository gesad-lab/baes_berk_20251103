```python
# /src/database/migrations/xxxxxx_add_teacher_relationship_to_courses.py

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxx_add_teacher_relationship_to_courses'
down_revision = 'previous_revision_id'  # replace with the actual previous revision id
branch_labels = None
depends_on = None

def upgrade():
    """Apply changes to the database to add the teacher relationship to the courses table."""
    # Add a new column 'teacher_id' to the 'courses' table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Create a foreign key constraint linking 'teacher_id' in 'courses' to 'id' in 'teachers'
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    """Revert changes made in the upgrade function."""
    # Drop the foreign key constraint from 'courses'
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    
    # Drop the 'teacher_id' column from the 'courses' table
    op.drop_column('courses', 'teacher_id')
```