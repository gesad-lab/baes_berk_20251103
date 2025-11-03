```python
"""Add StudentCourses mapping table

Revision ID: <timestamp>
Revises: 
Create Date: <timestamp>

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None  # Replace with appropriate previous revision if applicable
branch_labels = None
depends_on = None


def upgrade():
    # Create the 'student_courses' table to establish a many-to-many relationship
    op.create_table(
        'student_courses',
        sa.Column('id', sa.Integer(), primary_key=True),  # Unique identifier for the relationship
        sa.Column('student_id', sa.Integer(), nullable=False),  # Foreign key linking to the Student table
        sa.Column('course_id', sa.Integer(), nullable=False),  # Foreign key linking to the Course table
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),  # Set foreign key constraints
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ondelete='CASCADE'),  # Set foreign key constraints
        sa.PrimaryKeyConstraint('student_id', 'course_id')  # Composite primary key
    )


def downgrade():
    # Drop the 'student_courses' table if we need to revert migrations
    op.drop_table('student_courses')
```