from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2023_10_01_create_teachers_table'  # Unique identifier for this migration
down_revision = 'yyyyyyyyyyyy'  # Replace with the latest migration revision ID
branch_labels = None
depends_on = None


def upgrade():
    """Create the Teacher table with necessary fields."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.String(length=36), primary_key=True),  # Unique ID for teacher
        sa.Column('name', sa.String(length=255), nullable=False),  # Name of the teacher
        sa.Column('email', sa.String(length=255), nullable=False, unique=True)  # Unique email of the teacher
    )


def downgrade():
    """Drop the Teacher table if this migration is reversed."""
    op.drop_table('teachers')  # Drop the teachers table on downgrade operation