from alembic import op
import sqlalchemy as sa

# Migration version identifier
revision = 'def456_add_teacher_id_to_courses'
down_revision = 'previous_revision_id'  # replace with the actual previous revision ID
branch_labels = None
depends_on = None

def upgrade():
    """Add teacher_id column to the courses table to establish relationship with teachers."""
    # Add the `teacher_id` column to the `courses` table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Create a foreign key constraint linking the `teacher_id` to the `id` of the `teachers` table
    op.create_foreign_key(
        'fk_teacher_id',  # name of the foreign key constraint
        'courses',        # name of the source table
        'teachers',       # name of the target table
        ['teacher_id'],   # source column
        ['id'],           # target column
        ondelete='SET NULL'  # behavior on delete
    )

def downgrade():
    """Remove teacher_id column from courses table during a downgrade."""
    # Drop the foreign key constraint
    op.drop_constraint('fk_teacher_id', 'courses', type_='foreignkey')
    
    # Drop the `teacher_id` column
    op.drop_column('courses', 'teacher_id')