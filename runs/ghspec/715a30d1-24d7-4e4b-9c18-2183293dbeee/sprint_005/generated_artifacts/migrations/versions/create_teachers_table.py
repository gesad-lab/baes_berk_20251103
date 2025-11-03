from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'create_teachers_table'
down_revision = None  # Update with the correct previous revision if applicable
branch_labels = None
depends_on = None

def upgrade():
    """Create the teachers table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),  # Primary key with auto-increment
        sa.Column('name', sa.String(), nullable=False),    # Required name field
        sa.Column('email', sa.String(), nullable=False, unique=True),  # Required email field with uniqueness constraint
        sa.Column('created_at', sa.DateTime(), default=sa.func.current_timestamp()),  # Timestamp for creation
        sa.Column('updated_at', sa.DateTime(), default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp()),  # Timestamp for updates
    )

def downgrade():
    """Drop the teachers table."""
    op.drop_table('teachers')  # Reverse operation to drop the teachers table if needed