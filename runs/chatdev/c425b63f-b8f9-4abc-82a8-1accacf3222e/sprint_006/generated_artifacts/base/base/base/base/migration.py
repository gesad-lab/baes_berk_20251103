'''
Migration script to add email column to students table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    '''
    Add email column to the students table.
    '''
    # Step 1: Add email column as nullable
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Step 2: Populate existing records with a default value
    connection = op.get_bind()
    connection.execute("UPDATE students SET email = '' WHERE email IS NULL")
    # Step 3: Alter the column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    '''
    Remove email column from the students table.
    '''
    op.drop_column('students', 'email')