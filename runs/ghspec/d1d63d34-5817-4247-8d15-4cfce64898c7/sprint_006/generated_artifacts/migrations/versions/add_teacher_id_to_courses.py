```python
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'add_teacher_id_to_courses'
down_revision = None  # Replace with the appropriate revision if there is a previous one
branch_labels = None
depends_on = None


def upgrade():
    # Adding teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_course_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])


def downgrade():
    # Removing teacher_id column from the courses table
    op.drop_constraint('fk_course_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```