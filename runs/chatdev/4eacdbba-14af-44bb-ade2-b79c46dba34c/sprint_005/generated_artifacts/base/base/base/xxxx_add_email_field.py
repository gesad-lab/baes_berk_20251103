'''
Migration script to add email field to Student entity.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
def downgrade():
    op.drop_column('students', 'email')