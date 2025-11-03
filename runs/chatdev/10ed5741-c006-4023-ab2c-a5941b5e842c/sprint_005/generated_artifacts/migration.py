'''
Migration script to add Teacher table and preserve existing data.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teacher_table'
down_revision = 'add_student_courses_table'  # Assuming this is the last migration
branch_labels = None
depends_on = None
def upgrade():
    # Create the Teacher table
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
def downgrade():
    # Drop the Teacher table
    op.drop_table('teachers')