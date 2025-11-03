'''
Migration script to add email field to Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'unique_revision_id_for_email'  # Replace with actual unique revision ID
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
def downgrade():
    op.drop_column('students', 'email')