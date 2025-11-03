from alembic import op
import sqlalchemy as sa

# Upgrade function to create the teachers table
def upgrade():
    # Create the teachers table with id, name, and email fields
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True),
    )

# Downgrade function to drop the teachers table
def downgrade():
    # Drop the teachers table if it exists
    op.drop_table('teachers')