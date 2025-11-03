'''
Migration script to add Teacher table to the database.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with your revision ID
down_revision = None  # Replace with the previous revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Ensure existing Student and Course data is preserved
    # No specific operations are needed as the new table does not affect existing tables.
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Existing tables creation remains unchanged
    # ...
def downgrade():
    op.drop_table('teachers')
    # Existing tables drop remains unchanged
    # ...