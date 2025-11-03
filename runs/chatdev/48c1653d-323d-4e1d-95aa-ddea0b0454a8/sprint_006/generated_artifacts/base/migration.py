'''
Migration script to add Teacher table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teacher_table'
down_revision = 'add_email_to_student'  # Update this to the last migration
branch_labels = None
depends_on = None
def upgrade():
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )
def downgrade():
    op.drop_table('teachers')