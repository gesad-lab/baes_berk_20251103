'''
Migration script to add email field to the Student table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with your revision ID
down_revision = None  # Replace with your previous revision ID
branch_labels = None
depends_on = None
def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
def downgrade():
    op.drop_column('students', 'email')