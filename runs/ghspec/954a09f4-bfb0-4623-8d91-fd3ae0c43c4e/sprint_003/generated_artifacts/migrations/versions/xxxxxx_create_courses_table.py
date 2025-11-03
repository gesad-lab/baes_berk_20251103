"""Create courses table"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxx'
down_revision = 'previous_revision'

def upgrade():
    # Create the courses table with required fields
    op.create_table('courses',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),  # Auto-incrementing ID
        sa.Column('name', sa.String(), nullable=False),  # Course name, cannot be null
        sa.Column('level', sa.String(), nullable=False),  # Course level, cannot be null
        sa.PrimaryKeyConstraint('id')  # Setting the primary key
    )

def downgrade():
    # Drop the courses table if downgrade is called
    op.drop_table('courses')