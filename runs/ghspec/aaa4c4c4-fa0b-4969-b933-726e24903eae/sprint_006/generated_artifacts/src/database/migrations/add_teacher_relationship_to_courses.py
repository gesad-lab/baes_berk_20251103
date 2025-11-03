from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'add_teacher_relationship_to_courses'
down_revision = None  # Set to the appropriate previous migration revision ID
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration to add teacher_id to the courses table and create foreign key relationship."""
    # Add the teacher_id column as a foreign key referencing the teachers table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'])


def downgrade():
    """Revert the migration by dropping the foreign key and teacher_id column."""
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')