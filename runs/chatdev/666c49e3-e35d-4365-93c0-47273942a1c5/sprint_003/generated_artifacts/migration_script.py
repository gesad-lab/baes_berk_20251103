'''
Create a new migration script using Alembic to add Course table and preserve existing Student data.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
def downgrade():
    op.drop_table('courses')