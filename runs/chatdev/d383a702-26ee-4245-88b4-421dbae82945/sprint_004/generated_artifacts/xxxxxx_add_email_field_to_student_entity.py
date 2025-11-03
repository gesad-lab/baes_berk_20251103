'''
Migration script to add email field to Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx_add_email_field_to_student_entity'
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Add the email column
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
def downgrade():
    # Remove the email column
    op.drop_column('students', 'email')