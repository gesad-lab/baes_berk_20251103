```python
# migrations/versions/<timestamp>_create_student_courses_table.py

from flask_sqlalchemy import SQLAlchemy
from alembic import op
import sqlalchemy as sa

# Create a new database instance
db = SQLAlchemy()

# Revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Create the student_courses junction table."""
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, nullable=False),
        sa.Column('course_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], name='fk_student'),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name='fk_course'),
        sa.PrimaryKeyConstraint('student_id', 'course_id')  # Composite primary key
    )

def downgrade() -> None:
    """Drop the student_courses junction table."""
    op.drop_table('student_courses')
```