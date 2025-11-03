```python
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxx_add_teacher_id_to_courses'
down_revision = None  # Replace with the previous migration ID if applicable
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Add a new column `teacher_id` to the `courses` table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Optionally: Add foreign key constraint to ensure data integrity between courses and teachers
    op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade() -> None:
    # Remove the foreign key constraint
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    
    # Drop the `teacher_id` column from the `courses` table
    op.drop_column('courses', 'teacher_id')
```