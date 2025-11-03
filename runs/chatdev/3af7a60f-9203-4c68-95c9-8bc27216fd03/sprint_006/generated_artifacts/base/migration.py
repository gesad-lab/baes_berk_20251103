'''
Migration script to add teachers table to the database.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True),
    )
    # No need to migrate existing data for students and courses
def downgrade():
    op.drop_table('teachers')  # Remove teachers table