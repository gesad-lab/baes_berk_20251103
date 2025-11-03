---
```
# Migration to add teacher_id to courses table

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_teacher_id_to_courses'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Add teacher_id column to courses table."""
    # Creating new column 'teacher_id' referencing 'teachers.id'
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_courses_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade() -> None:
    """Remove teacher_id column from courses table."""
    # Dropping foreign key relationship and the column
    op.drop_constraint('fk_courses_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```
