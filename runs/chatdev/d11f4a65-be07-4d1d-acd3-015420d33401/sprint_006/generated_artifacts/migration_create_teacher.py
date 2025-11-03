'''
Migration script to create teachers table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'unique_revision_id_3'  # Replace with a unique revision ID
down_revision = 'unique_revision_id_2'  # Ensure this is the last applied migration ID for student_courses
branch_labels = None
depends_on = None
def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
def downgrade():
    # Drop the teachers table
    op.drop_table('teachers')