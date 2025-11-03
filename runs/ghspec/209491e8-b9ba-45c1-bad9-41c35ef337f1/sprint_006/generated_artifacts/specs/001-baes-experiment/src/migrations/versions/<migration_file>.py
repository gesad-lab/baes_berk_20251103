from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = 'xxxxxxx_add_teacher_id_to_courses'
down_revision = None  # Update this based on last migration
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration to add teacher_id to courses table."""
    # Add a new column 'teacher_id' to the 'courses' table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))

    # Create a foreign key relationship with the 'teachers' table
    op.create_foreign_key('fk_courses_teachers', 'courses', 'teachers', ['teacher_id'], ['id'])


def downgrade():
    """Revert the migration by removing teacher_id from courses table."""
    # Drop the foreign key and the column if rolled back
    op.drop_constraint('fk_courses_teachers', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')