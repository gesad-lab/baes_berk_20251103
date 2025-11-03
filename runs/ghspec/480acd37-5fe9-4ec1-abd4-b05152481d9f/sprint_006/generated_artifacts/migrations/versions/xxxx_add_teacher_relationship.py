from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = 'xxxx_add_teacher_relationship'
down_revision = 'previous_revision_id'  # Update with actual previous revision ID
branch_labels = None
depends_on = None


def upgrade():
    """Add teacher_id column to the courses table."""
    # Add the new column 'teacher_id' which references the 'id' column in the 'teachers' table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'], ondelete='SET NULL')


def downgrade():
    """Remove teacher_id column from the courses table."""
    # Drop the foreign key constraint and the column if we need to rollback the migration
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')