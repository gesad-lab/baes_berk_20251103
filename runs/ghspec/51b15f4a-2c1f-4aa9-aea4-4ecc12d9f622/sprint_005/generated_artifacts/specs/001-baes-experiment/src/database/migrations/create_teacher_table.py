# database/migrations/create_teacher_table.py

from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = 'xyz1234'  # replace with your revision id
down_revision = 'previous_revision_id'  # replace with appropriate previous revision id
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration to create the Teacher table."""
    # Create the 'teachers' table with the specified columns
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),  # Name is a required field
        sa.Column('email', sa.String(), nullable=False)  # Email is a required field
    )


def downgrade():
    """Revert the migration to drop the Teacher table."""
    # Drop the 'teachers' table if it exists
    op.drop_table('teachers')