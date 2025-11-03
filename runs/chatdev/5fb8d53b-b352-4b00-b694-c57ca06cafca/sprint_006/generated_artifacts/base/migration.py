'''
Handles the database migration for adding the Teacher table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create the Teacher table
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    # Do not recreate the student_course table here
def downgrade():
    op.drop_table('teachers')
    # Do not drop the student_course table here