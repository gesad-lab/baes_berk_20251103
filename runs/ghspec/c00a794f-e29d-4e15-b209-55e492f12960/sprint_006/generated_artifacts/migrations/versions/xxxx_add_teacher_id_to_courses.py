```python
# migrations/versions/xxxx_add_teacher_id_to_courses.py
from alembic import op
import sqlalchemy as sa

# Migration script to add a teacher_id column to the courses table
def upgrade():
    # Add a new column 'teacher_id' to the 'courses' table, allowing NULL values for existing rows
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Create a foreign key relationship with the 'teachers' table
    op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    # Rollback foreign key constraint on 'courses' table
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    # Remove the 'teacher_id' column from 'courses' table
    op.drop_column('courses', 'teacher_id')
```