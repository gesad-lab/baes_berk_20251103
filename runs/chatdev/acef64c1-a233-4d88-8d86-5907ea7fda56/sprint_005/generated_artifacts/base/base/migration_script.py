'''
Database migration script to add Course entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_course_entity'
down_revision = 'add_email_to_student'  # or the previous revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
def downgrade():
    # Drop the courses table
    op.drop_table('courses')