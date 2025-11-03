from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = '<timestamp>'  # replace with the actual timestamp
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),  # Ensure that emails are unique
    )

def downgrade():
    # Drop the teachers table if it exists
    op.drop_table('teachers')