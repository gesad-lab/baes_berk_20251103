'''
Run Alembic migrations.
'''
# Ensure to create a migration script for the Teacher table
from alembic import op
import sqlalchemy as sa
def upgrade():
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False)
    )
def downgrade():
    op.drop_table('teachers')