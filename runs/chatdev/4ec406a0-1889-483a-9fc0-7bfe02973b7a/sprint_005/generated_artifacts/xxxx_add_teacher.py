'''
Migration script to add the Teacher table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '20231001_add_teacher'  # Update this to a unique revision ID
down_revision = '20231001_add_student_courses'  # Ensure this matches the last applied migration ID
branch_labels = None
depends_on = None
def upgrade():
    """Create the Teacher table in the database."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
def downgrade():
    """Drop the Teacher table from the database."""
    op.drop_table('teachers')