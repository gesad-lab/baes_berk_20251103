```python
# File: migrations/002_add_teacher_id_to_courses.py

from alembic import op
import sqlalchemy as sa

# Upgrade function to add teacher_id column to courses table
def upgrade() -> None:
    # Add a new column 'teacher_id' to the 'courses' table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Create a foreign key relationship with 'teachers' table
    op.create_foreign_key(
        'fk_teacher_course',  # Name of the foreign key constraint
        'courses',            # Source table
        'teachers',          # Target table
        ['teacher_id'],      # Source column(s)
        ['id'],              # Target column(s)
        ondelete='SET NULL'  # Allow deletion of teachers without removing courses
    )

# Downgrade function to remove teacher_id column from courses table
def downgrade() -> None:
    # Drop the foreign key constraint
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    
    # Remove the 'teacher_id' column from the 'courses' table
    op.drop_column('courses', 'teacher_id')
```