'''
Migration script to add Course table to the database.
This migration depends on the previous migration that adds the email column to the Student table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxx_add_course_table'
down_revision = 'xxxx_add_email_column'  # Ensure this is the last migration
branch_labels = None
depends_on = None
def upgrade():
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
def downgrade():
    op.drop_table('courses')