```python
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Unique revision identifier
down_revision = None  # Previous revision identifier
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration to create the student_courses junction table."""
    op.create_table(
        'student_courses',  # Name of the junction table
        sa.Column('student_id', sa.Integer(), nullable=False),  # Foreign key for Student
        sa.Column('course_id', sa.Integer(), nullable=False),   # Foreign key for Course
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),  # Referencing Student table
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),    # Referencing Course table
        sa.PrimaryKeyConstraint('student_id', 'course_id')  # Composite primary key
    )

def downgrade():
    """Revert the migration by dropping the student_courses table."""
    op.drop_table('student_courses')  # Remove the junction table
```