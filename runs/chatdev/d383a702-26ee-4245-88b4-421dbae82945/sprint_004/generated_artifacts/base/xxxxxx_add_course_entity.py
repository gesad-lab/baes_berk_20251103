'''
Migration script to add Course entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx_add_course_entity'
down_revision = 'xxxxxx_add_email_field_to_student_entity'  # Updated to reference the correct previous migration
branch_labels = None
depends_on = None
def upgrade():
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
def downgrade():
    # Drop the courses table
    op.drop_table('courses')