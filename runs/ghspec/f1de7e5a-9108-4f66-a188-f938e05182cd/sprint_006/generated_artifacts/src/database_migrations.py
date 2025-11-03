```python
# src/database_migrations.py

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'add_teacher_id_to_courses'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Add teacher_id column to courses table with foreign key referencing teachers table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    # Remove teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')
```