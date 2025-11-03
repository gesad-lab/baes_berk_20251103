'''
Handles database migrations for the application.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    '''
    Upgrade the database schema to include the new Teacher table.
    '''
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
    )
    # Do not recreate courses and student_courses tables
def downgrade():
    '''
    Downgrade the database schema by dropping the Teacher table.
    '''
    op.drop_table('teachers')