```python
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '002_add_teacher_relationship_to_courses'
down_revision = None  # Set this to the ID of the previous migration if applicable
branch_labels = None
depends_on = None

def upgrade():
    # Add the teacher_id column to the courses table, allowing null values initially
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    # Remove the teacher_id column from the courses table on downgrade
    op.drop_column('courses', 'teacher_id')
```