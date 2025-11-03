'''
Handles the database migration for adding the email field to the Student table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
def downgrade():
    op.drop_column('students', 'email')