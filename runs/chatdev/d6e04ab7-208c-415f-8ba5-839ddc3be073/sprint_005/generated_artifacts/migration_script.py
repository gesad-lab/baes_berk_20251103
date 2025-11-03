'''
Migration script to add Teacher table to the database.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with the actual revision ID
down_revision = 'yyyyyy'  # Replace with the actual down revision ID
def upgrade():
    # Check if the 'students' and 'courses' tables exist before creating the 'teachers' table
    if not op.get_bind().has_table('students'):
        raise Exception("The 'students' table does not exist. Migration cannot proceed.")
    if not op.get_bind().has_table('courses'):
        raise Exception("The 'courses' table does not exist. Migration cannot proceed.")
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
def downgrade():
    op.drop_table('teachers')