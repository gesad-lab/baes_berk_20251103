'''
Migration script to add the teachers table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx_add_teacher_table'
down_revision = 'xxxxxx'  # Updated to reflect the correct previous migration revision
branch_labels = None
depends_on = None
def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )
def downgrade():
    op.drop_table('teachers')