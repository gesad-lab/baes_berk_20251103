'''
Migration script to add courses table to the database.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
def downgrade():
    op.drop_table('courses')  # Remove courses table