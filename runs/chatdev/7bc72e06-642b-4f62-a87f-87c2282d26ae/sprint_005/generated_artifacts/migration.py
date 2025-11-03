'''
Migration script for adding Teacher table and preserving existing data.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teacher_table'
down_revision = 'add_course_table'  # Update this based on your last migration
def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True),
    )
def downgrade():
    # Drop the teachers table
    op.drop_table('teachers')