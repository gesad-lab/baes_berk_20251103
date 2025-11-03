'''
Database migration script to add Course entity and email field to the Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Create courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
    # Add email column to students table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
def downgrade():
    # Drop courses table
    op.drop_table('courses')
    # Remove email column from students table
    op.drop_column('students', 'email')