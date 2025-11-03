from alembic import op
import sqlalchemy as sa


def upgrade():
    """Create courses table with required fields."""
    # Create courses table with auto-incremented primary key, and required fields for name and level
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )


def downgrade():
    """Drop courses table on downgrade."""
    # Reverse the upgrade by dropping the courses table
    op.drop_table('courses')