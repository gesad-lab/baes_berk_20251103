'''
Database migration script to add Teacher entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teacher_entity'
down_revision = 'add_course_entity'  # or the previous revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
    )
def downgrade():
    # Drop the teachers table
    op.drop_table('teachers')