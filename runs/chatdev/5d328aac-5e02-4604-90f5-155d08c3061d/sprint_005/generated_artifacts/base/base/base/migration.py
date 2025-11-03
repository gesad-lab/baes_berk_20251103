'''
Migration script to add email field to Student table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_email_field_to_student'
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))  # Changed to nullable=False
def downgrade():
    op.drop_column('students', 'email')