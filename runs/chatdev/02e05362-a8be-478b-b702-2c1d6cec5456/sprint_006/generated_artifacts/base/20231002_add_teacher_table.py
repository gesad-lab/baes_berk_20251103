'''
Migration script to add Teacher table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '20231002_add_teacher_table'  # Update with a unique revision ID
down_revision = '20231001_add_course_table'  # Ensure this is the correct previous migration ID
branch_labels = None
depends_on = None
def upgrade():
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
def downgrade():
    op.drop_table('teachers')