'''
Migration script to add Course entity and update the database schema.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = 'previous_revision_id'  # Set to the last migration ID
branch_labels = None
depends_on = None
def upgrade():
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
    # Ensure existing Student data is preserved (no changes to the Student table)
def downgrade():
    op.drop_table('courses')