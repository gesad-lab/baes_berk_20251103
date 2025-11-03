```python
"""Add student-course association.

This migration creates an association table called `student_courses` to establish
a many-to-many relationship between students and courses. It ensures that existing
data remains intact while implementing the new schema.
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None  # Adjust based on the previous migration
branch_labels = None
depends_on = None

def upgrade():
    """Run the upgrade migration to add the student_courses association table."""
    # Create the association table for many-to-many relationship
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )


def downgrade():
    """Run the downgrade migration to remove the student_courses association table."""
    # Drop the association table
    op.drop_table('student_courses')
```