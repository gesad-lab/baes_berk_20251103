```python
# /src/database/migrations/xxxx_add_course_ids_to_students.py

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'xxxx_add_course_ids_to_students'
down_revision = None  # Update this with the latest revision if applicable
branch_labels = None
depends_on = None

def upgrade():
    # Add a new column `course_ids` to the `students` table to store associated course IDs
    op.add_column('students', sa.Column('course_ids', sa.ARRAY(sa.Integer), nullable=True))

def downgrade():
    # Remove the `course_ids` column if we need to downgrade the database
    op.drop_column('students', 'course_ids')
```