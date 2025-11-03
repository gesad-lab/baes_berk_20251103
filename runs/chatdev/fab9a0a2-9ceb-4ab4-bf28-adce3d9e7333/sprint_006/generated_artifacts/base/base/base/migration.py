'''
Database migration script to add Course table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_course_table'
down_revision = 'add_email_to_student'
branch_labels = None
depends_on = None
def upgrade():
    # Create the 'courses' table without affecting existing 'students' table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
def downgrade():
    # Drop the 'courses' table if needed
    op.drop_table('courses')