'''
Migration script to add Teacher table while preserving existing Student and Course data.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '20231001_add_teacher_table'
down_revision = 'yyyyyy'  # Replace with the actual previous revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Create the Teacher table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
def downgrade():
    # Drop the Teacher table
    op.drop_table('teachers')