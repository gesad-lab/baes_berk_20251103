'''
Migration script to create the courses table while preserving existing Student data.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
def downgrade():
    op.drop_table('courses')