"""Add email field to Student
Revision ID: <revision_id>
Revises: <previous_revision_id>
Create Date: <date>
"""
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '<revision_id>'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None
def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
def downgrade():
    op.drop_column('students', 'email')