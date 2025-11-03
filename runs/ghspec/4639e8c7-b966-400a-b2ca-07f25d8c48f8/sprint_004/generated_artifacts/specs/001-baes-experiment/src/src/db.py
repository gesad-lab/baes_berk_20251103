```python
# src/db.py

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_student_course_join_table'
down_revision = None  # This should correspond to the previous migration
branch_labels = None
depends_on = None

def upgrade():
    """Create the student_course join table for many-to-many relationship."""
    op.create_table('student_course',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade():
    """Drop the student_course join table."""
    op.drop_table('student_course')
```