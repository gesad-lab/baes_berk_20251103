'''
Migration script to add Course table to the database.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_course_table'
down_revision = 'add_email_field_to_student'
branch_labels = None
depends_on = None
def upgrade():
    # Check if the 'courses' table already exists before creating it
    if not op.get_bind().has_table('courses'):
        op.create_table(
            'courses',
            sa.Column('id', sa.Integer, primary_key=True, index=True),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('level', sa.String(), nullable=False),
        )
def downgrade():
    # Ensure that the 'courses' table is dropped if it exists
    if op.get_bind().has_table('courses'):
        op.drop_table('courses')