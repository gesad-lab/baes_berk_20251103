'''
Migration script to add email column to Student table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxx_add_email_column'
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))  # Set nullable=False for migration
def downgrade():
    op.drop_column('students', 'email')