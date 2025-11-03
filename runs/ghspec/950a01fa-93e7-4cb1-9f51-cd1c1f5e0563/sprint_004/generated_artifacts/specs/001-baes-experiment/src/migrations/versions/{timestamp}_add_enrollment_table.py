```python
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'timestamp'  # Replace with the actual timestamp when the migration is created
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    """Create the enrollment table to establish a many-to-many relationship between students and courses."""
    # Create the enrollment table
    op.create_table(
        'enrollment',
        sa.Column('id', sa.Integer(), primary_key=True),  # Primary key for enrollment
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), nullable=False),  # Foreign key to students
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), nullable=False),  # Foreign key to courses
        sa.Column('enrolled_on', sa.DateTime(), server_default=sa.func.now()),  # Timestamp of enrollment
        sa.PrimaryKeyConstraint('student_id', 'course_id')  # Composite primary key
    )

def downgrade():
    """Drop the enrollment table if it exists."""
    op.drop_table('enrollment')
```