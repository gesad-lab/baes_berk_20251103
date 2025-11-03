```python
# migrations/versions/add_teacher_id.py

from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = 'add_teacher_id'
down_revision = None  # Set this to the previous migration if applicable
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Apply the migration to add the teacher_id column to the Courses table."""
    # Add a new column 'teacher_id' that allows null values
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))

    # Create a foreign key constraint linking teacher_id to the id in the teachers table
    op.create_foreign_key(
        'fk_teacher_courses', 
        source_table='courses', 
        referent_table='teachers', 
        local_cols=['teacher_id'], 
        remote_cols=['id'], 
        ondelete='SET NULL'  # Keep existing courses if teacher is deleted
    )


def downgrade() -> None:
    """Revert the migration by dropping the teacher_id column from the Courses table."""
    # Drop the foreign key constraint first to prevent errors
    op.drop_constraint('fk_teacher_courses', table_name='courses', type_='foreignkey')
    
    # Remove the 'teacher_id' column from the Courses table
    op.drop_column('courses', 'teacher_id')
```