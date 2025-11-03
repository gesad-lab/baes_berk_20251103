from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create the teachers table with required fields
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),  # Name is required
        sa.Column('email', sa.String(), nullable=False, unique=True),  # Email is required and must be unique
    )

def downgrade():
    # Drop the teachers table if it exists
    op.drop_table('teachers')